🧠 Mini Code Analyzer

AST-based Static Code Intelligence Tool (Python)

A minimal yet powerful static analysis engine built using Python’s ast module to understand code structure, dependencies, and execution flow — without executing the code.

This project focuses on learning how real-world code intelligence tools (used in AI assistants, refactoring engines, and GraphRAG systems) work internally.

🚀 Why This Project Exists

Modern AI and developer tools cannot rely on raw source code text alone.
They require structured semantic understanding, such as:

Which functions call which?

How modules depend on each other?

Where are architectural risks like cyclic dependencies?

How can this structure be fed into LLMs reliably?

This project answers those questions using pure static analysis.

✨ Key Capabilities
1️⃣ Call Graph Extraction

Detects:

Top-level functions

Class methods

Cross-module calls

Outputs fully-qualified call paths, e.g.:

module.Class.method → module.function

2️⃣ Import Dependency Graph

Tracks:

import x

from x import y

Builds a module dependency graph

Helps identify tight coupling and architectural boundaries

3️⃣ Multi-File Analysis

Analyze:

A single Python file

An entire directory (recursively)

Merges all results into one global graph

Designed to mirror real enterprise codebases

4️⃣ Cycle Detection (Architecture Risk)

Detects cyclic dependencies using DFS graph traversal

Outputs:

Human-readable cycle paths

Machine-readable cycles.json

Example:

a.func_a → b.func_b → c.func_c → a.func_a

5️⃣ Visual Graph Export (Mermaid)

Generates:

call_graph.mmd

import_graph.mmd

Features:

Module grouping

Red-highlighted cycle edges

Clear directional flow

Renders cleanly in:

GitHub

Mermaid Live

Documentation systems

🧩 Architecture Overview (Pipeline)

Parse Python files into ASTs

Extract function calls and imports

Normalize nodes into fully-qualified names

Merge results across files

Detect cycles via graph traversal

Export JSON for machines and Mermaid for humans

This mirrors how code intelligence platforms structure their pipelines.

📂 Project Structure
mini-code-analyzer/
├── analyzer.py          # AST analyzer (calls + imports)
├── cycle_detector.py    # Cycle detection engine
├── graph_exporter.py    # Mermaid graph generator
├── call_graph.json      # Structured graph output
├── diagrams/
│   ├── call_graph.mmd
│   └── import_graph.mmd
├── examples/
│   ├── multi_file_project/
│   └── cycle_project/
└── README.md

▶️ How to Run
Step 1: Analyze Code
python analyzer.py examples/multi_file_project


Generates:

call_graph.json

Step 2: Detect Cycles
python cycle_detector.py


Outputs:

Console cycle report

cycles.json

Step 3: Generate Diagrams
python graph_exporter.py


Creates:

diagrams/call_graph.mmd

diagrams/import_graph.mmd

🧪 Example Output
Call Graph (JSON)
{
  "a.func_a": ["b.func_b"],
  "b.func_b": ["c.func_c"],
  "c.func_c": ["a.func_a"]
}

Import Graph
{
  "a": ["b"],
  "b": ["c"],
  "c": ["a"]
}

🔁 Cyclic Dependency Example

Cyclic dependencies are a major architectural risk in large systems.
The analyzer detects and visually highlights them.

graph TD
  subgraph a
    "a.func_a"
  end
  subgraph b
    "b.func_b"
  end
  subgraph c
    "c.func_c"
  end

  "a.func_a" -->|cycle| "b.func_b":::cycleEdge
  "b.func_b" -->|cycle| "c.func_c":::cycleEdge
  "c.func_c" -->|cycle| "a.func_a":::cycleEdge

  classDef cycleEdge stroke:red,stroke-width:3px;

🧠 How This Fits AI / GraphRAG Systems

This project produces structured, machine-readable code context, which can be directly fed into:

GraphRAG pipelines

LLM-based code assistants

Refactoring engines

Legacy modernization tools

Instead of raw text, an LLM receives:

Execution paths

Dependency boundaries

Risk hotspots (cycles)

This significantly improves reasoning quality and reliability.

⚠️ Known Limitations (Intentional)

Static analysis only (no runtime resolution)

No dynamic dispatch inference

No type inference (yet)

These trade-offs keep the learning surface focused and explicit.

🔮 Future Enhancements

Severity ranking of cycles

Cross-repository analysis

Graph embeddings for LLM retrieval

CI integration for architecture checks

🎯 What This Project Demonstrates

Deep understanding of Python AST

Graph theory applied to real systems

Static analysis fundamentals

Tooling and platform mindset

Readiness for AI / platform engineering roles

📌 Author

Subhajit Das
AI / ML Engineer (in training)
Focus: Code Intelligence, AI Tooling, Graph-based Systems
