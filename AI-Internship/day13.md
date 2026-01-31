Day 13 – Cyclic Dependency Detection & Visualization
Context

As static analysis matures, understanding dependency cycles becomes critical.
Cyclic dependencies often indicate:

Tight coupling

Poor modular boundaries

High refactoring risk

Today’s goal was to detect, validate, and visualize cycles in the extracted call graph.

Objectives for Day 13

Detect cyclic dependencies in the call graph

Validate correctness using intentionally cyclic code

Highlight cycles visually in Mermaid diagrams

Group nodes by module for architectural clarity

What I Worked On
1. Intentional Cycle Injection

Created a controlled test project (examples/cycle_project) with three modules:

a.func_a → b.func_b → c.func_c → a.func_a


This ensured:

Cycle detection logic could be stress-tested

False negatives would be obvious

2. Cycle Detection Algorithm

Implemented a DFS-based cycle detection algorithm with:

Visited set

Recursion stack

Path tracking for accurate cycle reconstruction

The detector outputs:

Each cycle as an ordered path

Machine-readable JSON (cycles.json)

Example output:

Cycle 1:
a.func_a → b.func_b → c.func_c → a.func_a

3. Cycle-Aware Visualization (Mermaid)

Enhanced graph export to:

Highlight cycle edges in red

Label cycle edges explicitly

Preserve module-level grouping using subgraph

This makes architectural risks instantly visible.

Example Visualization (Conceptual)

Red edges → cyclic dependencies

Subgraphs → modules/domains

Closed loop → refactoring hotspot

This mirrors how professional architecture tools present dependency risks.

Key Learnings

Cycles rarely appear accidentally — they often indicate design issues

Call graph cycles and import graph cycles are related but distinct

Visualization dramatically improves comprehension over raw data

Static analysis is most valuable when paired with clear UX

Engineering Takeaways

AST-based analysis scales beyond simple code inspection

Graph-based representations unlock deeper insights

Even small tools can surface system-level design flaws

Next Steps

Distinguish import-level cycles vs call-level cycles

Rank cycles by severity or depth

Integrate graphs into LLM context pipelines (GraphRAG)

Expand to large real-world codebases

Summary

Day 13 marked the transition from analysis to insight.
The tool now not only extracts structure but also identifies architectural risk and presents it clearly — a core requirement for real-world static analysis systems.



