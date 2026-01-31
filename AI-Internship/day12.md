Objective for Day 12

Detect module dependencies using static analysis

Build an import graph alongside the call graph

Accurately resolve cross-module function calls

Separate module-level structure from function-level behavior

What I Worked On
1. Import Graph Extraction

Added logic to statically detect Python imports:

import module

import module as alias

from module import name

from module import name as alias

Built a module → module dependency graph

Stored dependencies using normalized module names

Result:

invoice -> ['tax']
tax -> []


This represents true module coupling inside the codebase.

2. Cross-Module Call Resolution

Extended call graph logic to:

Resolve function calls across modules

Map calls like tax.calculate_tax() correctly

Distinguished between:

Internal calls (same module)

Cross-module calls (different modules)

Example Output:

invoice.Invoice.validate
  └── tax.calculate_tax

3. Unified Multi-File Analysis

Analyzer now accepts:

A single Python file

A directory containing multiple Python files

Recursively scans directories using Path.rglob("*.py")

Merges per-file results into:

One global call graph

One global import graph

4. Graph Persistence

Persisted analysis output to call_graph.json

Stored structured data instead of plain text output

Prepared data format suitable for:

Visualization

Future Graph-based RAG systems

Code intelligence tooling

Sample Output
Call Graph
invoice.Invoice.validate
  └── tax.calculate_tax
tax.calculate_tax

Import Graph
invoice -> ['tax']
tax -> []

Key Learnings

AST can reveal architectural dependencies, not just syntax

Import graphs represent system boundaries

Call graphs explain behavior flow

Combining both enables:

Impact analysis

Dependency reasoning

Modernization planning

Static analysis scales across files without executing code

Limitations Identified

External library calls are not yet classified

Alias resolution is basic (advanced name binding not handled)

No visualization layer yet (graph rendered as text only)

No cycle detection or dependency ranking

Next Steps

Classify calls as:

Internal

Cross-module

External

Add visualization using Mermaid or Graphviz

Improve import alias resolution

Prepare data structures for GraphRAG / LLM context injection

Summary

Day 12 marked the transition from file-level analysis to system-level static understanding.
The analyzer now captures both behavior (call graph) and architecture (import graph) — a foundational capability of modern code intelligence platforms.