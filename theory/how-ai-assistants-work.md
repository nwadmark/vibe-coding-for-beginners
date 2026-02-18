# How AI Assistants Work

This is a non-technical explanation of what happens when you paste a prompt into Claude or ChatGPT and it generates code. You do not need to understand this to use vibe coding effectively, but knowing the basics helps you understand why the AI sometimes gets things right, sometimes gets them wrong, and how to steer it.

---

## The 30-Second Version

AI coding assistants are language models. They have been trained on vast amounts of text — including millions of lines of code, documentation, tutorials, and Stack Overflow answers. When you give them a prompt, they generate a response one word (technically, one "token") at a time, predicting what should come next based on patterns they learned during training.

They do not "understand" code the way a developer does. They are extremely good at pattern matching: given a description of a tool, they assemble code from patterns they have seen before. This is why specific, structured prompts work better than vague ones — the more your prompt looks like the kinds of descriptions that appear alongside good code in the training data, the better the output.

---

## What Happens When You Paste a Prompt

Here is the sequence, simplified:

```
Your prompt                The model                  The output
─────────────              ─────────                  ──────────
"Build me a tool           Processes your text.       Generates code
 that scores features      Matches patterns from      one token at a time.
 on 4 criteria..."         training data.             Assembles functions,
                           Predicts what code         variables, and logic
                           should follow this         that match your
                           kind of description.       description.
```

1. **Your prompt goes in as text.** The model reads the entire prompt at once. It does not execute code — it reads your description.

2. **The model predicts the response.** Based on patterns from training, it predicts what a helpful response looks like. For a coding prompt, that means Python code with the features you described.

3. **The response is generated sequentially.** The model writes one token at a time, left to right. Each token is influenced by everything that came before — both your prompt and the tokens it has already generated. This is why it can maintain consistency within a response.

4. **The entire conversation is context.** When you send Prompt #2 in the same conversation, the model sees Prompt #1, its response, and your new prompt. This is how it "remembers" what it built before and adds to it.

---

## Why Structured Prompts Work Better

The model has been trained on patterns. Some patterns appear much more frequently than others:

| Prompt style | How common in training data | Result quality |
|---|---|---|
| "Build me a tool that does X, Y, Z" with numbered requirements | Very common — matches tutorials, documentation, specs | High — the model has many good examples to draw from |
| "Make something cool with Python" | Vague — could match anything | Low — the model guesses what you want |
| Exact formula: `Score = (A×2 + B×1.5) / C × 10` | Specific — matches technical documentation | High — the model reproduces the formula exactly |
| "Make the output look nice" | Subjective — "nice" has no pattern | Low — the model invents its own idea of "nice" |

The principle: **the more your prompt resembles structured documentation, the better the output.** This is why numbered lists, exact formulas, output examples, and explicit constraints all improve results.

---

## Why the AI Gets Things Wrong

Understanding common failure modes helps you anticipate and prevent them.

### It invents things you did not ask for

The model predicts what a "complete" response looks like. If you ask for a tool with 5 features, the model may add a 6th because it has seen similar tools that include it. The fix: add constraints like "Add these three things only" and "Do not add features I did not ask for."

### It changes things you asked it to keep

When you say "improve the output formatting," the model may rewrite the entire file — including the scoring formula. It is not disobeying you. It is generating a "complete improved version" based on patterns. The fix: say explicitly "Keep existing logic. Change only the formatting."

### It uses libraries you cannot install

The model has been trained on code that uses pandas, numpy, Flask, and hundreds of other libraries. If you do not say "Python built-ins only," it will reach for whatever library seems most appropriate. The fix: always include library constraints.

### It generates code that looks right but calculates wrong

The model assembles code from patterns, not from mathematical reasoning. It might write a formula that looks like yours but has a subtle operator precedence error. The fix: always test with known inputs where you can verify the math by hand.

### It gives different code every time

Language models are probabilistic. The same prompt can produce different outputs on different runs. Variable names, function structure, and code organization will vary. The logic should be the same if your prompt is specific enough, but the surface-level code will differ. This is normal.

---

## The Context Window

The context window is the model's working memory for a single conversation. Everything you type and everything the model responds with goes into this window.

**Why it matters for vibe coding:**

- When you send Prompt #2, the model sees Prompt #1 and the code it generated. This is how it knows what "the tool" refers to and how to modify it.
- If the conversation gets very long (many prompts, many versions of the code), the model may start losing track of earlier details. This is rare for workshop-sized conversations but happens with extended projects.
- Starting a new conversation means the model has no memory of previous work. Always paste follow-up prompts in the same conversation.

**Context limits by model:**

| Model | Approximate context window |
|---|---|
| Claude (free tier) | 200,000 tokens (~150,000 words) |
| ChatGPT (free tier) | 128,000 tokens (~96,000 words) |

For the tools in this workshop, you will never come close to these limits. They matter more for larger projects or very long conversations.

---

## Temperature and Creativity

AI models have a "temperature" setting that controls how predictable the output is. Lower temperature means more deterministic (the model picks the most likely next token). Higher temperature means more variety (the model sometimes picks less likely tokens).

For code generation, most AI assistants use a lower temperature internally. This is why the code is generally consistent and functional — the model is being conservative. But it also means that when you run the same prompt twice, you get slightly different but structurally similar code.

You cannot control the temperature directly in Claude or ChatGPT's chat interfaces. But you can influence it through your prompts: more specific prompts lead to more deterministic output, and vaguer prompts lead to more varied output.

---

## The Difference Between Claude and ChatGPT

Both are large language models capable of generating code. The differences that matter for this workshop:

| Aspect | Claude | ChatGPT |
|---|---|---|
| Code display | Artifacts panel (side panel) with a Copy button | Inline code blocks with a Copy Code button |
| Conversation memory | Remembers full conversation | Remembers full conversation |
| Strengths | Follows complex instructions precisely, good at long-form structured output | Good at conversational back-and-forth, widespread familiarity |
| Free tier limits | Usage caps that reset periodically | Usage caps that reset periodically |

For the purposes of this workshop, both work equally well. The prompts are designed to produce good results with either model.

---

## Key Takeaways

1. **AI assistants are pattern matchers, not thinkers.** They generate code by predicting what should come next based on training data. Structured prompts match better patterns and produce better code.

2. **Specificity is your lever.** The more specific your prompt (exact formulas, output examples, explicit constraints), the more predictable and correct the output.

3. **The conversation is the context.** Follow-up prompts work because the model sees the entire conversation history. Always build on the same conversation.

4. **Verify the output, not the code.** You do not need to read the code to check if it works. Run the tool with known inputs and verify the output matches your expectations.

5. **Errors are normal, not failures.** The model generates plausible code, not guaranteed-correct code. Testing and iterating are part of the process for everyone, including experienced developers.
