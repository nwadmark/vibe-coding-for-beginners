# Pre-Work: Do This Before the Workshop

**Time required: 15 minutes**

Complete these steps before the session so you can jump straight into building when the workshop starts.

---

## Why Pre-Work Matters

The workshop moves fast — 60 minutes, three builds. If your tools are set up and tested in advance, you spend all your time building instead of troubleshooting.

---

## Step 1: AI Assistant (Choose One)

You need an AI assistant open in your browser. Pick one below. Both are free.

### Option A: Claude.ai — Recommended

Claude tends to produce cleaner Python code with better comments, which makes the workshop experience smoother.

1. Go to [claude.ai](https://claude.ai) and click **Sign Up**
2. Create an account with your email or Google account
3. Once you are logged in, you should see a chat window
4. Paste this test prompt into the chat:

```
I'm a product manager learning to vibe code.
Write a Python function that calculates NPS
from a list of ratings 0-10. Add comments.
```

5. **What you should see:** Claude responds with a code block (called an Artifact) containing a Python function. The code will have comments explaining each step. You do not need to understand the code — you are confirming Claude can generate it.

**Free tier limits:** Claude.ai's free tier gives you a limited number of messages per day. This resets every few hours. For the workshop, you will send 3-5 prompts total, which fits well within the free tier.

### Option B: ChatGPT — Alternative

ChatGPT is a solid alternative, especially if you already have an account.

1. Go to [chat.openai.com](https://chat.openai.com) and click **Sign Up**
2. Create an account with your email, Google, or Microsoft account
3. Once you are logged in, you should see a chat window
4. Paste this same test prompt into the chat:

```
I'm a product manager learning to vibe code.
Write a Python function that calculates NPS
from a list of ratings 0-10. Add comments.
```

5. **What you should see:** ChatGPT responds with a code block containing a Python function with comments. The code may look slightly different from Claude's — that is normal.

**Free tier limits:** ChatGPT's free tier has usage caps that reset periodically. The 3-5 prompts in the workshop fit within the free tier.

### Claude vs ChatGPT for This Workshop

| | Claude.ai | ChatGPT |
|---|---|---|
| Code quality | Cleaner comments, fewer errors in Python | Good code, occasionally more verbose |
| Copy experience | Artifact panel with one-click copy | Code block with copy button |
| Free tier | Limited messages per day, resets every few hours | Usage cap, resets periodically |
| Best for | This workshop (recommended) | If you already have an account |

**Use both?** Encouraged. If one hits a rate limit, switch to the other. Having both open in separate tabs is a good backup plan.

---

## Step 2: Coding Environment (Choose One)

You need a place to paste and run Python code. Pick one below.

### Option A: Replit — Recommended (Browser-Based)

Replit runs entirely in your browser. There is nothing to install on your computer.

1. Go to [replit.com](https://replit.com) and click **Sign Up**
2. Create an account with your email, Google, or GitHub account
3. Once logged in, click **Create Repl** (or the **+** button)
4. Select **Python** as the template
5. Give it a name like `pm-decision-tool` and click **Create Repl**
6. You should see a code editor on the left and a console on the right
7. Delete any starter code and paste this test:

```python
print("I'm ready to vibe code!")
name = input("What's your name? ")
print(f"Welcome, {name}!")
```

8. Click the green **Run** button at the top
9. **What you should see:** The console prints `I'm ready to vibe code!`, then waits for you to type your name. Type your name, press Enter, and it greets you.

**Free tier limits:** Replit's free tier includes enough compute time for all workshop projects. You get a limited number of Repls, but you only need one for this workshop.

### Option B: Cursor — Optional (Local IDE)

Cursor is a code editor that runs on your computer. Use this if you prefer working locally.

1. Go to [cursor.com](https://cursor.com) and download the installer for your operating system
2. Run the installer and open Cursor
3. Check that Python is available:
   - Open the built-in terminal (View → Terminal or `` Ctrl+` ``)
   - Type `python --version` (or `python3 --version` on Mac/Linux) and press Enter
   - You should see `Python 3.8` or higher
   - If Python is not found, download it from [python.org/downloads](https://python.org/downloads)
4. Create a new file called `test.py`
5. Paste this test:

```python
print("I'm ready to vibe code!")
name = input("What's your name? ")
print(f"Welcome, {name}!")
```

6. Run it from the terminal: `python test.py`
7. **What you should see:** Same output as above — a greeting with your name.

**Free tier limits:** Cursor's free tier includes AI features with a monthly usage cap. The workshop does not require Cursor's AI features (you will use Claude.ai or ChatGPT directly), so the free tier is more than enough.

---

## Step 3: Run the Setup Verification Script

This script checks that your environment has everything the workshop needs.

**Where to find it:** The file is at `setup/verify-setup.py` in the workshop repository.

### Running in Replit

1. In your Repl, create a new file called `verify-setup.py`
2. Copy the contents of `setup/verify-setup.py` from the repository and paste them in
3. Click **Run**

### Running in Cursor

1. Open a terminal in Cursor
2. Navigate to the workshop repository folder
3. Run: `python setup/verify-setup.py`

### What the Output Should Look Like

```
🔍 Vibe Coding for Beginners — Setup Check
=============================================

📌 Python Version
  ✅ Python 3.11.4

📌 Standard Libraries
  ✅ math
  ✅ json
  ✅ datetime
  ✅ random
  ✅ csv
  ✅ os

📌 Optional Libraries
  ℹ️  streamlit (not installed — optional, needed for dashboard projects)
     Install later with: pip install streamlit

=============================================
🎉 You are ready to go! Head to build/01-decision-framework/ to start.
```

All green checkmarks on the required items means you are good. The `ℹ️` on streamlit is fine — that library is only needed for later projects.

### What to Do If Something Fails

- **❌ on Python version:** Your Python is older than 3.8. Download a newer version from [python.org/downloads](https://python.org/downloads).
- **❌ on a standard library:** This is unusual. It means your Python installation may be incomplete. Reinstall Python from [python.org/downloads](https://python.org/downloads).
- **Script won't run at all:** Make sure you are running it with Python 3, not Python 2. Try `python3 setup/verify-setup.py` instead.

---

## The 2-Minute Primer: What Is Vibe Coding?

Read this before the workshop. It will make everything click faster.

### Definition

Vibe coding is building software by describing what you want in plain English and letting an AI coding assistant write the code for you. You focus on *what* the tool should do. The AI figures out *how* to make it work.

### The PM Workflow: Before and After

| Before Vibe Coding | After Vibe Coding |
|---|---|
| Have an idea for an internal tool | Have an idea for an internal tool |
| Write a spec or ticket | Describe it to an AI assistant |
| Wait for engineering availability | AI generates working code in seconds |
| Wait for the build (days to weeks) | Paste the code and run it |
| Review, request changes, wait again | Iterate with follow-up prompts |
| Get the tool weeks later | Have a working prototype in an hour |

### What We Are Building Today

The **PM Decision Framework** — a command-line tool that helps you score and evaluate feature ideas using weighted criteria. You describe a feature, rate it on four dimensions, and the tool calculates a recommendation: Strong Go, Maybe, or No Go.

Why this tool specifically? Because every PM makes prioritization decisions, and this tool turns a subjective process into a structured one. It is useful on day one.

### The Right Mindset

Think of it this way: **you are the PM, the AI is your developer.** You decide what to build and why. The AI handles the implementation. Your job is to write clear requirements (prompts) and evaluate the output — the same skills you already use every day.

### A Note for Non-Technical PMs

You do not need to understand the code the AI writes. You need to understand what the tool *does* — and you will, because you are the one who described it. If something does not work, you describe the problem in plain English and the AI fixes it. That is the entire workflow.

---

## Final Checklist

Before the workshop starts, confirm these five things:

- [ ] AI assistant account created and test prompt returned code
- [ ] Coding environment set up and test code ran successfully
- [ ] `verify-setup.py` passed with green checkmarks on required items
- [ ] Read the 2-minute primer above
- [ ] Laptop charged and ready to go

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Claude hit its free tier limit | Switch to ChatGPT (or vice versa). Having both accounts is a good backup. The limit resets every few hours. |
| Replit won't load or is very slow | Try refreshing the page. If it persists, clear your browser cache or try a different browser (Chrome works best). |
| Python error when running code | Copy the full error message, paste it back into your AI assistant, and ask it to fix the issue. This is part of the workflow. |
| Can't install Python on my computer | Use Replit instead — it runs in your browser and has Python built in. No installation needed. |
| Forgot my password for Claude/ChatGPT/Replit | Use the "Forgot password" link on the login page. Check your spam folder if the reset email does not arrive. |
| Code runs but gives wrong or unexpected output | Paste the code and the output back into your AI assistant and describe what you expected instead. |
| The test prompt gave different code than expected | That is normal. AI assistants generate slightly different code each time. As long as you got a code block with a Python function, you are all set. |
| Slow internet connection | Close other browser tabs and applications. Replit needs a stable connection. If it is too slow, try Cursor (works offline after setup). |

---

You are 15 minutes away from building your first tool. See you at the workshop.
