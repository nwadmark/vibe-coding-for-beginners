# Decision Framework Tool

A command-line tool that scores feature ideas on four weighted criteria and tells you whether to prioritize, investigate, or kill them. You describe a feature, rate it on Customer Value, Implementation Effort, Strategic Alignment, and Confidence, and the tool calculates a decision score with a clear recommendation.

## Why It's Useful for PMs

- **Turns gut feelings into structured decisions.** Instead of debating features in meetings, you have a repeatable scoring framework that makes trade-offs visible.
- **Takes 15 seconds per feature.** Quick enough to use during sprint planning, roadmap reviews, or when someone pitches a new idea in Slack.
- **Creates a paper trail.** Every evaluation produces a score breakdown you can paste into a ticket or share with stakeholders to explain your reasoning.

## Sample Interaction

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PM DECISION FRAMEWORK
  Evaluate feature ideas with a weighted scorecard
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Describe the feature idea: Bulk inventory import via CSV

  Customer Value (1-10): 9
   → High
  Implementation Effort (1-10): 6
   → Medium
  Strategic Alignment (1-10): 8
   → High
  Confidence (1-10): 7
   → High

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Feature: Bulk inventory import via CSV
  Score:   61.7
  Result:  🟢 Strong Go — Prioritize this
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Score Breakdown:
    Customer Value × 2    = 18
    Strategic Align × 1.5 = 12.0
    Confidence × 1        = 7
    ÷ Effort (6)         = 61.7

  Customer Value     █████████░  9/10
  Effort (impact)    ██████░░░░  6/10
  Strategic Align    ████████░░  8/10
  Confidence         ███████░░░  7/10

  📌 Suggested action: Add to next sprint backlog
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Evaluate another feature? (yes/no): no

Done. Use your evaluations to drive the next planning session.
```

## How to Run It

### In Replit

1. Open the `replit/` folder in your Repl
2. Make sure `main.py` is the active file
3. Click the green **Run** button
4. Type your answers in the **Console** panel on the right

### In Cursor

1. Open the `cursor/` folder
2. Open the terminal (Ctrl+` or Cmd+`)
3. Run: `python main.py`
4. Type your answers directly in the terminal

## How to Customize It

1. **Change the scoring weights.** In the `calculate_score` function, adjust the multipliers. If your team cares more about revenue than user impact, increase that weight and decrease another.

2. **Add or replace criteria.** Swap out "Confidence" for "Revenue Potential" or "Technical Risk." Update the `get_score` calls and the formula to match.

3. **Adjust the recommendation thresholds.** In `get_recommendation`, change the cutoff values (currently 15 and 10) to match how decisive your team wants to be. Lower thresholds mean more green lights.

## What the Code Is Doing

The tool has four main parts:

**Input collection** — The `get_score` function asks for each criterion and validates that the input is a number between 1 and 10. It shows a label (Low/Medium/High/Maximum) after each entry so you get instant feedback.

**Score calculation** — The `calculate_score` function applies the weighted formula: Customer Value counts double, Strategic Alignment gets 1.5x, Confidence is 1x, and the total is divided by Effort then scaled by 10. This means high-effort features need proportionally higher value scores to get a green light.

**Recommendation engine** — The `get_recommendation` function maps the numeric score to one of three buckets (Strong Go, Maybe, No Go) and pairs each with a concrete PM action step.

**Display** — The main loop ties it all together: it prints a score breakdown showing how each criterion contributed, an ASCII bar chart for visual comparison, a risk flag if effort is high, and the recommended next action. Then it asks if you want to evaluate another feature.

## Prompts

See [prompts.md](prompts.md) for the three workshop prompts used to build and extend this tool.
