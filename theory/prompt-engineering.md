# Prompt Engineering for PM Tools

Prompt engineering is the skill of writing instructions that get reliable, high-quality output from AI assistants. For vibe coding, it means writing prompts that produce working tools on the first or second try instead of the fifth.

This document covers the principles with examples drawn directly from the workshop tools. For copy-paste-ready prompts, see the [Prompts Library](../prompts/).

---

## The Five Principles

### 1. Set the Role

Start your prompt by telling the AI who you are and what you are building.

**Good:**
```
I'm a product manager. Build me a command-line Decision Framework tool in Python.
```

**Weak:**
```
Build me a tool in Python.
```

**Why it matters:** The role context changes how the AI writes code. "I'm a product manager" leads to plain-English variable names (`customer_value`), clear output labels, and comments that explain concepts rather than implementation details. Without the role, you get developer-oriented code — terse variable names, minimal output, and comments about data structures.

---

### 2. Number Your Requirements

Every feature of the tool should be a numbered item. Do not write requirements as a paragraph.

**Good:**
```
The tool should:
1. Ask me to describe a feature idea
2. Score the feature on 4 criteria (1-10 scale each)
3. Calculate a weighted score using this formula: [...]
4. Show a recommendation based on the score
5. Ask if I want to evaluate another feature
```

**Weak:**
```
The tool should ask about features and score them and show a recommendation and let me do multiple.
```

**Why it matters:** Numbered lists become a checklist for the AI. It processes each item individually and is less likely to skip or merge requirements. In testing, numbered prompts produce complete implementations significantly more often than paragraph-style prompts.

---

### 3. Be Explicit About Logic

If your tool has a formula, threshold, or decision rule — write it out exactly. Do not leave it for the AI to infer.

**Good:**
```
Calculate a weighted decision score:
Score = (CustomerValue×2 + StrategicAlignment×1.5 + Confidence×1) / Effort × 10

Output a recommendation:
Score > 15: 🟢 Strong Go — Prioritize this
Score 10-15: 🟡 Maybe — Needs more validation
Score < 10: 🔴 No Go — Deprioritize or kill
```

**Weak:**
```
Calculate a score that balances value against effort and categorize the result.
```

**Why it matters:** Formulas are where vibe coding is most fragile. If you omit the formula, the AI invents one — and it will be different every time, probably not what you intended. Explicit logic means you control the product decisions (the weights, the thresholds) while the AI handles the implementation.

---

### 4. Show the Output Format

If you care about how the output looks, include an example. The AI treats examples as visual specs and reproduces them closely.

**Good:**
```
Show a simple visual:
  Customer Value    ████████░░  8/10
  Effort (impact)   ██████░░░░  6/10
  Strategic Align   ███████░░░  7/10
  Confidence        █████░░░░░  5/10
Use █ for filled, ░ for empty, 10 chars total
```

**Weak:**
```
Show a bar chart for each score.
```

**Why it matters:** "Bar chart" can mean a hundred different things. The ASCII example eliminates ambiguity — the AI knows exactly which characters to use, how wide the bars should be, and what the labels look like. If you care about the format, show the format.

---

### 5. Constrain the Implementation

Tell the AI what not to do. Without constraints, it will make its own choices — and those choices often create problems.

**Good:**
```
Use Python built-ins only (no pip install needed).
Add plain-English comments explaining each section.
Keep it under 120 lines.
```

**Weak:**
```
Make it simple.
```

**Why it matters:** Each constraint solves a specific problem. "Python built-ins only" prevents import errors in Replit. "Under 120 lines" prevents over-engineering. "Plain-English comments" makes the code readable when you revisit it. Without these, you get 300-line code with numpy imports and cryptic variable names.

---

## Common Prompt Patterns

### The Build Pattern

Use when creating a tool from scratch.

```
I'm a [role]. Build me a command-line [tool description] in Python.

The tool should:
1. [Input]
2. [Input]
3. [Calculation — include exact formula]
4. [Output — include format example]
5. [Additional output]
6. [Loop or exit condition]

[Constraints — libraries, line limit, comments]
```

### The Improve Pattern

Use when modifying a working tool.

```
The tool works! Now improve it.

Add these features:
1. [Specific addition]
2. [Specific addition]
3. [Specific addition]

Keep existing logic. Add these three things only.
```

### The Fix Pattern

Use when the tool is broken.

```
My code has this error: [paste error]

Here's the code: [paste code]

Fix the error. Explain what went wrong in one sentence.
Do not change any other logic.
```

### The Extend Pattern

Use when adding a new feature to a working tool.

```
Add a [feature name] feature.

[Describe the trigger, input, logic, and output]

[Include an example of expected output if possible]

Keep existing logic. Add this feature only.
```

---

## The Iteration Mindset

Effective vibe coding is not about writing the perfect prompt on the first try. It is about iterating quickly:

**Loop 1:** Write a prompt. Get a tool that is 70% right.

**Loop 2:** Fix what is wrong. "The bar chart is misaligned" or "The formula gives wrong results."

**Loop 3:** Add what is missing. "Now add comparison mode."

Each loop takes 2-5 minutes. Three loops takes 10-15 minutes. Trying to get everything perfect in one prompt takes longer and produces worse results.

**The rule of three:** If your first three prompts have not gotten you to a working tool, the problem is usually scope. Your tool is too complex for a single conversation. Break it into smaller pieces and build each piece separately.

---

## Prompt Anti-Patterns

Things that reliably produce bad results:

### Vague requirements

```
Make a cool PM tool.
```

The AI has no idea what you want. You will get something random.

### Paragraph-style specs

```
Build a tool that takes features and scores them on customer value and effort and alignment
and confidence and then shows a recommendation and a bar chart and saves to a file.
```

The AI may skip requirements that are buried in the middle of a long sentence. Use numbered lists.

### No formula, no format

```
Calculate a score that weighs the criteria appropriately.
```

"Appropriately" means nothing. The AI will invent weights — and they will be different every time.

### Too many changes at once

```
Add comparison mode, a decision log, custom criteria, CSV export,
input validation, color coding, and a help menu.
```

More than 3-4 additions per prompt leads to dropped features and subtle bugs. Add one or two features per prompt.

### Mixing additions with changes

```
Add a bar chart AND change the formula AND restructure the output.
```

When you mix adding new things with changing existing things, the AI is more likely to break what was already working. Separate these into different prompts.

---

## Testing Your Prompts

After the AI generates code:

1. **Run it with a known example.** Use inputs where you can calculate the expected output by hand.
2. **Check the edges.** What happens with all 10s? All 1s? Maximum effort with minimum value?
3. **Verify the format.** Does the output look like what you specified? Are the bars aligned? Are the labels correct?
4. **Test the loop.** If the tool asks "evaluate another?", say yes and verify the second run works too.

If something is off, write a targeted fix prompt. Do not re-paste the entire original prompt — that starts over from scratch.

---

## Further Reading

- For copy-paste-ready prompts: [Prompts Library](../prompts/)
- For advanced techniques (constraint stacking, output-first prompting, chaining): [Advanced Prompts](../prompts/advanced.md)
- For understanding why the AI responds the way it does: [How AI Assistants Work](how-ai-assistants-work.md)
