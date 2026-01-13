# Tool Capability Framework

## Overview

This document defines what a complete modernization accelerator tool should do, organized by capability area. Use this as a reference for understanding the full scope and for self-assessing progress.

---

## Capability 1: Business Value

### What This Means

The tool solves a real problem that developers face when modernizing enterprise systems.

### Target Capabilities

| Capability | Description | Example |
|------------|-------------|---------|
| **Workflow Tracing** | Trace what happens when a user action occurs | "What happens when Sales Invoice is submitted?" → Shows GL entry creation, stock updates, notifications |
| **Business Rule Extraction** | Identify validation and business logic | "Patient must have at least one identifier before registration" |
| **Domain Mapping** | Map code to business domains | Sales Invoice belongs to Accounts domain, relates to Inventory and CRM |
| **Impact Analysis** | Show what's affected by a change | Changing discount calculation affects: POS, Sales Invoice, Quotation |

### Questions the Tool Should Answer

- "What happens when a user does X?"
- "Where is Y calculated/validated?"
- "What depends on Z?"
- "What business rules exist for this entity?"

### Evidence of Capability

- Tool generates workflow diagrams for real ERPNext/Bahmni actions
- Extracted business rules match what the application actually enforces
- A developer unfamiliar with the codebase can understand the flow using tool output

---

## Capability 2: AI Engineering

### What This Means

The tool integrates with AI assistants to improve their understanding of legacy codebases.

### Target Capabilities

| Capability | Description | Example |
|------------|-------------|---------|
| **Context Generation** | Produce context optimized for LLM consumption | JSON/markdown with relevant code, relationships, and business rules |
| **Query-Aware Retrieval** | Return context relevant to specific questions | Query "discount calculation" → Returns DiscountController, PricingRule, not all files |
| **MCP Integration** | Expose capabilities as MCP tools | Claude Code can call `search_code`, `trace_workflow`, `get_entity_context` |
| **Prompt Engineering** | Structure context for effective LLM use | System prompts, few-shot examples, context ordering |

### Integration Patterns

```
┌─────────────────────────────────────────────────────────────┐
│  AI ENGINEERING INTEGRATION                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Pattern A: Context Injection                               │
│  ├── Generate context offline (indexing)                    │
│  ├── Retrieve relevant context per query                    │
│  └── Inject into LLM prompt                                 │
│                                                             │
│  Pattern B: MCP Server                                      │
│  ├── Expose tools via Model Context Protocol                │
│  ├── AI assistant decides when to call tools                │
│  └── Returns structured responses                           │
│                                                             │
│  Pattern C: Agentic Workflow                                │
│  ├── AI orchestrates multiple tool calls                    │
│  ├── Iterative refinement of context                        │
│  └── Self-correcting based on results                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Evidence of Capability

- Claude Code gives more accurate answers with tool-generated context than without
- MCP server responds to tool calls within acceptable latency (<500ms)
- Context fits within LLM token limits while including relevant information

---

## Capability 3: LLM Observability

### What This Means

Track and measure how the tool affects LLM performance for systematic improvement.

### Target Capabilities

| Capability | Description | Example |
|------------|-------------|---------|
| **Experiment Tracking** | Compare different approaches systematically | "bge-large embeddings improved recall by 15% over all-minilm" |
| **Response Quality Logging** | Record LLM inputs, outputs, and quality ratings | Store queries, context provided, responses, human ratings |
| **Context Attribution** | Identify which context contributed to good/bad answers | "Call graph context helped, entity list didn't" |
| **Drift Detection** | Notice when quality degrades | "Answers about Inventory module got worse after reindexing" |

### Metrics to Track

| Metric | What It Measures | Target |
|--------|------------------|--------|
| **Context Precision** | % of provided context that was relevant | > 75% |
| **Answer Accuracy** | % of factually correct statements | > 80% |
| **Answer Completeness** | % of relevant information included | > 70% |
| **Retrieval Recall** | % of relevant files/functions found | > 80% |
| **Latency (p95)** | Time to retrieve context | < 500ms |

### Experiment Structure

```yaml
# experiment.yaml
experiment_id: "exp-003"
date: "2026-01-15"
parameters:
  embedding_model: "bge-large-v1.5"
  chunk_size: 1500
  retrieval_strategy: "hybrid"

