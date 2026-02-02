import json
from pathlib import Path
from typing import Dict, List


CALL_GRAPH_FILE = "call_graph.json"
INSIGHTS_FILE = "architecture_insights.json"
OUTPUT_FILE = "llm_context.txt"
NODE_DOCS_FILE = "llm_nodes.json"


# -------------------------
# Load helpers
# -------------------------
def load_json(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# -------------------------
# Natural language context
# -------------------------
def build_natural_language_context(
    call_graph: Dict[str, List[str]],
    insights: Dict
) -> str:
    lines = []

    lines.append("CODE EXECUTION & DEPENDENCY SUMMARY")
    lines.append("---------------------------------\n")

    for caller, callees in call_graph.items():
        if not callees:
            continue
        for callee in callees:
            lines.append(f"Function {caller} calls {callee}.")

    cycles = insights.get("cycles", [])
    if cycles:
        lines.append("\nARCHITECTURAL RISKS")
        lines.append("-------------------")

        for idx, cycle in enumerate(cycles, 1):
            severity = cycle.get("severity", "UNKNOWN")
            path = " → ".join(cycle["path"])
            lines.append(f"Cycle {idx} ({severity}): {path}")

        lines.append("\nRecommendation:")
        lines.append(
            "Refactor shared logic out of cycles and reduce coupling "
            "between involved modules."
        )
    else:
        lines.append("\nNo cyclic dependencies detected.")

    return "\n".join(lines)


# -------------------------
# GraphRAG-style node docs
# -------------------------
def build_node_documents(
    call_graph: Dict[str, List[str]],
    insights: Dict
) -> List[Dict]:
    cycle_map = {}

    for cycle in insights.get("cycles", []):
        for node in cycle["path"]:
            cycle_map[node] = cycle.get("severity", "UNKNOWN")

    node_docs = []

    for node, callees in call_graph.items():
        module = node.split(".")[0]

        node_docs.append({
            "node": node,
            "type": "function",
            "module": module,
            "calls": callees,
            "part_of_cycle": node in cycle_map,
            "cycle_severity": cycle_map.get(node)
        })

    return node_docs


# -------------------------
# Runner
# -------------------------
def main():
    if not Path(CALL_GRAPH_FILE).exists():
        raise FileNotFoundError("call_graph.json not found")

    call_graph_data = load_json(CALL_GRAPH_FILE)
    call_graph = call_graph_data.get("call_graph", {})

    insights = {}
    if Path(INSIGHTS_FILE).exists():
        insights = load_json(INSIGHTS_FILE)

    # Build LLM-readable text
    context_text = build_natural_language_context(call_graph, insights)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(context_text)

    # Build GraphRAG node docs
    node_docs = build_node_documents(call_graph, insights)
    with open(NODE_DOCS_FILE, "w", encoding="utf-8") as f:
        json.dump(node_docs, f, indent=2)

    print("🧠 LLM context generated")
    print(f"  - {OUTPUT_FILE}")
    print(f"  - {NODE_DOCS_FILE}")


if __name__ == "__main__":
    main()
