# What Is Vibe Coding

Vibe coding is building software by describing what you want in plain English and letting an AI write the code. You focus on the *what* — the requirements, the logic, the output format — and the AI handles the *how* — the syntax, the data structures, the implementation details.

The term was coined by Andrej Karpathy in early 2025. His description: "You fully give in to the vibes, embrace exponentials, and forget that the code even exists."

This document unpacks that idea, explains where it fits, and clarifies what it means for product managers specifically.

---

## The Core Idea

Traditional software development requires two kinds of knowledge:

1. **What to build** — Requirements, logic, edge cases, user experience
2. **How to build it** — Programming languages, frameworks, data structures, syntax

Engineers have both. Product managers have the first but not the second. This has always created a gap: PMs know what they want but cannot build it themselves. They write specs, hand them to engineers, wait for implementation, review the result, request changes, and wait again.

Vibe coding closes that gap for a specific category of tools. If you can describe what you want clearly enough — inputs, logic, output format — an AI assistant can generate working code from your description. You do not need to know Python. You need to know what a good decision framework looks like, what a RICE score is, or how retention cohorts work. Those are PM skills.

---

## What It Is Not

Vibe coding is not a replacement for software engineering. Here is where the boundary sits:

| Vibe Coding | Software Engineering |
|---|---|
| Prototypes and proof-of-concepts | Production systems serving customers |
| Internal tools for your own workflow | Scalable applications with many users |
| Quick analysis scripts | Reliable, tested, maintained codebases |
| Personal utilities | Systems that handle sensitive data securely |
| Workshop and learning exercises | Code that other engineers will maintain |

If you are building something that only you (or your team) will use, and it does not handle sensitive data, and it does not need to scale — vibe coding is a great fit. If any of those conditions are false, you need engineering.

---

## The Workflow

The vibe coding workflow is a loop with five steps:

```
DESCRIBE  →  GENERATE  →  RUN  →  OBSERVE  →  ITERATE
    ↑                                              │
    └──────────────────────────────────────────────┘
```

1. **Describe:** Write a prompt in plain English that specifies what the tool should do. Include inputs, calculations, output format, and constraints.
2. **Generate:** Paste the prompt into an AI assistant (Claude, ChatGPT). The AI writes the code.
3. **Run:** Copy the code into your editor (Replit, Cursor) and execute it.
4. **Observe:** Does the tool do what you intended? Check the inputs, the logic, the output.
5. **Iterate:** If something is off, write a follow-up prompt that describes the change. Go back to step 1.

Each loop takes 2-5 minutes. In a typical session, you go through 3-5 loops to build a complete tool.

---

## Why PMs Are Good at This

Vibe coding requires the same skills that make someone a good product manager:

- **Writing clear requirements.** A prompt is a product spec. The more precise your requirements, the better the output. Numbered lists, exact formulas, and output examples all transfer directly.
- **Defining acceptance criteria.** When you observe the output, you are doing acceptance testing. Does the score match the formula? Does the recommendation make sense? Does the output format work?
- **Iterating based on feedback.** When the tool does not do what you wanted, you write a change request. "Add these three things. Keep existing logic. Change only what I listed." That is the same sentence structure you use in Jira comments.
- **Scoping work.** Knowing what to include and what to leave out is the core PM skill. A prompt that asks for too much produces bad results — just like a ticket that is too ambitious gets deprioritized.

The mindset shift is not learning a new skill. It is applying an existing skill in a new context.

---

## How It Differs from Using ChatGPT for Other Tasks

You probably already use AI assistants for writing, summarizing, or brainstorming. Vibe coding is different in three ways:

1. **The output is executable.** When you ask ChatGPT to write an email, you get text. When you vibe code, you get a program that runs, takes input, and produces output. It is a tool, not a document.

2. **The conversation is cumulative.** Each prompt builds on the last. Prompt #1 creates the base. Prompt #2 adds features. Prompt #3 customizes it. The AI maintains context across the conversation, so your tool grows incrementally.

3. **You test the result.** Writing a draft email is low-stakes — you read it and tweak it. Running code is binary: it either works or it does not. This forces more precision in your prompts and gives you unambiguous feedback.

---

## The History

AI code generation has been developing for several years, but three things came together in 2024-2025 to make vibe coding accessible to non-programmers:

1. **Language models got good enough.** Earlier models could write simple functions but struggled with multi-part requirements. Current models (Claude, GPT-4, and beyond) reliably generate 80-120 lines of working code from a single prompt.

2. **Free tiers became usable.** Claude.ai, ChatGPT, and Replit all offer free tiers sufficient for building the tools in this workshop. You do not need to pay or install anything.

3. **The prompt format stabilized.** Early code generation required specialized syntax or technical knowledge. The current format — plain English with numbered requirements — is something anyone can write.

---

## Key Vocabulary

| Term | Definition |
|---|---|
| **Prompt** | The plain-English description you give to the AI. Includes requirements, constraints, and output format. |
| **Generate** | The AI writes code based on your prompt. |
| **Iterate** | You refine the tool with follow-up prompts in the same conversation. |
| **Constraint** | A rule that limits what the AI does — like "Python built-ins only" or "keep it under 100 lines." |
| **Artifact** | In Claude, the generated code appears in a side panel called an Artifact. You can copy it from there. |
| **Context window** | The AI's memory within a single conversation. It remembers everything you and it have said, so follow-up prompts can reference earlier work. |

---

## Next Steps

- To understand what happens under the hood when you paste a prompt, read [How AI Assistants Work](how-ai-assistants-work.md).
- To learn how to write more effective prompts, read [Prompt Engineering](prompt-engineering.md).
- To see practical applications, read [PM Use Cases](pm-use-cases.md).
