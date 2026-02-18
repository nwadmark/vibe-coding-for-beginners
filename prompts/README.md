# Prompt Library

This folder contains copy-paste-ready prompts for building PM tools with AI coding assistants. Each prompt is tested with both Claude and ChatGPT. Pick the file that matches what you are trying to do, copy the prompt, and paste it into your AI assistant.

---

## Table of Contents

| File | What It Contains | When to Use It |
|---|---|---|
| [workshop-prompts.md](workshop-prompts.md) | The 5 prompts from the live workshop (Prompts #1, #2, #3A, #3B, #3C) | During or after the workshop to rebuild the Decision Framework tool |
| [generate.md](generate.md) | Prompt templates for building new PM tools from scratch | When starting a brand-new tool — any of the 7 build projects or your own idea |
| [improve.md](improve.md) | Prompts for adding visual polish, better UX, and output formatting | When your tool works but looks rough or is hard to use |
| [debug.md](debug.md) | Prompts for fixing errors, tracing bugs, and recovering from broken code | When your code crashes, shows wrong output, or behaves unexpectedly |
| [extend.md](extend.md) | Prompts for adding new features to an existing tool | When your tool works and you want to add a specific capability |
| [explain.md](explain.md) | Prompts for understanding what code does and how it works | When you want to learn from generated code or understand someone else's |
| [advanced.md](advanced.md) | Advanced patterns — chaining prompts, constraints, output control | When you are comfortable with basics and want more precise control |

---

## Tips for Adapting Prompts to Your Context

- **Replace ShopFlow with your product name.** The example prompts use "ShopFlow" as a placeholder. Swap it for whatever product you manage — the AI will tailor outputs accordingly.
- **Adjust criteria to match your team's framework.** If your team uses RICE instead of the weighted scorecard, change the criteria and formula. If you prioritize revenue over user impact, change the weights.
- **Change the output format to match your workflow.** If your team reads Notion docs, ask for Markdown. If you present in meetings, ask for a summary table. If you export to spreadsheets, ask for CSV output.

---

## How Prompts Work with Different AI Tools

| Tool | How to Use These Prompts |
|---|---|
| **Claude** | Paste into the chat. For code, look for the Artifact panel on the right — click Copy to grab the generated code. You can also use Claude's Projects feature to save prompts for reuse. |
| **ChatGPT** | Paste into the chat. Hover over code blocks and click "Copy code." For longer conversations, the AI remembers context from earlier prompts in the same thread. |
| **Cursor** | Use `Ctrl+K` (inline edit) to modify existing code or `Ctrl+L` (chat) to generate new code. Paste the prompt into the chat panel. Cursor can read your open files for context. |

---

## Quick Start

1. Open your AI assistant (Claude, ChatGPT, or Cursor)
2. Pick a prompt from the relevant file above
3. Copy the entire prompt — including the constraints at the bottom
4. Paste it and wait for the generated code
5. Copy the code into Replit or your editor and run it
6. If something is off, use a prompt from [debug.md](debug.md) or [improve.md](improve.md)
