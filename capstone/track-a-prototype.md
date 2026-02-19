# Track A — Build an Interactive Prototype

Build an interactive prototype of a real feature you are currently working on or evaluating. Something users can click through and stakeholders can react to.

---

## What You Will Build

An interactive prototype that demonstrates a core user workflow for a feature you care about. It does not need to be production-ready. It needs to be real enough that:

- A user can click through it and give you meaningful feedback
- A stakeholder can see it and understand what you are proposing
- You can test whether the core interaction pattern works

---

## Why This Track

Choose Track A if:

- You need to test a feature concept with users
- You want a clickable demo for a stakeholder meeting
- You are exploring interaction patterns and want to see them working
- You are tired of explaining features with words and want to show them

---

## Success Criteria

Your capstone is done when:

- [ ] It demonstrates the core user workflow (not every edge case — just the main path)
- [ ] A user can interact with it (click, type, navigate — not just read)
- [ ] It looks real enough for meaningful feedback (not pixel-perfect, but not obviously fake)
- [ ] You built it in under 4 hours
- [ ] You can explain what you learned from building it

---

## The Process

### Step 1: Define the Workflow (30 minutes)

Before you write a single prompt, answer these questions on paper or in a doc:

1. **What problem does this feature solve?** One sentence.
2. **Who is the user?** Be specific — "warehouse manager" not "user."
3. **What is the user's goal?** What do they want to accomplish?
4. **What are the key steps?** List 3-5 steps in the workflow.
5. **What does success look like?** What does the user see when the workflow is complete?

**Example — ShopFlow bulk inventory update:**

1. Problem: Warehouse managers waste time updating items one by one.
2. User: Warehouse managers at ShopFlow customers.
3. Goal: Update inventory quantities for multiple items at once.
4. Steps:
   - View inventory list with current quantities
   - Select multiple items using checkboxes
   - Choose action: update quantity, change status, or export
   - Preview changes before applying
   - Confirm and see success message
5. Success: "12 items updated successfully" with a summary of changes.

### Step 2: Choose Your Approach (10 minutes)

Pick the approach that fits your prototype:

| Approach | Best For | Complexity | Tools Needed |
|---|---|---|---|
| **Streamlit app** | Data-heavy interfaces (tables, charts, filters) | Medium | Python + Streamlit |
| **HTML/CSS/JS** | Interaction-heavy interfaces (click, drag, navigate) | Medium | Browser only |
| **Lovable** | Fast polished prototype with backend | Low (but $20/mo) | Lovable account |
| **Command-line** | Logic-heavy tools with minimal UI | Low | Python only |

**For most PM prototypes, Streamlit is the sweet spot.** It handles tables, forms, buttons, and charts out of the box, and you can build a usable prototype in under 2 hours.

### Step 3: Build the Shell (45 minutes)

Use AI to generate the basic structure. Your first prompt should cover:

- The layout (sidebar, main area, sections)
- The data model (what fields, what types)
- The core interaction (the main thing the user does)

**Example prompt for the ShopFlow inventory prototype:**

```
Build me a Streamlit app for bulk inventory management.

The app should show:
1. A sidebar with filter options: status (All, In Stock, Low Stock, Out of Stock) and search by name
2. A main area with a table showing: checkbox, Product Name, SKU, Current Qty, Status
3. Use this sample data (10 items):
   - Mix of in-stock, low-stock, and out-of-stock items
   - Realistic product names for an e-commerce platform
4. Above the table: show count of selected items and a "Bulk Update" button
5. When Bulk Update is clicked: show a form to set new quantity or status
6. After update: show a success message with count of items changed

Use streamlit and pandas. Add comments explaining each section.
```

Run it. Verify the basic layout works. Do not worry about polish yet.

### Step 4: Add Realistic Content (60 minutes)

Replace placeholder content with content that makes the prototype feel real:

- Use real product names from your domain (or realistic fakes)
- Add realistic data volumes (if your real dataset has 500 items, show at least 20-30)
- Match the labels and terminology your users actually use
- Add the small details: timestamps, status badges, counts