results:
  precision: 0.82
  recall: 0.78
  avg_answer_accuracy: 0.85

comparison:
  vs_baseline: "+18% accuracy"
  vs_exp_002: "+5% recall"
```

### Evidence of Capability

- Experiment logs show systematic comparison of approaches
- Quality metrics tracked over time
- Clear documentation of what parameters affect what outcomes

---

## Capability 4: Context Quality

### What This Means

The context generated by the tool actually helps AI assistants give better answers.

### Target Capabilities

| Capability | Description | Example |
|------------|-------------|---------|
| **Relevance** | Context matches the query intent | Query about "discount" returns discount-related code, not all code |
| **Completeness** | Context includes all necessary information | Includes the function AND what calls it AND what it calls |
| **Accuracy** | Context correctly represents the code | Relationships shown actually exist in the code |
| **Conciseness** | Context doesn't include unnecessary information | Excludes test files, generated code, deprecated functions |

### Context Quality Dimensions

```
┌─────────────────────────────────────────────────────────────┐
│  CONTEXT QUALITY DIMENSIONS                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  STRUCTURAL                                                 │
│  ├── Entities extracted correctly                           │
│  ├── Relationships mapped accurately                        │
│  └── Hierarchy preserved (module → class → method)          │
│                                                             │
│  SEMANTIC                                                   │
│  ├── Business meaning captured                              │
│  ├── Intent of code understood                              │
│  └── Domain concepts identified                             │
│                                                             │
│  TEMPORAL                                                   │
│  ├── Execution order clear                                  │
│  ├── Workflow steps sequenced                               │
│  └── Event triggers mapped                                  │
│                                                             │
│  PRAGMATIC                                                  │
│  ├── Helps answer actual questions                          │
│  ├── Reduces developer investigation time                   │
│  └── Enables confident code changes                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Validation Protocol

1. **Baseline**: Ask AI about codebase without any context
2. **With Context**: Provide tool-generated context, ask same question
3. **Evaluation**: Rate both answers for accuracy and completeness
4. **Attribution**: Identify what context helped, what was missing

### Evidence of Capability

- Documented experiments showing improvement with context
- Specific examples of questions answered better with context
- Identification of gaps (what context is still missing)

---

## Capability Maturity Levels

### Level 1: Extraction

- Parses code files
- Extracts functions, classes, imports
- Outputs JSON

### Level 2: Relationships

- Maps call relationships
- Identifies entity connections
- Generates dependency graphs

### Level 3: Semantics

- Extracts business rules
- Identifies workflows
- Maps to domain concepts

### Level 4: AI Integration

- Generates LLM-ready context
- Exposes via MCP
- Retrieves query-relevant context

### Level 5: Validated

- Context quality measured
- Experiments tracked
- Continuous improvement

---

## Self-Assessment Questions

Use these to evaluate your current progress:

### Business Value
- [ ] Can your tool answer "what happens when X is submitted?"
- [ ] Does it extract business rules, not just code structure?
- [ ] Have you tested it on the actual target codebase?

### AI Engineering
- [ ] Is your output structured for LLM consumption?
- [ ] Can an AI assistant use your output to answer questions?
- [ ] Have you considered MCP integration?

### LLM Observability
- [ ] Are you tracking what approaches work better?
- [ ] Can you compare different configurations?
- [ ] Do you know which context types help most?

### Context Quality
- [ ] Have you tested if your context improves AI answers?
- [ ] Do you know what's still missing from your context?
- [ ] Can you measure relevance and completeness?

---

## Related

- [[01-Submission-Review-2026-01|Submission Review]]
- [[03-Context-Quality-Experiment|Context Quality Experiment Guide]]
- [[../07-Technical-Architecture/02-Quality-Metrics|Quality Metrics]]
- [[../06-Code-Intelligence/01-What-Is-Code-Intelligence|What Is Code Intelligence]]

---

*Last Updated: 2026-01-13*
