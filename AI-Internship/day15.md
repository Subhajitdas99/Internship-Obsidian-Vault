# Day 15 — Architecture Scoring & Risk Signals

## Context
By Day 14, the Mini Code Analyzer could:
- Build call graphs
- Detect cyclic dependencies
- Visualize architecture using Mermaid

Day 15 focuses on **extracting insights** from those graphs instead of only visualizing them.

Modern static analysis tools do not stop at graphs — they provide **actionable signals**.

---

## Objectives
- Assign severity levels to detected cycles
- Identify architectural hotspots
- Generate machine-readable insights for AI/LLM pipelines

---

## Work Done

### 1. Cycle Severity Scoring
Each detected cycle is classified using its length:
- Length 2 → HIGH severity
- Length 3 → MEDIUM severity
- Length ≥4 → LOW severity

This helps prioritize refactoring efforts.

---

### 2. Hotspot Detection
Identified functions and modules that:
- Are involved in multiple cycles
- Have high fan-in (many callers)

These represent high-risk areas of the codebase.

---

### 3. Architecture Risk Summary
Generated a concise summary highlighting:
- Total cycles detected
- Severity distribution
- Most risky modules and functions

This mirrors real-world architecture review reports.

---

### 4. AI / GraphRAG-Ready Output
Produced a structured `architecture_insights.json` file containing:
- Cycle paths
- Severity labels
- Hotspot identifiers
- Refactoring recommendations

This output can be directly consumed by:
- GraphRAG pipelines
- LLM-based code assistants
- Automated refactoring tools

---

## Key Learnings
- Static analysis value comes from **signals**, not raw data
- Graph metrics can guide architectural decisions
- Structured outputs enable AI-driven reasoning

---

## Next Steps
- Historical trend analysis (cycle growth over time)
- CI integration for architecture regression checks
- LLM-powered refactoring suggestions
