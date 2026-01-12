# AI Engineering Internship

## Theme: AI-Driven Legacy Modernization

> *Building intelligent tools that understand enterprise codebases and accelerate migration from legacy systems to modern architectures.*

---

## How to Navigate This Documentation

### Recommended: Obsidian Desktop App

For the best experience navigating this documentation, we recommend using **[Obsidian](https://obsidian.md/)** - a free knowledge base app that works on local Markdown files.

**Why Obsidian?**
- **Graph View**: Visualize connections between documents
- **Quick Navigation**: `Ctrl/Cmd + O` to jump to any document
- **Backlinks**: See which documents reference the current one
- **Local-first**: All files stay on your machine

**Setup**:
1. Download Obsidian from [obsidian.md](https://obsidian.md/)
2. Clone this repository
3. Open the `AI-Internship` folder as a vault in Obsidian

**Alternative**: You can also browse via GitHub web UI - all links work in both environments.

---

## Master Document Index

### Start Here (Orientation)

| # | Document | Description | Read When |
|---|----------|-------------|-----------|
| 1 | **[This Index](./Index.md)** | Overview, theme, tracks | First day |
| 2 | [Organizational Context](./Organizational-Context.md) | Your role in PearlThoughts (Team Topologies) | First day |
| 3 | [Goals & Expectations](./Goals-and-Expectations.md) | 4-week plan, deliverables, success criteria | First day |

### Week 1: Research Phase

| # | Document | Description | Read When |
|---|----------|-------------|-----------|
| 4 | [Existing Tools Research](./Existing-Tools-Research.md) | Commercial & open source tools (GitHub Copilot, Amazon Q, GPT-Migrate) | Week 1 |
| 5 | [Market Analysis](./Market-Analysis.md) | $300B+ market, why consultants still needed | Week 1 |
| 6 | [AI Coding Tools Comparison](./AI-Coding-Tools-Comparison.md) | How Cursor, Aider, OpenCode, Claude Code work internally | Week 1 |

### Week 2-3: Build Phase

| # | Document | Description | Read When |
|---|----------|-------------|-----------|
| 7 | [Technical Architecture](./Technical-Architecture.md) | 4-mode knowledge extraction (text, symbol, runtime, workflow) | Week 2 |
| 8 | [Quality Metrics](./Quality-Metrics.md) | How to measure tool quality (RAGAs, MLflow, test cases) | Week 2-3 |
| 9 | [Validation Projects](./Validation-Projects.md) | Target systems: Bahmni, ERPNext, Odoo | Week 2-4 |

### Progress Tracking

| # | Document | Description | Read When |
|---|----------|-------------|-----------|
| 10 | [OKR](./OKR.md) | Objectives & Key Results by track | Weekly |

---

## Quick Links by Topic

### Understanding the Problem

- [Market Analysis](./Market-Analysis.md) - Why legacy modernization is hard
- [Index](./Index.md#the-problem-were-solving) - Technical debt statistics
- [Organizational Context](./Organizational-Context.md#the-current-reality-cursor-ai-alone) - What's missing in current tools

### Understanding Existing Tools

- [Existing Tools Research](./Existing-Tools-Research.md) - Tool-by-tool breakdown
- [AI Coding Tools Comparison](./AI-Coding-Tools-Comparison.md) - Architecture deep dive
- [Market Analysis](./Market-Analysis.md#what-actually-exists-2025-landscape) - Commercial landscape

### Building Your Solution

- [Technical Architecture](./Technical-Architecture.md) - 4-mode extraction approach
- [Quality Metrics](./Quality-Metrics.md) - Measuring success
- [Goals & Expectations](./Goals-and-Expectations.md#week-2-build-phase) - Week 2 tasks

### Validation & Testing

- [Validation Projects](./Validation-Projects.md) - Bahmni, ERPNext, Odoo details
- [Quality Metrics](./Quality-Metrics.md#building-a-test-suite) - Test case format
- [Goals & Expectations](./Goals-and-Expectations.md#week-4-verify--document-phase) - Verification approach

---

## The Problem We're Solving

Every enterprise faces the same challenge: **legacy systems that are too valuable to abandon but too complex to understand**. These systems contain decades of business logic, evolved over years of real-world usage, embedded in millions of lines of code that no single person fully comprehends.

### The Scale of Technical Debt

- **$300B+ annual market** for legacy modernization ([Market Analysis](./Market-Analysis.md))
- Average enterprise maintains **15+ year old core systems**
- **70% of modernization projects fail** due to lost business logic
- **85% of critical business rules** exist only in code, not documentation

### Why Current Approaches Fail

| Approach | Problem | Learn More |
|----------|---------|------------|
| **Manual Analysis** | Takes years, expensive, experts retire mid-project | [Market Analysis](./Market-Analysis.md#reason-3-undocumented-business-logic) |
| **Big Bang Rewrite** | Loses embedded business logic, high failure rate | [Goals](./Goals-and-Expectations.md#strangler-fig-pattern) |
| **Lift and Shift** | Moves the mess to cloud, doesn't fix technical debt | [Market Analysis](./Market-Analysis.md#reason-1-extreme-context-specificity) |
| **Traditional Tools** | Static analysis only, miss runtime behavior | [Technical Architecture](./Technical-Architecture.md#the-problem-with-single-mode-indexing) |

---

## The AI-Powered Solution

We're building tools that **understand code like an expert developer** - not just syntax, but semantics, relationships, and business intent.

### Beyond Archaeological Indexing

Tools like Cursor, GitHub Copilot, and other AI editors provide basic code exploration with what we call "archaeological indexing" - they index files and symbols, enabling search and autocomplete. But this approach has fundamental limitations. See [AI Coding Tools Comparison](./AI-Coding-Tools-Comparison.md) for detailed analysis.

```
┌────────────────────────────────────────────────────────────────┐
│           CURRENT AI EDITORS (Archaeological Indexing)         │
├────────────────────────────────────────────────────────────────┤
│  ✓ File-level indexing                                         │
│  ✓ Symbol search (functions, classes)                          │
│  ✓ Basic autocomplete                                          │
│  ✗ No semantic understanding                                   │
│  ✗ No cross-file business logic tracking                       │
│  ✗ No runtime behavior awareness                               │
│  ✗ No enterprise context (wikis, tickets, decisions)           │
│  ✗ Cannot answer "why was this built this way?"                │
└────────────────────────────────────────────────────────────────┘
```

### Our Approach: Holistic Enterprise Intelligence

We go beyond simple indexing to build a **complete knowledge model** of the enterprise system. See [Technical Architecture](./Technical-Architecture.md) for implementation details.

```
┌────────────────────────────────────────────────────────────────┐
│           OUR APPROACH (Holistic Enterprise Intelligence)      │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  1. SEMANTIC CHUNKING (Mode 1: Text Chunks)                    │
│     └── Intelligent code splitting at function/class level     │
│     └── Preserves context (imports, docstrings, decorators)    │
│     └── Vector embeddings for semantic search                  │
│                                                                │
│  2. GRAPH EXTRACTION (Mode 2: Symbol Chunks)                   │
│     └── Call graphs (who calls whom)                           │
│     └── Dependency graphs (what depends on what)               │
│     └── Data flow graphs (how data moves through system)       │
│     └── Domain boundaries (implicit bounded contexts)          │
│                                                                │
│  3. AST ANALYSIS (tree-sitter)                                 │
│     └── Deep syntax tree parsing                               │
│     └── Pattern extraction (ORM relations, validations)        │
│     └── Business rule identification                           │
│     └── Framework-specific analysis                            │
│                                                                │
│  4. RUNTIME LOGS (Mode 3: Runtime Traces)                      │
│     └── Production trace analysis                              │
│     └── Hot path identification                                │
│     └── Error pattern clustering                               │
│     └── Performance bottleneck discovery                       │
│                                                                │
│  5. ENTERPRISE CONTEXT (Mode 4: Workflows)                     │
│     └── Wiki/Confluence integration                            │
│     └── Jira/ticket history                                    │
│     └── Git commit archaeology                                 │
│     └── Architecture Decision Records (ADRs)                   │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## What You'll Build

### The Code Synthesizer Tool

A developer tool that augments AI editors by providing deep enterprise codebase understanding. See [Organizational Context](./Organizational-Context.md#the-augmented-reality-with-your-tools) for detailed examples of how this compares to current tools.

```
Developer Query                          System Response
─────────────────────────────────────────────────────────────────
"How does discount                  →    Retrieves:
 calculation work?"                      • DiscountService.calculateDiscounts()
                                         • CustomerTier logic
                                         • Promo code validation
                                         • Related tests
                                         • Git history of changes
                                         • Jira tickets explaining business rules

"What breaks if I change            →    Impact analysis:
 the Order model?"                       • 47 direct callers
                                         • 12 services affected
                                         • 3 API endpoints impacted
                                         • Test coverage: 67%
                                         • Risk assessment: HIGH
```

### Key Capabilities to Implement

| Capability | Description | AI Technique | Learn More |
|------------|-------------|--------------|------------|
| **Semantic Search** | Find code by intent, not just keywords | RAG, Embeddings | [Technical Architecture](./Technical-Architecture.md#mode-1-text-based-chunks) |
| **GraphRAG** | Vector search + graph traversal | Hybrid Retrieval | [Technical Architecture](./Technical-Architecture.md#mode-4-workflowcall-graphs) |
| **Domain Discovery** | Auto-identify bounded contexts | Clustering | [Goals](./Goals-and-Expectations.md#track-c-domain-discovery) |
| **Parity Tracking** | Map legacy→modern coverage | Semantic Similarity | [Goals](./Goals-and-Expectations.md#track-d-migration-automation) |
| **Impact Analysis** | "What breaks if I change X?" | Graph Algorithms | [Organizational Context](./Organizational-Context.md#example-3-impact-analysis-in-odoo) |

---

## Target Systems for Validation

We validate on **real enterprise open-source systems**. See [Validation Projects](./Validation-Projects.md) for detailed breakdowns.

| System | Stack | Domain | Size | Why |
|--------|-------|--------|------|-----|
| **[Bahmni](./Validation-Projects.md#1-bahmni-healthcare)** | Java, Spring | Healthcare | ~500K LOC | Medical domain, compliance |
| **[ERPNext](./Validation-Projects.md#2-erpnext-business-erp)** | Python, Frappe | ERP | ~1M LOC | Full business domain |
| **[Odoo](./Validation-Projects.md#3-odoo-modules-modular-erp)** | Python, PostgreSQL | Modular ERP | ~2M LOC | Bounded contexts |

---

## Internship Tracks

Choose your focus area. See [Goals & Expectations](./Goals-and-Expectations.md) for week-by-week breakdown and [OKR](./OKR.md) for success metrics.

### Track A: Knowledge Extraction
- Build semantic chunking pipeline for Java/Python
- Implement graph extraction (call graphs, dependencies)
- **Validation**: Apply to [Bahmni's clinical module](./Validation-Projects.md#1-bahmni-healthcare)
- **Deep dive**: [Technical Architecture - Symbol Chunks](./Technical-Architecture.md#mode-2-symbol-chunks-ast-based)

### Track B: Intelligent Retrieval
- Build RAG pipeline for code understanding
- Implement GraphRAG (vector + graph hybrid)
- **Validation**: Answer questions about [ERPNext accounting](./Validation-Projects.md#2-erpnext-business-erp)
- **Deep dive**: [Quality Metrics - RAG Quality](./Quality-Metrics.md#category-1-rag-retrieval-quality)

### Track C: Domain Discovery
- Implement clustering for bounded context detection
- Build visualization for domain boundaries
- **Validation**: Auto-discover [Odoo module boundaries](./Validation-Projects.md#3-odoo-modules-modular-erp)
- **Deep dive**: [Technical Architecture - Workflows](./Technical-Architecture.md#mode-4-workflowcall-graphs)

### Track D: Migration Automation
- Build parity tracking system (legacy↔modern mapping)
- Create AI migration agents for code transformation
- **Validation**: Migrate one [Bahmni service](./Validation-Projects.md#1-bahmni-healthcare)
- **Deep dive**: [Goals - Week 3 Migrate Phase](./Goals-and-Expectations.md#week-3-migrate-phase)

---

## Technology Stack

| Layer | Technologies | Learn More |
|-------|--------------|------------|
| **Languages** | TypeScript, Python | |
| **Frameworks** | NestJS, FastAPI | |
| **Embeddings** | Ollama, OpenAI, Sentence Transformers | [Technical Architecture](./Technical-Architecture.md#open-source-libraries-to-use) |
| **Vector Store** | LanceDB, SQLite | [AI Tools Comparison](./AI-Coding-Tools-Comparison.md#from-cursor-embedding-cache) |
| **Graph** | Graphology, SQLite CTEs | [Technical Architecture](./Technical-Architecture.md#mode-4-workflowcall-graphs) |
| **Parsing** | tree-sitter | [Technical Architecture](./Technical-Architecture.md#mode-2-symbol-chunks-ast-based) |
| **LLM** | Claude, GPT-4, Llama, Groq | |

---

## Learning Outcomes

By the end of this internship, you will:

1. **Understand RAG deeply** - Not just tutorials, but production systems ([Quality Metrics](./Quality-Metrics.md))
2. **Work with knowledge graphs** - Graph algorithms for code intelligence ([Technical Architecture](./Technical-Architecture.md))
3. **Build AI agents** - Practical experience with LLM orchestration ([Goals](./Goals-and-Expectations.md#week-3-migrate-phase))
4. **Apply to real systems** - Validate on actual enterprise codebases ([Validation Projects](./Validation-Projects.md))
5. **Contribute to open source** - Your work helps real modernization projects

---

## Getting Started Checklist

| # | Action | Document | Status |
|---|--------|----------|--------|
| 1 | Read this overview completely | [Index](./Index.md) | ☐ |
| 2 | Understand your role in the organization | [Organizational Context](./Organizational-Context.md) | ☐ |
| 3 | Review 4-week goals and expectations | [Goals & Expectations](./Goals-and-Expectations.md) | ☐ |
| 4 | Research existing AI modernization tools | [Existing Tools Research](./Existing-Tools-Research.md) | ☐ |
| 5 | Understand the market landscape | [Market Analysis](./Market-Analysis.md) | ☐ |
| 6 | Study how AI coding tools work | [AI Coding Tools Comparison](./AI-Coding-Tools-Comparison.md) | ☐ |
| 7 | Learn the technical architecture | [Technical Architecture](./Technical-Architecture.md) | ☐ |
| 8 | Understand quality measurement | [Quality Metrics](./Quality-Metrics.md) | ☐ |
| 9 | Review validation projects | [Validation Projects](./Validation-Projects.md) | ☐ |
| 10 | Choose your track (A, B, C, or D) | [OKR](./OKR.md) | ☐ |
| 11 | Set up development environment | See mentor | ☐ |
| 12 | Join #ai-internship Slack channel | | ☐ |

---

## Related Resources

- [Intern Handbook](../Handbook/Index.md)
- [Programme Structure](../Programme-Structure/Index.md)
- [Meet Your Mentors](../Support/Mentors.md)
- [Quick Start Guide](../Resources/Quick-Start.md)

---

## Document Relationships

```
                    ┌─────────────────┐
                    │   Index.md      │ ◄── You are here
                    │   (Overview)    │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Organizational  │ │ Goals &         │ │ Validation      │
│ Context         │ │ Expectations    │ │ Projects        │
│ (Your Role)     │ │ (4-Week Plan)   │ │ (Target Systems)│
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │
         │    ┌──────────────┴──────────────┐    │
         │    │                             │    │
         ▼    ▼                             ▼    ▼
┌─────────────────┐                 ┌─────────────────┐
│ Research Docs   │                 │ Technical Docs  │
│ ├── Existing    │                 │ ├── Technical   │
│ │   Tools       │◄───────────────►│ │   Architecture│
│ ├── Market      │                 │ └── Quality     │
│ │   Analysis    │                 │     Metrics     │
│ └── AI Tools    │                 │                 │
│     Comparison  │                 │                 │
└─────────────────┘                 └─────────────────┘
         │                                   │
         └───────────────┬───────────────────┘
                         │
                         ▼
                 ┌─────────────────┐
                 │     OKR.md      │
                 │ (Track Progress)│
                 └─────────────────┘
```

---

*Last Updated: 2025-01-12*
*Program Lead: Engineering Team*
