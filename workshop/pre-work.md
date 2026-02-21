# Pre-Work: Do This Before the Workshop

**Time required: 15 minutes. You can do this from your couch.**

Complete these three steps before the session so you can jump straight into building when the workshop starts. Each step tells you exactly what to do, what you will see, and what to do if something does not look right.

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

**If that worked, great!** You asked an AI to write code and it did. That is the first half of vibe coding. If it did not work, don't worry — check the [troubleshooting table](#troubleshooting) at the bottom of this page before moving on.

---

## Step 2: Coding Environment (Choose One)

Now you need a place to paste that code and run it. Pick one below. **If you are new to this, pick Replit** — it runs in your browser and there is nothing to install.

### Option A: Replit — Recommended (Browser-Based)

Replit runs entirely in your browser. There is nothing to install on your computer.

1. Go to [replit.com](https://replit.com) and click **Sign Up**
2. Create an account with your email, Google, or GitHub account
3. Once logged in, click **Create Repl** (or the **+** button)
4. Select **Python** as the template
5. Give it a name like `pm-decision-tool` and click **Create Repl**
6. You should see a screen split into panels — a code editor (the big area where you paste code) and a console at the bottom (where you will see output and type answers)
7. If there is any starter code already in the editor, select all of it (Ctrl+A on Windows, Cmd+A on Mac) and delete it. Then paste this test:

```python
print("I'm ready to vibe code!")
name = input("What's your name? ")
print(f"Welcome, {name}!")
```

8. Click the green **Run** button at the top
9. **What you should see:** The bottom panel prints `I'm ready to vibe code!`, then waits for you to type your name. **Click inside the bottom panel**, type your name, press Enter, and it greets you.

**Free tier limits:** Replit's free tier includes enough compute time for all workshop projects. You only need one Repl for this workshop.

**Stuck here?** This is the #1 place people get stuck during pre-work. Here is exactly what to do:
- If you do not see output after clicking Run, make sure your code is in the file called `main.py` (check the tab above the editor)
- If you see red text with an error, select all the code (Ctrl+A or Cmd+A), delete it, and paste the test code again — sometimes extra spaces sneak in during copy-paste
- If the program asks "What's your name?" but you cannot type, click **inside the bottom panel** (the console) first, then type
- For anything else, check the [troubleshooting table](#troubleshooting) at the bottom of this page

### Option B: Cursor — Optional (For Experienced Users)

Cursor is a code editor that runs on your computer. **If you are new to coding, skip this and use Replit above.** Cursor is for people who already have some experience with code editors or want files saved locally.

1. Go to [cursor.com](https://cursor.com) and download the installer for your operating system
2. Run the installer and open Cursor
3. Check that Python is available:
   - In Cursor, go to **View → Terminal** to open a text panel at the bottom of the screen
   - Copy and paste this into that panel: `python --version` (on Mac/Linux, try `python3 --version` instead) and press Enter
   - You should see `Python 3.8` or higher printed back
   - If you see an error instead, download Python from [python.org/downloads](https://python.org/downloads)
4. Create a new file called `test.py`
5. Paste this test:

```python
print("I'm ready to vibe code!")
name = input("What's your name? ")
print(f"Welcome, {name}!")
```

6. Copy and paste this into the text panel at the bottom: `python test.py` and press Enter
7. **What you should see:** Same output as with Replit — a greeting with your name.

**Free tier limits:** Cursor's free tier includes AI features with a monthly usage cap. The workshop does not require Cursor's AI features (you will use Claude.ai or ChatGPT directly), so the free tier is more than enough.

---

## Step 3: Verify Everything Works

This step checks that everything is set up correctly. If you see green checkmarks, you are ready. If you see red marks, scroll down to troubleshooting — it is almost always a quick fix.

**Where to find the check script:** The file is at `setup/verify-setup.py` in the workshop repository.

### If you are using Replit

1. In your Repl, click the **+** icon in the Files panel (left side) to create a new file
2. Name it `verify-setup.py`
3. Open `setup/verify-setup.py` from the repository, select all the code, and copy it
4. Paste it into your new `verify-setup.py` file in Replit
5. Make sure the `verify-setup.py` tab is selected (click it above the editor if needed)
6. Click the green **Run** button

### If you are using Cursor

1. Open the text panel at the bottom of Cursor (View → Terminal)
2. Copy and paste this into the panel: `python setup/verify-setup.py` and press Enter

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

=============================================
🎉 You are ready to go! Head to build/01-decision-framework/ to start.
```

**If you see all green checkmarks (✅) on Python Version and Standard Libraries, you are ready.** That is the only thing that matters here.

The `ℹ️` on streamlit is completely fine — ignore it. That library is only needed for one advanced project later, and you can deal with it then.

### What to Do If You See Red Marks (❌)

Don't panic — these are fixable:

- **❌ on Python version:** Your Python is older than 3.8. Download a newer version from [python.org/downloads](https://python.org/downloads). If you are using Replit, this should not happen — Replit has a recent Python version built in.
- **❌ on a standard library:** This is unusual and means your Python installation may be incomplete. If you are using Replit, try creating a fresh Repl. If you are using Cursor, reinstall Python from [python.org/downloads](https://python.org/downloads).
- **Nothing happens when you click Run:** Make sure the `verify-setup.py` tab is selected in the editor (not `main.py`). In Replit, the Run button runs whichever file is currently open.

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

The **PM Decision Framework** — an interactive tool that helps you score and evaluate feature ideas using weighted criteria. You describe a feature, rate it on four dimensions, and the tool calculates a recommendation: Strong Go, Maybe, or No Go.

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

If something goes wrong, find your situation in this table. Every one of these has happened to other participants — you are not the first, and the fix is almost always quick.

| What happened | What to do |
|---|---|
| Claude says you have reached your limit | Switch to ChatGPT (or vice versa). Having both accounts is a good backup. The limit resets on its own every few hours. |
| Replit will not load or is very slow | Refresh the page. If it is still slow, try a different browser (Chrome works best) or close other tabs to free up memory. |
| You see red text with an error after clicking Run | This is normal — it happens to everyone, including experienced developers. Copy the full red text, paste it into Claude or ChatGPT, and say "fix this error." That is the standard workflow. |
| You cannot get Python working on your computer | Use Replit instead. It runs in your browser and has Python built in. No installation or setup needed. |
| You forgot your password for Claude, ChatGPT, or Replit | Click "Forgot password" on the login page. Check your spam folder if the reset email does not arrive within a minute. |
| The code runs but the output looks wrong | Paste the code and the output back into your AI assistant and describe what you expected instead. The AI will figure out the difference and fix it. |
| The test prompt gave different code than expected | That is normal. AI assistants generate slightly different code each time. As long as you got a block of code (you will recognize it by the different background color), you are all set. |
| Your internet is slow and Replit keeps freezing | Close other browser tabs and applications. Replit needs a stable connection. If it is still too slow, try again at a different time of day when your connection is stronger. |

---

**You did it.** If you got through these three steps, you are ready for the workshop. The hardest part is behind you — from here on, it is all building.

See you at the workshop.
