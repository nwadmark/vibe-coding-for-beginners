# Participant Guide

Keep this document open during the entire workshop. Follow along step by step.

---

## Quick Reference

| I Need... | Go To |
|---|---|
| The prompts to paste | [Part 2: Build](#part-2-build-001500050) — Prompts #1, #2, #3 are inline |
| Help with an error | Troubleshooting boxes after each step, or [Stuck?](#stuck) at the bottom |
| Setup instructions | [Pre-work](pre-work.md) — complete before the session |
| The slide deck | Your facilitator will share it on screen |
| To share my finished tool | [Part 3: Ship + Reflect](#part-3-ship--reflect-005001000) |
| What to do after the workshop | [Part 4: Next Steps](#part-4-next-steps-010001010) |

---

## Part 1: Orientation (00:00–00:15)

### What We Are Building Today

The **PM Decision Framework** — a command-line tool that scores feature ideas on four criteria and tells you whether to prioritize, investigate, or kill them.

By the end of the session you will have:
- A working tool you built yourself
- Experience with the vibe coding workflow
- A foundation to build six more PM tools on your own

### The Vibe Coding Loop

This is the workflow you will repeat throughout the session:

```
    ┌──────────┐
    │ DESCRIBE │  ← You write a prompt in plain English
    └────┬─────┘
         ▼
    ┌──────────┐
    │ GENERATE │  ← AI writes the code
    └────┬─────┘
         ▼
    ┌──────────┐
    │   RUN    │  ← You paste the code and run it
    └────┬─────┘
         ▼
    ┌──────────┐
    │ OBSERVE  │  ← You check: does this do what I wanted?
    └────┬─────┘
         ▼
    ┌──────────┐
    │ ITERATE  │  ← You refine with a follow-up prompt
    └────┬─────┘
         │
         └──────── back to DESCRIBE ──────►
```

You will go through this loop three times today, each time adding more to your tool.

### Your Tools Today

- **AI Assistant:** Claude.ai or ChatGPT (open in a browser tab)
- **Code Editor:** Replit (browser) or Cursor (local)

### The Workflow

```
AI assistant tab          Code editor tab
─────────────────         ─────────────────
1. Paste prompt      →
2. Read the code     →    3. Paste code here
                          4. Click Run
5. See the result    ←    (output appears)
6. New prompt        →    (repeat)
```

---

## Part 2: Build (00:15–00:50)

### Loop 1: Generate the Base Tool (00:15–00:25)

**Goal:** Go from zero to a working Decision Framework in 10 minutes.

**Step 1:** Switch to your AI assistant tab (Claude.ai or ChatGPT).

**Step 2:** Copy and paste this entire prompt:

> **PROMPT #1 — Copy everything inside this box:**
>
> ```
> I'm a product manager. I want to build a simple command-line PM Decision Framework Tool in Python.
>
> The tool should:
> 1. Ask me to describe a feature idea (one sentence)
> 2. Score the feature on 4 criteria (1-10 scale each):
>    - Customer Value: How much will customers benefit?
>    - Implementation Effort: How hard to build? (10 = very hard)
>    - Strategic Alignment: Does it fit our strategy?
>    - Confidence: How sure are we of our assumptions?
> 3. Calculate a weighted decision score:
>    Score = (CustomerValue×2 + StrategicAlignment×1.5 + Confidence×1) / Effort × 10
> 4. Output a recommendation:
>    Score > 15: 🟢 Strong Go — Prioritize this
>    Score 10-15: 🟡 Maybe — Needs more validation
>    Score < 10: 🔴 No Go — Deprioritize or kill
> 5. Show a score breakdown per criterion
> 6. Add a risk flag if effort > 7:
>    ⚠️ High effort — validate with engineering first
> 7. Show a suggested PM action:
>    Strong Go → 📌 Add to next sprint backlog
>    Maybe → 🔍 Schedule discovery session
>    No Go → 📁 Document reasoning and archive
> 8. Ask if they want to evaluate another feature
>
> Use Python built-ins only (no pip install needed).
> Add plain-English comments explaining each section.
> Keep it under 120 lines.
> ```

**Step 3:** Wait for the AI to generate the code.

- **In Claude:** Look for the Artifact panel on the right side. Click the **Copy** button in the top-right corner of the code block.
- **In ChatGPT:** Look for the code block in the response. Hover over it and click the **Copy code** button.

> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> ⚠️ IF YOU SEE THIS: "AI GAVE ME DIFFERENT CODE THAN THE EXAMPLE"
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> Your code looks nothing like the person sitting next to you.
>
> WHAT IT MEANS:
> This is completely expected. AI assistants generate fresh code every time.
> Your version might use different variable names, different formatting,
> or even a different approach — and still work perfectly.
>
> WHAT TO DO:
> 1. Do not panic. Different-looking code is normal.
> 2. Copy it and paste it into your editor anyway.
> 3. Run it. If it asks for a feature name and scores, it is working.
> 4. If it does something completely unrelated to scoring features,
>    go back to the AI and paste the prompt again.
>
> THIS IS NORMAL: Professional developers get different results from
> AI tools every time. There is no single "correct" version of the code.
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Step 4:** Switch to your code editor.

- **In Replit:** Select all existing code in the editor (Ctrl+A / Cmd+A), delete it, and paste the new code (Ctrl+V / Cmd+V).
- **In Cursor:** Create a new file called `decision_tool.py`, paste the code, and save.

> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> ⚠️ IF YOU SEE THIS ERROR
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> Error: `IndentationError: unexpected indent`
> or: `IndentationError: expected an indented block`
>
> WHAT IT MEANS:
> Python cares about the spaces at the beginning of each line. When you
> copy-paste code, sometimes the spacing gets scrambled. This is not
> your fault — it is a copy-paste quirk.
>
> WHAT TO DO:
> 1. Go back to your AI assistant tab.
> 2. Copy the code again — this time, click the **Copy** button
>    instead of highlighting with your mouse (mouse-selecting
>    sometimes grabs extra spaces).
> 3. In your editor, select all (Ctrl+A / Cmd+A) and delete.
> 4. Paste the fresh copy (Ctrl+V / Cmd+V).
> 5. Run it again.
>
> THIS IS NORMAL: Indentation errors are the #1 most common Python
> error in the world. Every Python developer has seen this hundreds
> of times. It is a spacing issue, not a logic issue.
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Step 5:** Run it.

- **In Replit:** Click the green **Run** button.
- **In Cursor:** Open the terminal and run `python decision_tool.py`.

> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> ⚠️ IF YOU SEE THIS ERROR
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> Error: `SyntaxError: invalid syntax`
> (sometimes with a little arrow ^ pointing to a specific spot)
>
> WHAT IT MEANS:
> Python found something it does not understand — a typo, a missing
> colon, or a mismatched parenthesis. When AI generates code, this
> occasionally happens. It is like a grammatical error in a sentence.
>
> WHAT TO DO:
> 1. Copy the **entire error message** (including the line number).
> 2. Go back to your AI assistant tab.
> 3. Paste the error and say: "I got this error when I ran the code.
>    Fix it."
> 4. The AI will give you corrected code. Copy the whole thing and
>    replace everything in your editor again.
>
> THIS IS NORMAL: Syntax errors happen to professional developers
> every single day. The fix is almost always a one-character change
> that the AI will catch instantly.
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> ⚠️ IF THIS HAPPENS: "NOTHING HAPPENS WHEN I CLICK RUN"
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> You clicked Run but the screen just... sits there. No error, no
> output, nothing.
>
> WHAT IT MEANS:
> The program is probably waiting for you to type something, but it
> is waiting in a different panel than the one you are looking at.
>
> WHAT TO DO:
> 1. **In Replit:** Look at the right side of the screen — the
>    **Console** panel. Click inside it. You should see a blinking
>    cursor or a prompt like "Describe a feature idea:". Type there.
> 2. **In Cursor:** Look at the **Terminal** panel at the bottom.
>    Click inside it and type your answer there.
> 3. If you see absolutely nothing anywhere, try clicking Run again.
> 4. If it still does nothing, select all code, delete it, re-paste
>    from the AI, and try once more.
>
> THIS IS NORMAL: The "where do I type?" confusion happens to almost
> everyone the first time. Once you find the right panel, it clicks
> and you will not lose it again.
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Expected output:** The tool asks you to describe a feature. Try this example:

```
Feature: Add one-click checkout to ShopFlow mobile app

Customer Value (1-10): 8
Implementation Effort (1-10): 6
Strategic Alignment (1-10): 7
Confidence (1-10): 5
```

You should see a calculated score, a recommendation (likely 🟢 or 🟡), a score breakdown, and a suggested PM action.

> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> ⚠️ IF YOU SEE THIS ERROR
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> Error: `NameError: name 'customer_value' is not defined`
> (or any variable name instead of 'customer_value')
>
> WHAT IT MEANS:
> The code is trying to use a name it does not recognize. This usually
> means the AI used a variable in one place but spelled it differently
> somewhere else — like calling something `cust_value` at the top and
> `customer_value` at the bottom.
>
> WHAT TO DO:
> 1. Copy the **full error message**.
> 2. Go back to your AI assistant.
> 3. Paste the error and say: "I got a NameError. It looks like a
>    variable name is misspelled or missing. Fix it."
> 4. Copy the corrected code and replace everything in your editor.
>
> THIS IS NORMAL: Misspelled variable names are one of the top 3
> errors in all of programming. The AI usually fixes it on the first
> try when you show it the error.
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> ⚠️ IF YOU SEE THIS ERROR
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> Error: `TypeError: unsupported operand type(s) for *: 'str' and 'int'`
> (or a similar TypeError mentioning 'str' and 'int')
>
> WHAT IT MEANS:
> Python is trying to do math with text instead of numbers. When you
> type "8" into the tool, Python sometimes treats it as the text
> character "8" instead of the number 8. The AI needed to convert it
> and may have missed a spot.
>
> WHAT TO DO:
> 1. Copy the **full error message**.
> 2. Go back to your AI assistant.
> 3. Paste the error and say: "I got a TypeError. It looks like the
>    input is not being converted to a number. Make sure all score
>    inputs are converted to integers with int()."
> 4. Copy the corrected code and replace everything in your editor.
>
> THIS IS NORMAL: This is Python's most common type error. It happens
> because Python does not automatically guess whether "8" means the
> number eight or the text character "8". One small fix and it is gone.
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> **💡 PM Tip:** You described what you wanted in plain English. The AI turned it into working software. That is vibe coding. You did not need to know Python — you needed to know what a good decision framework looks like. That is a PM skill.

#### Troubleshooting — Loop 1

| Problem | Fix |
|---|---|
| `SyntaxError` or `IndentationError` | The code may not have copied cleanly. Go back to the AI assistant, copy the code again carefully, and replace everything in your editor. |
| The tool runs but the score formula seems off | Paste the code back into your AI assistant and say: "The score calculation doesn't match the formula I gave you. Fix it." |
| `input()` not working in Replit | Make sure you are clicking in the **Console** panel (right side) to type your answers, not in the code editor. |

---

### Loop 2: Improve the Tool (00:25–00:40)

**Goal:** Add visual score bars and input labels to make the tool more useful.

Keep your existing code in the editor. Switch to your AI assistant tab.

**Important:** If you are using Claude, paste Prompt #2 in the **same conversation** as Prompt #1. If you are using ChatGPT, do the same. The AI remembers context from earlier in the conversation.

> **PROMPT #2 — Copy everything inside this box:**
>
> ```
> The tool works! Now improve it.
>
> Add these features:
> 1. After each score input, show a brief label:
>    1-3: Low, 4-6: Medium, 7-9: High, 10: Maximum
> 2. After the recommendation, show a simple visual:
>    Customer Value    ████████░░  8/10
>    Effort (impact)   ██████░░░░  6/10
>    Strategic Align   ███████░░░  7/10
>    Confidence        █████░░░░░  5/10
>    Use █ for filled, ░ for empty, 10 chars total
> 3. Add a separator line between evaluations
>
> Keep existing logic. Add these three things only.
> ```

Now do the same cycle:

1. **Copy** the new code from the AI assistant
2. **Replace** all the code in your editor with the new version (Ctrl+A, then Ctrl+V)
3. **Run** it

**Expected output:** Same flow as before, but now you see labels after each input (like "High" for an 8) and a visual bar chart after the recommendation.

> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> ⚠️ IF THIS HAPPENS: "OUTPUT LOOKS WRONG BUT NO ERROR"
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> The tool runs, no red error text appears, but something looks off.
> Maybe the bars are jumbled, the score seems way too high, or the
> labels are in the wrong place.
>
> WHAT IT MEANS:
> The code runs fine — Python is happy. But the logic or formatting
> does not match what you asked for. This is the most interesting kind
> of problem because it is a product issue, not a code issue. You are
> the one who spots it because you know what the output should look like.
>
> WHAT TO DO:
> 1. Take a close look at what is wrong. Be specific. ("The bars all
>    show 10/10 even though I entered different scores" is better than
>    "it looks weird.")
> 2. Go back to your AI assistant.
> 3. Describe what you see vs. what you expected: "The bar chart shows
>    all bars at the same length, but my scores were 8, 6, 7, 5. The
>    bars should be different lengths. Fix this."
> 4. Copy the corrected code and replace everything in your editor.
>
> THIS IS NORMAL: Finding logic bugs by looking at the output is
> literally what QA testing is. You are doing product work right now —
> testing, spotting issues, and writing clear bug reports. That is a
> skill, not a failure.
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> **💡 PM Tip:** You gave the AI a change request — add these three things, keep everything else. That is iterative product development. You are writing prompts the same way you would write acceptance criteria in a ticket. The skill transfers directly.

#### Troubleshooting — Loop 2

| Problem | Fix |
|---|---|
| The bars show up wrong (misaligned, wrong characters) | Paste the output back into your AI assistant and say: "The visual bars aren't aligned correctly. Here's what I see: [paste the output]. Fix the alignment." |
| Some of the old features disappeared | The AI may have rewritten too much. Say: "You removed the risk flag and PM action suggestion. Add those back." |
| The labels don't appear after input | Say: "The labels (Low/Medium/High/Maximum) should appear immediately after I enter each score, before the next question." |

---

### Loop 3: Make It Yours (00:40–00:50)

**Goal:** Customize the tool with one new feature that you choose.

Pick **one** of the three prompts below. Each adds a different capability. Choose whichever sounds most useful to you.

#### Option A: Add a Decision Log

This saves every evaluation to a file so you can review past decisions.

> **PROMPT #3A — Copy everything inside this box:**
>
> ```
> Add a decision log feature.
>
> After each evaluation, append results to decision_log.txt in this format:
>
> =====================================
> Date: [YYYY-MM-DD]
> Feature: [feature name]
> Score: [score]/20
> Decision: [Go/Maybe/No Go]
> ─────────────────────────────────────
> Customer Value:        [x]/10
> Implementation Effort: [x]/10
> Strategic Alignment:   [x]/10
> Confidence:            [x]/10
> =====================================
>
> Tell the user: ✅ Saved to decision_log.txt
> At program start, if log exists, show:
> 📋 You have [N] previous evaluations. View? (yes/no)
> ```

#### Option B: Add Comparison Mode

This lets you evaluate multiple features and rank them side by side.

> **PROMPT #3B — Copy everything inside this box:**
>
> ```
> Add a comparison mode.
>
> At the start ask:
> 'Evaluate single feature or compare? (single/compare)'
>
> If compare:
> - Evaluate features one by one
> - Ask 'Add another? (yes/no)' after each
> - At the end show a ranked comparison table:
>
> FEATURE COMPARISON
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> Rank  Feature            Score  Decision
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
>  1.   [feature]          [18.2] 🟢 Strong Go
>  2.   [feature]          [12.5] 🟡 Maybe
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 🏆 Top recommendation: [feature name]
>
> If single: use existing flow.
> ```

#### Option C: Custom Criteria

This replaces the default scoring criteria with your own team's priorities.

> **PROMPT #3C — Copy everything inside this box:**
>
> ```
> Replace the 4 scoring criteria with my team's criteria:
> 1. User Impact: How many users affected? (1-10)
> 2. Revenue Potential: Does this drive revenue? (1-10)
> 3. Build Effort: Engineering complexity (1-10, higher = harder)
> 4. Strategic Fit: Fits 2025 roadmap? (1-10)
>
> New formula:
> Score = (UserImpact×2 + RevenuePotential×2 + StrategicFit) / BuildEffort × 8
>
> Keep the same output format and thresholds.
> ```

**After pasting your chosen prompt:**

1. **Copy** the new code from the AI assistant
2. **Replace** all the code in your editor
3. **Run** it and test it out

> **💡 PM Tip:** Look at what you did. You wrote a feature spec in plain English — inputs, outputs, format, behavior. The AI implemented it. This is the same skill you use when writing tickets, PRDs, or acceptance criteria. Vibe coding is not about learning to code. It is about applying PM skills you already have in a new context.

#### Troubleshooting — Loop 3

| Problem | Fix |
|---|---|
| Decision log file is not created | In Replit, check the Files panel on the left — the file may be there but not visible until you refresh. In Cursor, check the same folder as your Python file. |
| Comparison table is misaligned | Paste the output back to the AI and say: "The comparison table columns aren't aligned. Fix the formatting." |
| The tool crashes when I choose compare mode | Say: "When I select 'compare', I get this error: [paste the error]. Fix it while keeping the single evaluation mode working." |

---

## Part 3: Ship + Reflect (00:50–01:00)

### Share Your Work

**In Replit:**
1. Click the **Share** button (top right)
2. Copy the link
3. Share it in the workshop chat

**In Cursor:**
1. Take a screenshot of your tool running in the terminal
2. Share it in the workshop chat

### Reflection

Think about these three questions. You do not need to write anything down — but if the facilitator asks, be ready to share one thought.

1. **What surprised you?** Was there a moment where the AI did something you did not expect — good or bad?

2. **Where did you steer?** Think about a decision *you* made that shaped the tool. A criterion you chose, a threshold you set, a format you preferred. The AI wrote the code, but you drove the product decisions.

3. **What would you build next?** If you had another hour, what tool would you describe to the AI? A customer feedback sorter? A sprint velocity tracker? A pricing model?

> **⚠️ Watch Out:** Vibe coding is great for prototypes, internal tools, and personal utilities. It is not a replacement for production engineering. The tools you build today are useful as-is for PM work, but shipping them to customers would require engineering review, testing, and hardening. Know the boundary.

---

## Part 4: Next Steps (01:00–01:10)

### Six More Tools to Build

Each project in the `build/` folder stands on its own. Pick whichever interests you most.

| # | Tool | What It Does | Time |
|---|---|---|---|
| 02 | [Feature Prioritizer](../build/02-feature-prioritizer/) | Rank features using RICE, MoSCoW, or custom frameworks | 30-45 min |
| 03 | [Cohort Analyzer](../build/03-cohort-analyzer/) | Analyze user cohort data for retention patterns | 30-45 min |
| 04 | [A/B Test Calculator](../build/04-ab-calculator/) | Calculate sample sizes and statistical significance | 20-30 min |
| 05 | [Pricing Calculator](../build/05-pricing-calculator/) | Model pricing tiers and revenue projections | 30-45 min |
| 06 | [Feedback Analyzer](../build/06-feedback-analyzer/) | Categorize and surface themes from user feedback | 30-45 min |
| 07 | [Metric Dashboard](../build/07-metric-dashboard/) | Visualize and track key product metrics | 45-60 min |

### Recommended Reading

Before diving into the next builds, these three theory docs will deepen your understanding:

| Doc | What It Covers |
|---|---|
| [Theory: What Is Vibe Coding](../theory/) | Deeper dive into the concepts behind today's session |
| [Prompts Library](../prompts/) | Copy-paste prompts for common PM tool patterns |
| [Guides](../guides/) | Reference material for Replit, Cursor, debugging, and more |

### The Capstone (Optional)

The [capstone project](../capstone/) is a larger, self-directed build that combines skills from the workshop. It is always optional — tackle it when you are ready for a bigger challenge.

---

## Stuck?

| Problem | Where to Go |
|---|---|
| My code has an error I cannot fix | Paste the full error message into your AI assistant and ask it to fix the code |
| My AI assistant hit its rate limit | Switch to the other one (Claude ↔ ChatGPT). Both are free. |
| Replit is frozen or unresponsive | Refresh the page. Your code is auto-saved. |
| I fell behind the group | Skip to the current prompt number — each prompt generates a complete tool, not a partial one |
| I finished early | Try a different Prompt #3 option, or start exploring `build/02-feature-prioritizer/` |
| I want to keep building after the workshop | Start with the [next steps](#six-more-tools-to-build) section above |
