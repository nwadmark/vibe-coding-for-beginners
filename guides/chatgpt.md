# ChatGPT Guide

ChatGPT is an AI assistant made by OpenAI. It is a strong alternative to Claude for this workshop, especially if you want unlimited messages on the free tier or are already familiar with it.

---

## What Makes ChatGPT Good for PMs

- **Unlimited messages on the free tier.** Unlike Claude, ChatGPT does not cap your daily messages. You can iterate as many times as you need without hitting a limit.
- **Good code generation.** ChatGPT reliably generates working Python code from structured prompts. It handles numbered requirements well and follows constraints.
- **Well-documented.** Millions of people use ChatGPT, so there are tutorials, tips, and troubleshooting guides everywhere. If you get stuck, you can usually find an answer quickly.
- **Fast iteration.** The combination of unlimited messages and fast response times means you can go through the describe-generate-run-observe-iterate loop very quickly.

---

## Free Tier Walkthrough

### Sign Up (2 minutes)

1. Go to [chatgpt.com](https://chatgpt.com)
2. Sign up with email, Google, Microsoft, or Apple account
3. Verify your email — you are ready to go

### What You Get

- **Model:** GPT-4o mini (free), GPT-4o (limited access)
- **Messages:** Unlimited on GPT-4o mini, limited on GPT-4o
- **Code generation:** Full support for Python and other languages
- **File uploads:** You can upload files for analysis

### Limitations

- **Slower during peak times.** Free tier users may experience delays when many people are using the service simultaneously.
- **GPT-4o access is limited.** The most capable model has usage caps on the free tier. For this workshop, GPT-4o mini is sufficient.

---

## Getting Good Code Blocks

### Always specify the language

```
Write a Python script that...
```

This ensures ChatGPT formats the output as a proper code block with syntax highlighting and a copy button.

### If formatting breaks

Sometimes ChatGPT outputs code inline instead of in a block. Say:

```
Please format that as a single Python code block that I can copy.
```

### How to copy code

1. Hover over the code block
2. Click the **Copy code** button that appears in the top-right corner
3. Switch to Replit or Cursor and paste

### If the code is split across multiple blocks

Sometimes ChatGPT explains code in pieces with text in between. Say:

```
Show me the complete code as one single block that I can copy and run. No explanations in between.
```

---

## Conversation Management

### ChatGPT remembers context

Within a single conversation, ChatGPT remembers everything you and it have said. This is how follow-up prompts work — when you say "now add comparison mode," it knows what "the tool" refers to because it sees the entire conversation.

### When to start a new chat

Start a new conversation when:
- You are building a completely different tool
- The conversation has become very long (20+ messages) and responses seem confused
- You want a fresh start after too many failed iterations

### How to keep context fresh

If the conversation gets long and ChatGPT seems to lose track:

```
Here is the current version of my code. Treat this as the ground truth and make changes to it:

[paste the full current code]

Now, [your change request].
```

Pasting the full code resets the context to what you actually have.

---

## Best Prompting Patterns for ChatGPT

### Direct requests work well

ChatGPT responds well to straightforward instructions:

```
Build me a Python command-line tool that calculates RICE scores for feature prioritization.
```

You do not need elaborate preambles. State what you want directly.

### Ask for multiple approaches

```
Show me 3 different approaches for calculating a weighted feature score. For each one, explain the trade-offs.
```

ChatGPT is good at generating alternatives when asked.

### If output is too brief

```
Explain in more detail. Show me the complete code with comments explaining each section.
```

ChatGPT sometimes gives abbreviated answers. Asking for detail gets you a more complete response.

### If output is too long

```
Show me just the function that calculates the score. Nothing else.
```

Narrow the scope when you only need a specific piece.

---

## 5 Example PM Workflows

### 1. Building a Decision Tool

**Prompt:**
```
I'm a product manager. Build me a Python command-line tool that scores feature ideas on Customer Value, Implementation Effort, Strategic Alignment, and Confidence. Use this formula: Score = (CustomerValue×2 + StrategicAlignment×1.5 + Confidence×1) / Effort × 10. Show a recommendation (Go/Maybe/No Go) and an ASCII bar chart. Use Python built-ins only. Keep it under 120 lines.
```

**What to expect:** A code block with the complete tool. Copy it to Replit and run it.

### 2. Analyzing CSV Data

**Prompt:**
```
Write a Python script that reads a CSV called user-data.csv with columns user_id, signup_date, last_active_date. Group users into weekly cohorts and show retention percentages at Week 0 through Week 4. Use only the csv and datetime modules. Show an ASCII table.
```

**What to expect:** A script that processes your CSV. Upload the CSV to Replit, paste the script, and run it.

### 3. Creating a Web Prototype

**Prompt:**
```
Build a Streamlit app that reads metrics.csv (columns: date, active_users, signups, revenue) and shows 4 metric cards with week-over-week changes plus a line chart. Use streamlit and plotly.
```

**What to expect:** A Streamlit app. You will need to install streamlit and plotly in your environment.

### 4. Debugging an Error

**Prompt:**
```
My Python code gives this error:
ValueError: invalid literal for int() with base 10: 'abc'

Here's the code:
[paste code]

Fix it so it handles non-numeric input gracefully. Do not change anything else.
```

**What to expect:** ChatGPT explains the error and provides the fixed code.

### 5. Understanding Code

**Prompt:**
```
I'm a product manager, not a developer. Explain this Python code section by section. For each part, tell me what it does in plain English, what would happen if I removed it, and what I could safely change.

[paste code]
```

**What to expect:** A clear walkthrough with practical guidance on what you can modify.

---

## Free vs Plus Comparison

| Feature | Free | Plus ($20/mo) |
|---|---|---|
| GPT-4o mini | Unlimited | Unlimited |
| GPT-4o | Limited access | Full access |
| Response speed | Standard (slower at peak) | Priority |
| File uploads | Yes | Yes |
| Image generation | Limited | Full |
| Advanced data analysis | Limited | Full |

**Honest take:** The free tier is totally sufficient for this workshop and for regular PM tool building. GPT-4o mini handles Python generation well. Upgrade to Plus only if you hit GPT-4o limits frequently or want faster responses during peak hours.

---

## Tips and Tricks

- **Use ChatGPT for high-volume iteration.** Unlimited messages mean you can try prompt after prompt without worrying about limits. Great for experimentation.
- **Great for debugging loops.** Paste error, get fix, paste next error, get fix. The unlimited messages make this painless.
- **Combine with Claude.** Use Claude for the initial build (better at complex structured prompts) and ChatGPT for rapid iteration and debugging (unlimited messages).
- **Pin important conversations.** Click the three dots next to a conversation and pin it so your tool-building conversations stay at the top of the sidebar.
- **Use custom instructions.** In Settings > Personalization > Custom Instructions, add: "I'm a product manager. When I ask for code, use Python built-ins only, add plain-English comments, and keep it concise." This context applies to every conversation automatically.
- **Regenerate responses.** If you do not like the generated code, click the regenerate button (circular arrow) to get a different version from the same prompt. Sometimes the second attempt is better.
