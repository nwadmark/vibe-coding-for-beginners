# Decision Framework Tool — Prompts

These are the three prompts from the workshop. Each one builds on the last. Use them in order in the same AI conversation.

---

## Prompt #1: The Foundation

This prompt builds the complete base tool from scratch.

```
I'm a product manager. I want to build a simple command-line PM Decision Framework Tool in Python.

The tool should:
1. Ask me to describe a feature idea (one sentence)
2. Score the feature on 4 criteria (1-10 scale each):
   - Customer Value: How much will customers benefit?
   - Implementation Effort: How hard to build? (10 = very hard)
   - Strategic Alignment: Does it fit our strategy?
   - Confidence: How sure are we of our assumptions?
3. Calculate a weighted decision score:
   Score = (CustomerValue×2 + StrategicAlignment×1.5 + Confidence×1) / Effort × 10
4. Output a recommendation:
   Score > 15: 🟢 Strong Go — Prioritize this
   Score 10-15: 🟡 Maybe — Needs more validation
   Score < 10: 🔴 No Go — Deprioritize or kill
5. Show a score breakdown per criterion
6. Add a risk flag if effort > 7:
   ⚠️ High effort — validate with engineering first
7. Show a suggested PM action:
   Strong Go → 📌 Add to next sprint backlog
   Maybe → 🔍 Schedule discovery session
   No Go → 📁 Document reasoning and archive
8. Ask if they want to evaluate another feature

Use Python built-ins only (no pip install needed).
Add plain-English comments explaining each section.
Keep it under 120 lines.
```

### Why this prompt works

- **"I'm a product manager"** sets the context so the AI writes for a PM audience, not a developer one.
- **Numbered requirements** prevent the AI from skipping features. Each number becomes a testable acceptance criterion.
- **The exact formula** removes ambiguity. Without it, the AI would invent its own weighting.
- **Emoji in the output spec** tells the AI exactly what the output should look like.
- **"Python built-ins only"** prevents the AI from importing libraries that would require setup.
- **"Plain-English comments"** means the code explains itself, which helps when you revisit it later.

### What you could change

- Replace the four criteria with whatever your team uses for prioritization.
- Adjust the formula weights to reflect your priorities (e.g., make Revenue count triple).
- Change the recommendation thresholds if your team runs more or fewer experiments.

---

## Prompt #2: The Improvement

This prompt adds visual polish without changing the core logic. Paste it in the **same conversation** as Prompt #1.

```
The tool works! Now improve it.

Add these features:
1. After each score input, show a brief label:
   1-3: Low, 4-6: Medium, 7-9: High, 10: Maximum
2. After the recommendation, show a simple visual:
   Customer Value    ████████░░  8/10
   Effort (impact)   ██████░░░░  6/10
   Strategic Align   ███████░░░  7/10
   Confidence        █████░░░░░  5/10
   Use █ for filled, ░ for empty, 10 chars total
3. Add a separator line between evaluations

Keep existing logic. Add these three things only.
```

### Why this prompt works

- **"The tool works!"** tells the AI not to rewrite everything — just add to what exists.
- **Three specific additions** gives a clear, bounded scope. The AI won't over-engineer.
- **"Keep existing logic"** is the most important line. Without it, the AI might refactor the scoring formula or change the recommendations.
- **The exact bar format** with `█` and `░` removes guesswork about what the visual should look like.

### What you could change

- Use different Unicode characters for the bars (e.g., `▓` and `░`, or `■` and `□`).
- Add color labels to the bars (e.g., print "Low" in a different style for scores under 4).
- Change the label ranges to match your team's vocabulary (e.g., "Critical" instead of "Maximum").

---

## Prompt #3 Options

Pick **one** of these three. Each adds a different capability.

### Option A: Decision Log

Saves every evaluation to a file so you can review past decisions.

```
Add a decision log feature.

After each evaluation, append results to decision_log.txt in this format:

=====================================
Date: [YYYY-MM-DD]
Feature: [feature name]
Score: [score]/20
Decision: [Go/Maybe/No Go]
─────────────────────────────────────
Customer Value:        [x]/10
Implementation Effort: [x]/10
Strategic Alignment:   [x]/10
Confidence:            [x]/10
=====================================

Tell the user: ✅ Saved to decision_log.txt
At program start, if log exists, show:
📋 You have [N] previous evaluations. View? (yes/no)
```

**Why this works:** The exact file format means you can paste log entries into tickets or documents. The "view previous" feature makes the tool useful across multiple sessions.

**What you could change:** Switch from a text file to CSV format for easier import into spreadsheets. Or add a date range filter to the view feature.

### Option B: Comparison Mode

Evaluate multiple features and rank them side by side.

```
Add a comparison mode.

At the start ask:
'Evaluate single feature or compare? (single/compare)'

If compare:
- Evaluate features one by one
- Ask 'Add another? (yes/no)' after each
- At the end show a ranked comparison table:

FEATURE COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Rank  Feature            Score  Decision
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 1.   [feature]          [18.2] 🟢 Strong Go
 2.   [feature]          [12.5] 🟡 Maybe
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 Top recommendation: [feature name]

If single: use existing flow.
```

**Why this works:** The table format gives you a prioritization artifact you can bring to sprint planning. The "top recommendation" line makes the output immediately actionable.

**What you could change:** Add a "bottom 3" section for features to explicitly deprioritize. Or export the comparison table to a CSV file.

### Option C: Custom Criteria

Replace the default scoring criteria with your team's priorities.

```
Replace the 4 scoring criteria with my team's criteria:
1. User Impact: How many users affected? (1-10)
2. Revenue Potential: Does this drive revenue? (1-10)
3. Build Effort: Engineering complexity (1-10, higher = harder)
4. Strategic Fit: Fits 2025 roadmap? (1-10)

New formula:
Score = (UserImpact×2 + RevenuePotential×2 + StrategicFit) / BuildEffort × 8

Keep the same output format and thresholds.
```

**Why this works:** It shows that the framework is a template, not a fixed tool. Changing the criteria and formula takes one prompt.

**What you could change:** Add a fifth criterion. Change the weights to match a specific OKR. Adjust the scaling factor (×8) to shift where the thresholds land.

---

## Mix and Match

Once you've completed the three loops, you can combine elements from different prompts. Here are three combinations that work well:

**Decision Log + Comparison Mode:** After running a comparison, save the entire ranked table to the log file. Use this prompt:

```
Combine the decision log and comparison mode. When I run a comparison, save the full ranked table to decision_log.txt with a timestamp. When I view previous logs, show comparison results as tables.
```

**Custom Criteria + Comparison Mode:** Use your team's custom criteria to compare features. No special prompt needed — just apply Option C first, then Option B. The comparison will use whatever criteria are active.

**All Three Together:** Apply all three options in sequence (A, then B, then C) in the same AI conversation. The AI will integrate them. If anything breaks, tell it: "The comparison mode should use the custom criteria and save results to the log."
