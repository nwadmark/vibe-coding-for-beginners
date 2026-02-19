# Prompts for Extending Tools

Use these prompts when your tool works and you want to add a specific new capability. Each prompt adds one feature without disturbing existing functionality.

**Important:** Always paste these in the **same conversation** where you generated the original code. End every extension prompt with "Keep existing logic" to protect what already works.

---

## Add File Export

Save results to a file for later reference or sharing.

```
After showing the results, ask the user:
"Save results to file? (yes/no)"

If yes, write the results to [tool_name]_results.txt in a clean, readable format.
Include a timestamp at the top (YYYY-MM-DD HH:MM).
After saving, print: ✅ Saved to [tool_name]_results.txt

Keep existing logic. Add the save feature only.
```

**Works with:** Decision Framework, RICE calculator, pricing calculator, A/B test calculator.

---

## Add CSV Export

Export data in a format that spreadsheets can import.

```
After showing the results, ask:
"Export to CSV? (yes/no)"

If yes, write results to [tool_name]_export.csv with:
- A header row with column names
- One row per item/evaluation
- All numbers unformatted (no dollar signs or commas — just raw numbers)
- Use the csv module from Python's standard library

After saving, print: ✅ Exported to [tool_name]_export.csv

Keep existing logic. Add the CSV export only.
```

**Works with:** Any tool that evaluates multiple items — RICE calculator, pricing tiers, cohort data.

---

## Add a History/Log Feature

Track evaluations across multiple sessions.

```
Add a history feature.

After each evaluation, append the result to [tool_name]_log.txt with this format:
[YYYY-MM-DD] | [item name] | Score: [score] | Result: [recommendation]

At program start, if the log file exists:
- Show how many previous entries exist
- Ask "View history? (yes/no)"
- If yes, print the last 10 entries

Use append mode so previous entries are never overwritten.
Keep existing logic. Add the history feature only.
```

**Works with:** Decision Framework, RICE calculator, any tool with a repeat loop.

---

## Add Multiple-Item Comparison

Evaluate several items and rank them side by side.

```
At the start, ask:
"Evaluate one item or compare multiple? (single/compare)"

If compare:
- Run the normal evaluation flow for each item
- After each, ask "Add another? (yes/no)"
- When done, show a ranked table sorted by score descending:

  Rank  Name               Score   Result
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   1.   [name]             [score] [recommendation]
   2.   [name]             [score] [recommendation]
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🏆 Top pick: [highest scoring name]

If single: use the existing flow unchanged.
Keep existing logic. Add comparison mode only.
```

**Works with:** Decision Framework, RICE calculator, pricing scenarios.

---

## Add Input Presets

Skip repetitive typing for common scenarios.

```
Before asking for inputs, offer preset options:

"Choose a preset or enter custom values:
 1. [Preset name] — [brief description]
 2. [Preset name] — [brief description]
 3. Custom — enter your own values"

If the user picks a preset, pre-fill the values and show them.
If the user picks custom, use the existing input flow.

Presets:
- [Preset 1]: [value1], [value2], [value3], [value4]
- [Preset 2]: [value1], [value2], [value3], [value4]

Keep existing logic. Add presets only.
```

**Customization:** Replace the preset names and values with scenarios relevant to your team. For example, a pricing calculator might have presets for "Startup pricing" and "Enterprise pricing."

---

## Add a What-If Mode

Let users tweak one variable and see how the result changes.

```
After showing results, ask:
"Run a what-if? (yes/no)"

If yes:
- Show the current values for each input
- Ask which one they want to change (show a numbered list)
- Ask for the new value
- Recalculate and show OLD vs NEW results side by side:

  [criterion]    Old: [value]  →  New: [value]
  Score          Old: [score]  →  New: [score]
  Result         Old: [rec]    →  New: [rec]

Keep existing logic. Add the what-if feature only.
```

**Works with:** Decision Framework, pricing calculator, A/B test calculator.

---

## Add Input Validation

Make the tool handle bad input gracefully instead of crashing.

```
Add input validation for all user inputs:
- Numeric inputs: if the user types text, show "Please enter a number" and ask again
- Range inputs (1-10): if the number is out of range, show "Enter a number between 1 and 10" and ask again
- Yes/no inputs: accept "yes", "y", "no", "n" (case-insensitive)
- Never crash on bad input — always re-prompt

Use a while loop with try/except for each input.
Keep existing logic. Add validation only.
```

**Works with:** Every tool. This should be one of the first extensions you add.

---

## General Extension Template

Use this for any feature not listed above:

```
Add a [feature name] feature.

How it works:
1. [Trigger — when does this feature activate?]
2. [Input — what does the user provide?]
3. [Logic — what happens with that input?]
4. [Output — what does the user see?]

[Include an example of the expected output if possible]

Keep existing logic. Add this feature only.
Do not modify the [specific part you want protected].
```

**Tips:**
- One feature per prompt. If you want two features, use two prompts.
- Always include the trigger ("after showing results," "at program start," "when the user types 'export'").
- If the AI breaks existing features while adding the new one, say: "Your addition broke [feature]. Add [new feature] without changing [existing feature]."
