# Advanced Prompt Techniques

These patterns give you more precise control over AI-generated code. Use them once you are comfortable with the basics from the [workshop prompts](workshop-prompts.md) and [generate prompts](generate.md).

---

## Technique 1: Constraint Stacking

Add constraints at the end of your prompt to control code quality. Stack as many as you need.

```
[Your main prompt here]

Constraints:
- Use Python built-ins only (no pip install needed)
- Keep it under 80 lines
- Add plain-English comments explaining each section
- Validate all inputs — never crash on bad data
- Use f-strings for all output formatting
- No global variables — pass data through function arguments
```

### Why this works

Each constraint eliminates a category of problems. Without them, the AI makes its own choices — and those choices often create headaches:

| Constraint | What it prevents |
|---|---|
| Python built-ins only | Importing libraries that require `pip install` |
| Line limit | 300-line over-engineered code |
| Plain-English comments | Cryptic code you can't understand later |
| Input validation | Crashes on unexpected user input |
| f-strings | Inconsistent string formatting |
| No global variables | Hard-to-trace bugs when state changes unexpectedly |

**Tip:** You do not need all of these every time. Pick the ones relevant to your tool. The first three (builtins, line limit, comments) are good defaults for every prompt.

---

## Technique 2: Output-First Prompting

Instead of describing what the tool should *do*, show what the output should *look like*. The AI reverse-engineers the code from the example.

```
Build me a Python tool that produces this exact output:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PM DECISION FRAMEWORK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Feature: Add one-click checkout

  Customer Value (1-10): 8
   → High
  Implementation Effort (1-10): 6
   → Medium
  Strategic Alignment (1-10): 7
   → High
  Confidence (1-10): 5
   → Medium

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Feature: Add one-click checkout
  Score:   8.3
  Result:  🟡 Maybe — Needs more validation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The scoring formula is:
Score = (CustomerValue×2 + StrategicAlignment×1.5 + Confidence×1) / Effort × 10

Make the tool produce output that matches this format exactly.
Use Python built-ins only. Keep it under 100 lines.
```

### Why this works

The AI treats the example output as a visual spec. It matches the separators (`━`), spacing, emoji, alignment, and flow. This is more precise than describing the format in words, because the AI can see exactly what you want character by character.

**When to use:** When the output format matters a lot — dashboards, reports, tables, or anything you will paste into Slack or a document.

---

## Technique 3: Incremental Prompting

Build complex tools in stages instead of one giant prompt. Each stage adds one layer.

**Stage 1:** Build the simplest possible version.

```
Build a Python tool that asks for a feature name and 4 scores (1-10 each),
calculates a weighted score, and prints the result. Nothing else.
Use Python built-ins only.
```

**Stage 2:** Add output formatting.

```
The tool works. Now improve the output:
- Add a summary box with the feature name, score, and recommendation
- Add score breakdown showing each criterion's contribution
Keep existing logic. Add formatting only.
```

**Stage 3:** Add visual elements.

```
Add ASCII bar charts showing each score visually.
Add input labels (Low/Medium/High/Maximum).
Keep existing logic. Add these two things only.
```

**Stage 4:** Add an advanced feature.

```
Add comparison mode so I can evaluate multiple features and see a ranked table.
Keep existing logic. Add comparison mode only.
```

### Why this works

Each prompt is small and focused. The AI makes fewer mistakes with bounded scope. If something breaks, you know exactly which stage caused it and can fix that one prompt.

**The trade-off:** More prompts = more round-trips. But each round-trip is safer. For complex tools, this is almost always faster than one massive prompt that produces buggy code.

---

## Technique 4: Negative Constraints

Tell the AI what *not* to do. This prevents common over-engineering patterns.

```
[Your main prompt here]

Do NOT:
- Add features I did not ask for
- Import any external libraries
- Add a graphical interface — keep it command-line
- Use classes or object-oriented patterns — use simple functions
- Add error handling for scenarios that cannot happen
- Add type hints or docstrings
```

### Why this works

AI models tend to add things. Without negative constraints, the AI may:
- Import `colorama` for colored output (breaks in Replit)
- Build a class hierarchy for a 50-line script
- Add elaborate try/except blocks around code that cannot fail
- Include type annotations that clutter the code

Negative constraints are particularly useful when you have seen the AI do something unwanted in a previous attempt.

---

## Technique 5: Role + Context Priming

Add context about your specific situation to get more relevant code.

```
Context:
- I'm a PM at a B2B SaaS company with 3 pricing tiers
- My team uses RICE scoring for prioritization
- We plan in 2-week sprints
- I present feature recommendations at weekly stakeholder meetings

Given this context, build me a [tool description].

The output should be formatted so I can paste it directly into a Slack message
for my stakeholder meeting.
```

### Why this works

The AI tailors variable names, labels, output format, and default values to your context. A tool built for "a B2B SaaS PM who presents at weekly meetings" looks different from one built for "a mobile app PM who writes Jira tickets."

**Tip:** You do not need to include your context every time. Use it in the first prompt of a conversation. The AI remembers it for follow-up prompts.

---

## Technique 6: Diff-Style Change Requests

When you want to change specific lines, point to them precisely.

```
In the calculate_score function, change the formula from:
  (customer * 2 + alignment * 1.5 + confidence * 1) / effort * 10
to:
  (customer * 3 + alignment * 1.5 + confidence * 1) / (effort * 1.2) * 10

In the get_recommendation function, change the thresholds from:
  > 15: Strong Go
  >= 10: Maybe
to:
  > 20: Strong Go
  >= 12: Maybe

Change only these two things. Keep everything else exactly the same.
```

### Why this works

You are pointing to exact locations and exact values. The AI makes surgical changes instead of rewriting surrounding code. This is the safest way to modify logic.

**When to use:** When you know exactly what to change. If you are not sure what to change, use a prompt from [explain.md](explain.md) first to understand the code.

---

## Technique 7: Chaining Prompts Across Tools

Use the output of one tool as the input to another.

```
I have a decision_log.txt file that was generated by my PM Decision Framework tool.
Each entry looks like this:

=====================================
Date: 2024-03-15
Feature: Add one-click checkout
Score: 18.2/20
Decision: Go
─────────────────────────────────────
Customer Value:        8/10
Implementation Effort: 6/10
Strategic Alignment:   7/10
Confidence:            5/10
=====================================

Build a Python tool that:
1. Reads decision_log.txt
2. Parses each entry
3. Shows a summary: how many Go / Maybe / No Go decisions
4. Lists the top 5 features by score
5. Shows average scores for each criterion across all entries

Use Python built-ins only. Keep it under 80 lines.
```

### Why this works

You are building a pipeline: Tool A generates data, Tool B analyzes it. By showing the exact format of Tool A's output, the AI builds Tool B to parse it correctly. This is how you go from individual scripts to a connected workflow.

---

## Pattern Summary

| Technique | Use When |
|---|---|
| Constraint stacking | Every prompt — pick the relevant constraints |
| Output-first | The output format matters a lot |
| Incremental | Building something complex (3+ features) |
| Negative constraints | The AI keeps adding unwanted stuff |
| Role + context | First prompt in a new conversation |
| Diff-style | You know exactly what lines to change |
| Chaining | You want tools to work together |
