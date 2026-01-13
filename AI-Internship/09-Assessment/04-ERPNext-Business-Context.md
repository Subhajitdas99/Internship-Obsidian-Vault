# Understanding ERPNext: The Business Context

## Why This Matters

You're building tools for developers who modernize enterprise systems. To build useful tools, you need to understand **what problem the enterprise system solves**.

---

## The Assignment

Before diving deeper into code analysis, spend time actually using ERPNext. This gives you:

1. **Domain Knowledge**: What does a Sales Invoice actually do?
2. **User Perspective**: What workflows do users care about?
3. **Pain Points**: Where would a developer struggle to understand the code?

---

## Getting Started with ERPNext

### Option 1: Online Demo

ERPNext provides a demo instance:
- URL: https://demo.erpnext.com
- Credentials: Usually shown on the page

### Option 2: Local Installation

```bash
# Using Docker (recommended)
docker pull frappe/erpnext
docker run -d -p 8080:8080 frappe/erpnext
```

### Option 3: Frappe Cloud Trial

- Free 14-day trial at https://frappecloud.com

---

## Exploration Tasks

### Task 1: Create a Sales Invoice (30 min)

1. Navigate to: Selling → Sales Invoice
2. Create a new invoice with:
   - Customer (create one if needed)
   - 2-3 line items
   - Apply a discount
3. Submit the invoice
4. Check the GL Entry (Accounting → GL Entry)

**Document**:
- What fields are required?
- What happened when you submitted?
- What other records were created?

### Task 2: Follow the Quote-to-Cash Flow (45 min)

Create this flow end-to-end:

```
Quotation → Sales Order → Delivery Note → Sales Invoice → Payment Entry
```

**Document**:
- How do documents link to each other?
- What happens at each step?
- What validations blocked you?

### Task 3: Explore the Customer Master (20 min)

1. Create a Customer
2. Set credit limit
3. Add payment terms
4. Try to create an invoice exceeding credit limit

**Document**:
- What data does Customer hold?
- How does credit limit enforcement work?
- Where might this logic live in code?

---

## What to Look For

### Business Rules (Hidden in Code)

| Rule | Where You'll See It |
|------|---------------------|
| "Invoice total must equal line items + tax - discount" | Submit validation |
| "Can't deliver more than ordered" | Delivery Note creation |
| "Credit limit check" | Invoice creation for customer |
| "Stock availability check" | Item selection |

### Entity Relationships

```
Customer
├── has many → Quotations
├── has many → Sales Orders
├── has many → Sales Invoices
└── has many → Payment Entries

Sales Invoice
├── belongs to → Customer
├── has many → Items (line items)
├── creates → GL Entry (on submit)
└── creates → Stock Ledger Entry (if applicable)
```

### Workflow States

```
Draft → Submitted → Paid → Cancelled
         ↓
     (GL created)
```

---

## Recording Your Exploration

Create a markdown file documenting your exploration:

```markdown
# ERPNext Exploration Notes

## Date: 2026-01-14

### Sales Invoice Flow

**What I Did:**
- Created Sales Invoice SI-00001
- Added 2 items: Widget A ($100), Widget B ($50)
- Applied 10% discount
- Submitted

**What Happened on Submit:**
- Status changed to "Submitted"
- GL Entry created (saw 3 accounting entries)
- Outstanding amount updated on Customer

**Questions for Code Analysis:**
- Where is the GL Entry creation triggered?
- How is discount calculated?
- What validation runs before submit?

### Discoveries

**Interesting Behavior:**
- Couldn't delete after submit (had to cancel first)
- Cancellation created reverse GL entries

**Would Be Hard to Find in Code:**
- The link between Sales Invoice and GL Entry
- Why certain fields are required
```

---

## Connect Business to Code

After exploration, map what you learned to code questions:

| Business Behavior | Code Question |
|-------------------|---------------|
| Invoice creates GL entries on submit | Where is on_submit hook? What does it call? |
| Discount applies to total | Where is discount calculation? |
| Credit limit blocks invoice | Where is credit limit validation? |
| Cancellation reverses entries | What does cancel() method do? |

Your code analyzer should help answer these questions.

---

## Expected Outcomes

After this exploration:

1. **You can describe** what Sales Invoice does to a non-technical person
2. **You understand** the main entities and relationships
3. **You have questions** that your code analyzer should answer
4. **You can evaluate** whether your tool's output is actually useful

---

## Related

- [[03-Context-Quality-Experiment|Context Quality Experiment]]
- [[../04-Target-Projects/02-ERPNext-Domain-Analysis|ERPNext Domain Analysis]]

---

*Created: 2026-01-13*
