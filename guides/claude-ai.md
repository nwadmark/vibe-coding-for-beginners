# Claude.ai Guide

Claude is an AI assistant made by Anthropic. It is the recommended AI tool for this workshop because of its structured output, Artifacts feature, and PM-friendly explanations.

---

## What Makes Claude Good for PMs

- **PM-friendly explanations.** Claude writes code with clear variable names and plain-English comments. When you ask it to explain something, it adjusts for a non-developer audience.
- **Artifacts.** Claude displays generated code in a side panel called an Artifact. You can view, edit, and copy code separately from the conversation — no scrolling through chat to find the code block.
- **Projects.** You can create a Project with persistent context (like your product name, team criteria, or tool preferences). Every conversation in that project inherits that context automatically.
- **Strong at Python generation.** Claude reliably produces working Python code from structured prompts. It follows numbered requirements closely and respects constraints like "Python built-ins only."

---

## Free Tier Walkthrough

### Sign Up (2 minutes)

1. Go to [claude.ai](https://claude.ai)
2. Sign up with your email or Google account
3. Verify your email — you are ready to go

### What You Get

- **Model:** Claude Sonnet 4 (fast, capable, good at code)
- **Messages:** Approximately 30-50 messages per day (varies by message length)
- **Features:** Full access to Artifacts and basic Projects
- **File uploads:** You can upload files for Claude to analyze

### How to Check Remaining Messages

When you are running low, Claude shows a notice near the input box: "You've used most of your free messages." There is no exact counter, but you will see the warning before you run out.

### When Messages Reset

Usage limits reset periodically. If you hit the cap, wait a few hours or switch to ChatGPT to continue working while the limit resets.

---

## Using Artifacts for Coding

### What Artifacts Are

When Claude generates code, it appears in a panel on the right side of the screen (desktop) or in a separate tab (mobile). This is an Artifact — a live, editable code block separate from the conversation.

### How to Copy Code from Artifacts

1. Look at the Artifact panel on the right
2. Click the **Copy** button in the top-right corner of the Artifact
3. Switch to Replit or Cursor and paste (Ctrl+V / Cmd+V)

### How to Edit Code Directly in Artifacts

You can click into an Artifact and edit the code directly. This is useful for small changes — like updating a threshold from 15 to 20, or changing a label. For larger changes, write a follow-up prompt instead.

### How to Create New Artifacts

Claude creates Artifacts automatically when it generates code. If you want a fresh Artifact (instead of modifying an existing one), say: "Create a new version of the tool with these changes." Claude will generate a new Artifact while keeping the previous one available.

### Save Your Code

Artifacts are tied to your conversation. If you lose access to the conversation, you lose the Artifact. Always copy your finished code to Replit or a local file.

---

## Using Projects for PM Work

### When to Use Projects

Use Projects when you are building multiple tools around the same product or working on a tool over several sessions. Projects give Claude persistent context so you do not need to re-explain your product, criteria, or preferences in every conversation.

### How to Create a Project

1. Click **Projects** in the left sidebar
2. Click **New Project**
3. Name it something like "PM Tools" or "ShopFlow Tools"
4. Add project knowledge (see below)

### What to Put in Project Knowledge

Add a short context block that describes your situation:

```
I'm a PM at ShopFlow, a B2B e-commerce platform.

Our team prioritizes features using these criteria:
- Customer Value (weight: 2x)
- Revenue Impact (weight: 1.5x)
- Strategic Alignment (weight: 1x)
- Implementation Effort (denominator)

We use Python for internal tools. Python built-ins only, no pip install.
Output should be formatted for pasting into Slack or Notion.
```

### How Conversations Inherit Context

Every new conversation you start inside the project automatically has access to the project knowledge. You can jump straight into "Build me a pricing calculator" without re-explaining who you are or what tools you use.

---

## Best Prompting Patterns for Claude

### Start with your role

```
I'm a product manager. Build me a...
```

This one line changes how Claude writes code — clearer variable names, PM-oriented output labels, and explanations pitched at a non-developer audience.

### Use numbered lists for requirements

```
The tool should:
1. Ask for feature name
2. Score on 4 criteria
3. Calculate weighted score
```

Claude treats numbered lists as a checklist and is less likely to skip items.

### Ask for extensive comments

```
Add plain-English comments explaining each section.
```

Claude will add comments that explain what the code does in terms you understand.

### If Claude is too cautious

Sometimes Claude adds caveats or asks for clarification instead of generating code. If you are confident about what you want:

```
I understand the limitations. Please proceed and generate the complete code.
```

---

## 5 Example PM Workflows

### 1. Building a Decision Tool

**Prompt:**
```
I'm a PM at ShopFlow. Build me a command-line tool that scores feature ideas on Customer Value, Revenue Impact, Strategic Alignment, and Implementation Effort. Use the weighted formula: (CV×2 + RI×1.5 + SA×1) / Effort × 10. Show a recommendation and bar chart. Python built-ins only.
```

**Expected output:** An Artifact with a complete Python script. Copy it to Replit, run it, and score your features.

### 2. Analyzing CSV Data

**Prompt:**
```
I have a CSV file with columns: user_id, signup_date, last_active_date. Build me a Python script that reads this file and shows retention by weekly cohort. Use only the csv and datetime modules.
```

**Expected output:** An Artifact with a script. Upload your CSV to Replit, run the script, and see a retention table.

### 3. Creating a Web Prototype

**Prompt:**
```
Build me a Streamlit dashboard that shows 4 metric cards (active users, signups, revenue, retention) with week-over-week deltas. Read data from metrics.csv. Use streamlit and plotly.
```

**Expected output:** An Artifact with a Streamlit app. Requires pip install — best run in Cursor or a Replit with Streamlit configured.

### 4. Debugging an Error

**Prompt:**
```
My code throws this error:
TypeError: unsupported operand type(s) for +: 'int' and 'str'

Here's the code: [paste code]

Fix the error. Explain what went wrong. Do not change any other logic.
```

**Expected output:** Claude explains the error in plain English and provides the corrected Artifact.

### 5. Understanding Code

**Prompt:**
```
Explain this code to me like I'm a PM, not a developer. For each function, tell me: what it does, why it's there, and what I could change safely.

[paste code]
```

**Expected output:** A section-by-section walkthrough in plain English with concrete examples.

---

## Free vs Pro Comparison

| Feature | Free | Pro ($20/mo) |
|---|---|---|
| Model | Claude Sonnet 4 | Claude Sonnet 4 + Opus 4 |
| Messages per day | ~30-50 | Much higher limits |
| Artifacts | Yes | Yes |
| Projects | Basic | Full (more project knowledge) |
| File uploads | Yes | Yes, larger files |
| Priority access | No | Yes (no waiting during peak) |

**Honest take:** The free tier is enough for this workshop and for building PM tools regularly. Upgrade to Pro if you hit message limits frequently or want access to the most powerful model (Opus) for complex tasks.

---

## Tips and Tricks

- **Continue a conversation later.** Your conversations are saved in the left sidebar. Click any previous conversation to continue where you left off. Claude remembers the full context.
- **Share Artifacts.** Click the Share button on an Artifact to get a link. Anyone with the link can view the code — useful for sharing with teammates.
- **Organize chats.** Rename conversations by clicking the title. Use names like "Decision Framework v2" or "RICE Calculator" so you can find them later.
- **Upload files.** Drag a CSV or text file into the chat. Claude can read it and write code that processes it. Useful for building tools around your actual data.
- **Use keyboard shortcuts.** Press `/` to focus the input box. Press `Enter` to send. Press `Shift+Enter` for a new line within your message.
