import json
import sys
from pathlib import Path

INSIGHTS_FILE = "architecture_insights.json"


def load_insights():
    path = Path(INSIGHTS_FILE)
    if not path.exists():
        print("❌ architecture_insights.json not found")
        sys.exit(2)

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def evaluate(insights):
    high_cycles = [
        c for c in insights.get("cycles", [])
        if c.get("severity") == "HIGH"
    ]

    medium_cycles = [
        c for c in insights.get("cycles", [])
        if c.get("severity") == "MEDIUM"
    ]

    print("\n🚦 ARCHITECTURE QUALITY GATE")
    print("-" * 34)

    if high_cycles:
        print(f"❌ FAIL — {len(high_cycles)} HIGH severity cycle(s)\n")
        for idx, c in enumerate(high_cycles, 1):
            print(f"HIGH Cycle {idx}:")
            print("  " + " → ".join(c["path"]))
        print("\nAction required: break cycles immediately.")
        sys.exit(1)

    if medium_cycles:
        print(f"⚠️ WARN — {len(medium_cycles)} MEDIUM severity cycle(s)\n")
        for idx, c in enumerate(medium_cycles, 1):
            print(f"MEDIUM Cycle {idx}:")
            print("  " + " → ".join(c["path"]))
        print("\nRecommendation: schedule refactoring.")
        sys.exit(0)

    print("✅ PASS — No architectural blockers detected")
    sys.exit(0)


if __name__ == "__main__":
    insights = load_insights()
    evaluate(insights)