**Follow-up prompt:**

```
Update the sample data:
- 25 products with realistic e-commerce names (electronics, clothing, accessories)
- SKUs in format "SF-XXXX" (4 digit numbers)
- Quantities ranging from 0 to 500
- 4 out of stock, 6 low stock (qty < 20), 15 in stock
- Add a "Last Updated" column with dates in the past 30 days

Keep existing layout and functionality.
```

### Step 5: Test and Refine (45 minutes)

Walk through the prototype yourself:

1. Follow the exact workflow you defined in Step 1
2. Note every place where it feels wrong, confusing, or incomplete
3. Fix the top 2-3 issues with targeted prompts
4. Try one unexpected action (wrong input, empty selection, etc.)

**Common refinements:**
- "Add a confirmation dialog before applying bulk updates"
- "Show a preview of what will change before the user confirms"
- "Add an undo last action button"

---

## ShopFlow Example Project

Alex, PM at ShopFlow, wanted to test whether warehouse managers would prefer a bulk-action interface over the current one-by-one editing.

**Workflow defined:**
1. Select multiple items from inventory list
2. Choose action (update quantity, change status, export)
3. Preview changes
4. Confirm and see result

**Built using:** Streamlit (data-heavy prototype with tables and forms)

**Time taken:** 3 hours (30 min planning, 45 min shell, 60 min content, 45 min refinement)

**Prompt used for the shell:**
```
Build me a Streamlit app for inventory management. Show a table of 20 products with columns: checkbox, name, SKU, quantity, status, last updated. Add a sidebar with status filter and search. Add a "Bulk Actions" section that appears when items are selected: update quantity, change status, or export selected. Show a preview before applying changes. Use streamlit and pandas.
```

**What Alex learned:**
- Users wanted a "preview" step before confirming — the first version applied changes immediately and that felt unsafe
- The search filter was used more than the status filter — Alex moved search to a more prominent position
- 3 out of 5 test users asked for an "undo" feature — added to the real feature spec

---

## Your Turn

Fill in this worksheet before you start building:

```
Feature name: _______________________________
Problem it solves: __________________________
Target user: ________________________________
User's goal: ________________________________

Key workflow (3-5 steps):
1. ________________________________________
2. ________________________________________
3. ________________________________________
4. ________________________________________
5. ________________________________________

Approach: [ ] Streamlit  [ ] HTML/CSS/JS  [ ] Lovable  [ ] CLI

What would make this prototype successful?
_____________________________________________
```

---

## Prompts to Get Started

### Dashboard / Analytics Prototype

```
Build me a Streamlit dashboard for [your domain].

Show:
1. 4 metric cards at the top: [metric 1], [metric 2], [metric 3], [metric 4]
   Each with current value and week-over-week change
2. A line chart showing [key metric] over the past 30 days
3. A data table below with [columns relevant to your data]
4. A sidebar with date range filter and [relevant filter]

Use sample data with realistic values for a [your industry] company.
Use streamlit, pandas, and plotly.
```

### Form / Input Flow Prototype

```
Build me a Streamlit app for [workflow name].

The flow:
1. Step 1: User enters [input fields for step 1]
2. Step 2: User selects [options for step 2]
3. Step 3: App calculates/processes [what happens with the data]
4. Step 4: Show results with [output format]

Add a progress indicator showing which step the user is on.
Use sample data where relevant.
Use streamlit.
```

### Settings / Configuration Prototype

```
Build me a Streamlit app for [feature] settings.

The interface should show:
1. A sidebar with setting categories: [category 1], [category 2], [category 3]
2. Each category shows relevant settings as form controls:
   - Toggles for on/off settings
   - Dropdowns for multi-option settings
   - Text inputs for custom values
   - Sliders for numeric ranges
3. A "Save Changes" button that shows a summary of what changed
4. A "Reset to Defaults" button

Pre-populate with realistic default values for a [your product type].
Use streamlit.
```
