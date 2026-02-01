import json
from collections import defaultdict
from pathlib import Path

CALL_GRAPH_FILE = "call_graph.json"
CYCLES_FILE = "cycles.json"
OUTPUT_FILE = "architecture_insights.json"


# -------------------------
# Load data
# -------------------------
def load_call_graph():
    with open(CALL_GRAPH_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("call_graph", {})


def load_cycles():
    path = Path(CYCLES_FILE)
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# -------------------------
# Cycle severity
# -------------------------
def classify_cycle(cycle):
    length = len(cycle) - 1  # last node repeats
    if length == 2:
        return "HIGH"
    elif length == 3:
        return "MEDIUM"
    return "LOW"


# -------------------------
# Fan-in analysis
# -------------------------
def compute_fan_in(call_graph):
    fan_in = defaultdict(int)
    for caller, callees in call_graph.items():
        for callee in callees:
            fan_in[callee] += 1
    return fan_in


# -------------------------
# Main analysis
# -------------------------
def analyze_architecture():
    call_graph = load_call_graph()
    cycles = load_cycles()

    fan_in = compute_fan_in(call_graph)

    cycle_reports = []
    cycle_nodes = set()

    for cycle in cycles:
        severity = classify_cycle(cycle)
        cycle_nodes.update(cycle)
        cycle_reports.append({
            "path": cycle,
            "severity": severity
        })

    hotspots = sorted(
        [node for node, count in fan_in.items() if count >= 2],
        key=lambda n: fan_in[n],
        reverse=True
    )

    insights = {
        "cycle_count": len(cycles),
        "cycles": cycle_reports,
        "hotspots": [
            {"node": node, "fan_in": fan_in[node]}
            for node in hotspots
        ],
        "recommendation": (
            "Refactor shared logic out of cycles and reduce fan-in on hotspot nodes."
            if cycles else
            "No architectural cycles detected. Maintain modular boundaries."
        )
    }

    return insights


# -------------------------
# Output
# -------------------------
def print_summary(insights):
    print("\n🏗️ ARCHITECTURE RISK SUMMARY")
    print("-" * 32)

    print(f"Cycles detected: {insights['cycle_count']}")
    for idx, cycle in enumerate(insights["cycles"], 1):
        print(f"\nCycle {idx}: ({cycle['severity']})")
        print("  " + " → ".join(cycle["path"]))

    if insights["hotspots"]:
        print("\nHotspot Nodes:")
        for h in insights["hotspots"]:
            print(f"  - {h['node']} (fan-in: {h['fan_in']})")
    else:
        print("\nNo hotspots detected.")

    print("\nRecommendation:")
    print(f"  {insights['recommendation']}")


def save_insights(insights):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(insights, f, indent=2)
    print(f"\n💾 Saved {OUTPUT_FILE}")


# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    insights = analyze_architecture()
    print_summary(insights)
    save_insights(insights)
