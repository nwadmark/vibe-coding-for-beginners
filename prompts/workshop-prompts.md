# Workshop Prompts

These are the exact prompts used in the live workshop. Each one builds on the last. Use them in order in the **same AI conversation** so the AI retains context.

For the full workshop walkthrough, see the [Participant Guide](../workshop/participant-guide.md).

---

## Prompt #1: Foundation

This prompt builds the complete base Decision Framework tool from scratch.

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

### Why This Works

- **"I'm a product manager"** sets the role context. The AI writes code suited for a PM audience — plain-English variable names, clear output labels, no jargon. Without this, you might get developer-oriented code with terse variable names.
- **Numbered requirements are the backbone.** Each number becomes a testable acceptance criterion. The AI treats numbered lists as a checklist and is less likely to skip items.
- **The exact formula removes ambiguity.** Without `Score = (CustomerValue×2 + StrategicAlignment×1.5 + Confidence×1) / Effort × 10`, the AI would invent its own weighting system. Explicit math means you control the logic.
- **Emoji in the output spec** tells the AI exactly what the visual output should look like. If you include the emoji, the AI reproduces them. If you omit them, the AI may use plain text or invent its own symbols.
- **"Python built-ins only"** is a critical constraint. Without it, the AI might import pandas, numpy, or other libraries that require `pip install` — which would break in a fresh Replit environment.
- **"Plain-English comments"** means the code explains itself. This matters when you revisit the code a week later and need to understand what each section does.
- **"Keep it under 120 lines"** prevents the AI from over-engineering. Without a line limit, you might get 300 lines of code with features you did not ask for.
- If you remove the formula, the AI will guess a weighting scheme — and it will be different every time. If you remove the line limit, the code balloons. If you remove "Python built-ins only," you get dependency headaches. Every line in this prompt earns its place.

---

## Prompt #2: Improvement

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

### Why This Works

- **"The tool works!"** signals continuation. It tells the AI not to start over — just modify what exists. Without this, the AI might rewrite everything from scratch and drop features from Prompt #1.
- **Three specific additions** create a bounded scope. The AI knows exactly what to add and what not to touch. Vague prompts like "make it better" lead to unpredictable rewrites.
- **"Keep existing logic. Add these three things only."** is the guardrail. This is the most important line in the prompt. It prevents the AI from refactoring the scoring formula, changing thresholds, or reorganizing the code structure.
- **The exact bar format with `█` and `░`** removes guesswork. Without the visual example, the AI might use `#` and `-`, or `[====    ]`, or something else entirely. Showing the exact characters you want means you get exactly those characters.
- If you remove "Keep existing logic," the AI may restructure the code and accidentally break the scoring. If you remove the bar format example, you get whatever bar style the AI defaults to. If you list more than 3-4 additions in a single prompt, the AI starts making trade-offs about what to include.

---

## Prompt #3A: Decision Log

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

### Why This Works

- **The exact file format** means you can paste log entries directly into tickets, Slack messages, or documents. The AI reproduces the format character-for-character.
- **"Append results"** tells the AI to add to the file, not overwrite it. This is a subtle but critical distinction — without it, each evaluation might erase previous ones.
- **The startup check** ("if log exists, show count") makes the tool useful across sessions. It turns a one-time script into a persistent workflow tool.
- If you remove the format block, the AI will invent its own log format — probably JSON or a comma-separated dump. If you remove "append," the AI might use write mode (`w`) instead of append mode (`a`), destroying previous entries.

---

## Prompt #3B: Comparison Mode

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

### Why This Works

- **Two clear modes** (single vs compare) with an explicit prompt at startup. The AI knows to branch the logic without breaking the existing single-evaluation flow.
- **The exact table format** with column headers and `━` separators means the output is immediately readable. Without the example, the AI might dump results as a plain list.
- **"If single: use existing flow"** protects the original functionality. The comparison mode is additive, not a replacement.
- **"🏆 Top recommendation"** gives the output a clear conclusion. Without it, the AI might show the table and stop, leaving the PM to scan for the winner.
- If you remove the table example, the AI will format comparisons however it wants — probably less readable. If you remove "If single: use existing flow," the AI might replace the original mode entirely.

---

## Prompt #3C: Custom Criteria

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

### Why This Works

- **"Replace the 4 scoring criteria"** is an explicit instruction to swap, not add. The AI removes the old criteria and inserts the new ones.
- **Each criterion has a description** ("How many users affected?") that the AI uses as the input prompt. Without descriptions, the AI invents its own.
- **The new formula is explicit** with different weights and a different scaling factor (×8 instead of ×10). This shows the PM is in control of the math, not the AI.
- **"Keep the same output format and thresholds"** means the bar charts, recommendations, and actions all carry over. Only the criteria and formula change.
- If you remove the formula, the AI will guess weights for the new criteria — and they will be wrong for your team. If you remove "Keep the same output format," the AI might redesign the entire output.

---

## Bonus: Debug Prompt Template

Use this when your generated code throws an error or produces wrong output.

```
My code is broken. Here's the error:

[Paste the full error message here]

Here's the code that caused it:

[Paste the relevant code section — or the whole file if it's short]

Fix the error. Explain what went wrong in one sentence.
Do not change any other logic — only fix this specific issue.
```

**When to use:** Paste this into the same conversation where you generated the code. The AI already has context about what the code is supposed to do, so it can fix the issue without breaking other features.

**Tip:** Always include the full error message. "It doesn't work" gives the AI nothing to work with. `TypeError: unsupported operand type(s) for +: 'int' and 'str'` tells it exactly what to fix.

---

## Bonus: Explanation Prompt Template

Use this when you want to understand what generated code does.

```
Explain this code to me like I'm a product manager, not a developer.

For each section:
1. What does it do in plain English?
2. Why is it there — what would break if you removed it?
3. What could I change without breaking things?

[Paste the code here]
```

**When to use:** After generating any tool, paste the code back with this prompt to build your understanding. Knowing what the code does helps you write better follow-up prompts.

**Tip:** You do not need to understand every line. Focus on understanding the structure: what are the inputs, what are the outputs, and where does the decision logic live.
