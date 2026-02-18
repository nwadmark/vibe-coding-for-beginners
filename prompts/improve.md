# Prompts for Improving Existing Tools

Use these prompts when your tool works but needs visual polish, better formatting, or a smoother user experience. These prompts modify the look and feel without changing the core logic.

**Important:** Always paste these in the **same conversation** where you generated the original code. The AI needs context about what it already built.

---

## The Golden Rule

Always end improvement prompts with:

```
Keep existing logic. Add these things only.
```

Without this line, the AI may rewrite your entire tool while adding the improvements — and break features that were already working.

---

## Add Visual Score Bars

```
Add a visual bar chart after the results. For each criterion, show:

  [Label]    ████████░░  8/10

Use █ for filled and ░ for empty, 10 characters total.
Pad labels so all bars align in a column.

Keep existing logic. Add this visual only.
```

**When to use:** Any tool that scores items on a numeric scale. Works for Decision Framework, RICE scores, sentiment analysis, and more.

---

## Add Input Labels

```
After each numeric input, show a label:
  1-3: Low
  4-6: Medium
  7-9: High
  10: Maximum

Print the label on the same line as the input, like:
  Customer Value (1-10): 8  → High

Keep existing logic. Add labels only.
```

**When to use:** Any tool that collects 1-10 scores. Gives the user instant feedback that their input was registered and categorized.

---

## Improve Table Formatting

```
Reformat the output table to align all columns.

Use fixed-width formatting so columns line up:
  - Left-align text columns
  - Right-align number columns
  - Pad all columns to the same width

Add a header row with column names.
Add separator lines above and below the header using ━ characters.

Keep existing logic. Change only the table formatting.
```

**When to use:** When your ranked tables or comparison outputs look ragged. Common with RICE calculator, pricing calculator, and comparison mode.

---

## Add Color-Coded Results

```
Make the recommendation output easier to scan:
- For "Strong Go" results, add 🟢 before the line
- For "Maybe" results, add 🟡 before the line
- For "No Go" results, add 🔴 before the line

Also add emoji to these elements:
- Risk warnings: ⚠️
- Action items: 📌 for high priority, 🔍 for investigate, 📁 for archive
- Section headers: use ━━━ separator lines

Keep existing logic. Change only the display formatting.
```

**When to use:** When the output is a wall of text and the user needs to scan for the key result quickly.

---

## Add a Summary Header

```
Add a summary block at the top of the results output:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Feature: [name]
  Score:   [score]
  Result:  [recommendation]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Show this before the detailed breakdown.
Keep existing logic. Add this summary block only.
```

**When to use:** When the tool outputs a lot of detail and the user wants the bottom line at the top.

---

## Format Dollar Amounts

```
Format all dollar amounts with:
- A dollar sign prefix
- Commas for thousands ($16,605)
- Two decimal places for cents when relevant ($4.99)
- Right-align all dollar columns in tables

Keep existing logic. Change only the number formatting.
```

**When to use:** Pricing calculator, revenue models, or any tool that displays financial data.

---

## Add Separators Between Evaluations

```
When the user evaluates multiple items, add a clear visual separator between each one:

─────────────────────────────────

Print this line before each new evaluation (except the first one).
Keep existing logic. Add separators only.
```

**When to use:** Any tool with a repeat loop (Decision Framework, RICE calculator, pricing scenarios). Makes it easy to tell where one evaluation ends and the next begins.

---

## General Improvement Template

Use this when you want to request a custom improvement:

```
The tool works. Now improve the [specific area].

Change these things:
1. [First improvement — be specific about what and how]
2. [Second improvement]
3. [Third improvement]

Keep existing logic. Change only what I listed above.
Do not add any features I did not ask for.
```

**Tips:**
- Limit to 3 improvements per prompt. More than that and the AI starts making trade-offs.
- Always include an example of what the improved output should look like if possible.
- If the AI changes something you did not ask for, say: "You changed [thing]. Revert that and only make the changes I listed."
