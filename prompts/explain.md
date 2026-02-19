# Prompts for Understanding Code

Use these prompts when you want to understand what generated code does, learn how a specific section works, or build enough knowledge to write better follow-up prompts.

You do not need to understand every line. Focus on understanding the structure: what are the inputs, what are the outputs, and where does the decision logic live.

---

## Full Code Walkthrough

Get a plain-English explanation of an entire file.

```
Explain this code to me like I'm a product manager, not a developer.

For each section:
1. What does it do in plain English?
2. Why is it there — what would break if you removed it?
3. What could I change without breaking things?

[Paste the code here]
```

**When to use:** After generating any tool for the first time. This builds your mental model of the code so you can write more targeted follow-up prompts.

---

## Explain One Function

Understand a specific piece of the code.

```
Explain what this function does in plain English:

[Paste the function]

Answer these questions:
1. What goes in? (What inputs does it take?)
2. What comes out? (What does it return?)
3. What is the logic in between?
4. Give me a concrete example with real numbers.
```

**When to use:** When the full walkthrough is too much and you want to zoom in on one specific function — like the scoring formula or the bar chart display.

---

## Explain the Formula

Understand the math behind a calculation.

```
Explain this formula step by step:

[Paste the formula or the line of code that calculates the score]

1. What does each variable represent?
2. Walk me through the calculation with these example values:
   [Provide example inputs]
3. What range of outputs is possible?
4. What makes the output go up vs down?
```

**When to use:** When you want to verify that the scoring formula works the way you intended. Especially useful for the Decision Framework weighted score, RICE calculations, and A/B test sample size formulas.

---

## Explain the Flow

Understand the order of operations — what happens when a user runs the tool.

```
Walk me through what happens when a user runs this program, step by step.

For each step:
- What does the user see?
- What does the user type?
- What does the program do with that input?

Use a real example — pretend the user is evaluating a feature called "Add dark mode to the app" with scores of 8, 5, 7, 6.

[Paste the code here]
```

**When to use:** When you want to trace the user experience from start to finish. This is how the [participant guide](../workshop/participant-guide.md) verifies that the generated tool matches the spec.

---

## Compare Two Versions

Understand what changed between two versions of the code.

```
Here is version 1 of my code:

[Paste version 1]

Here is version 2:

[Paste version 2]

What changed? For each change:
1. What was it before?
2. What is it now?
3. Why would someone make this change?
4. Does this change affect the output?
```

**When to use:** After Prompt #2 or #3 when the AI gives you a new version and you want to verify it only changed what you asked for.

---

## Explain an Error

Understand what an error message means before trying to fix it.

```
I got this error when running my Python code:

[Paste the full error message]

Explain in plain English:
1. What does this error mean?
2. What line of code caused it?
3. What is the most likely reason?
4. How would a developer fix it?

Don't fix the code yet — just explain what's going on.
```

**When to use:** When you want to understand an error before asking the AI to fix it. Knowing what went wrong helps you verify the fix is correct.

---

## Explain Python Concepts

Understand a specific Python feature you see in the generated code.

```
I'm a product manager learning to read Python code. Explain this concept:

[Paste the line or block of code that uses the concept]

1. What does [concept] mean in Python?
2. Why is it used here instead of something simpler?
3. Show me what this specific line produces with a concrete example.

Keep the explanation non-technical — use analogies if helpful.
```

**Common concepts you might ask about:**
- `f"Score: {score:.1f}"` — What does `:.1f` mean?
- `while True:` — Why does it loop forever?
- `try: ... except ValueError:` — What is exception handling?
- `if __name__ == "__main__":` — Why is this at the bottom?
- `label = "Low" if value <= 3 else "High"` — What is this one-line if?
- `with open(filename, "a") as f:` — What does `with` and `"a"` do?

---

## Ask "What If I Change This?"

Understand the impact of a change before making it.

```
If I change [specific thing] in this code, what happens?

[Paste the relevant code section]

Specifically:
1. What output changes?
2. Does anything break?
3. What else would I need to update to keep things consistent?
```

**When to use:** Before modifying thresholds, weights, labels, or other values. For example: "What if I change the Strong Go threshold from 15 to 20?" or "What if I add a fifth scoring criterion?"

---

## Tips for Learning from Code

- **You don't need to understand every line.** Focus on the parts that implement your product logic — the formula, the thresholds, the output format.
- **Ask about one thing at a time.** "Explain the whole file" is useful once. After that, zoom in on specific functions or lines.
- **Use concrete examples.** "Explain the formula" is vague. "Walk me through the formula with Customer Value=8, Effort=5, Alignment=7, Confidence=6" gives you a tangible answer.
- **Learning to read code makes you better at prompting.** When you understand the structure, you can write more precise change requests.
