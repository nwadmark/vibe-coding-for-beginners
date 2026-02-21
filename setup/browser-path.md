# Getting Set Up (Browser Only)

**Time: 15 minutes. You only need a web browser and an email address.**

This page walks you through setting up everything you need for the workshop. You will create two free accounts and test that both work. Every step tells you exactly what to click and what you will see on screen.

No software to download. No special skills needed. If you can use Gmail, you can do this.

---

## What You Are Setting Up

You need two browser tabs open for the workshop:

1. **Claude.ai** — This is where you type descriptions of what you want to build. It writes code for you.
2. **Replit** — This is where you paste the code and run it. Think of it like Google Docs, but for code.

That is it. Two tabs.

---

## Part 1: Set Up Claude.ai

### Create your account

1. Open a new browser tab
2. Go to **claude.ai**
3. You will see a page with a large "Start for free" or "Sign Up" button. Click it.
4. You will see options to sign up with Google, email, or other accounts. **Pick whichever is easiest for you.** Google is the fastest — one click and you are in.
5. If you chose email, check your inbox for a verification message. Click the link inside it.
6. You will see a chat screen with a text box at the bottom that says something like "How can I help you today?" — this means you are logged in and ready.

### Test that it works

7. Click inside the text box at the bottom of the screen
8. Copy and paste this exact text into the box:

```
I'm a product manager learning to vibe code.
Write a Python function that calculates NPS
from a list of ratings 0-10. Add comments.
```

9. Press **Enter** (or click the arrow/send button to the right of the text box)
10. Wait about 10 seconds

**What you will see:** A response appears with a block of code. The code block has a slightly different background color (usually gray or dark) and looks like this kind of thing:

```
def calculate_nps(ratings):
    # Count promoters, passives, and detractors
    ...
```

You do not need to understand what this code means. You are just confirming that Claude can write code when you ask it to.

11. Look for a **Copy** button somewhere near the code block. It might be in the top-right corner of the code area, or it might be a small clipboard icon. Click it to confirm you can copy the code. You will need this during the workshop.

**You are done with Claude.ai setup.** Leave this tab open.

### If something went wrong

| What you see | What to do |
|---|---|
| The sign-up page asks for a phone number | This is normal for verification. Enter your phone number. You will get a text message with a code. |
| You signed up but see "you've reached your limit" | This means you somehow used up free messages. Wait a few hours — the limit resets on its own. Or go to **Part 1B** below and set up ChatGPT as a backup. |
| The page is loading forever | Refresh the page. If it still does not load, try a different browser (Chrome works best). |
| You do not see a code block in the response | Claude might have just written a text explanation. Try again — paste the same prompt and add "Show me the code" at the end. |

---

## Part 1B: Set Up ChatGPT (Backup)

This is optional but recommended. If Claude runs out of free messages during the workshop, you can switch to ChatGPT and keep going.

1. Open a new browser tab
2. Go to **chatgpt.com**
3. Click **Sign up**
4. Create an account with Google, email, Microsoft, or Apple. Same idea as Claude — pick the easiest option.
5. Once logged in, you will see a chat screen similar to Claude's
6. Paste the same test prompt:

```
I'm a product manager learning to vibe code.
Write a Python function that calculates NPS
from a list of ratings 0-10. Add comments.
```

7. Press **Enter** and wait
8. You should see a code block in the response, just like with Claude

**If it works, you have a backup ready.** You can close this tab for now and open it during the workshop if needed.

---

## Part 2: Set Up Replit

### Create your account

1. Open a new browser tab
2. Go to **replit.com**
3. You will see a homepage with a **Sign Up** button (usually top right). Click it.
4. Sign up with Google, GitHub, or email. Google is fastest.
5. After signing in, you will land on a home screen or dashboard

### Create your first project

6. Look for a button that says **Create Repl** or a **+** button. It is usually near the top left or in the center of the screen. Click it.
7. You will see a popup or page asking you to choose a template. **Type "Python" in the search box** and select the **Python** template.
8. You will see a field asking for a name. Type: `pm-decision-tool`
9. Click **Create Repl** (or **Create** — the blue/green button at the bottom of the popup)

### Understand what you are looking at

10. You will now see a screen split into sections. Here is what each part is:

```
┌──────────────┬────────────────────────────────┐
│              │                                │
│  FILES       │     EDITOR                     │
│  (left side) │     (big area in the middle)   │
│              │                                │
│  You'll see  │     This is where you paste    │
│  "main.py"   │     code. It looks like a      │
│  listed here │     text document.              │
│              │                                │
│              ├────────────────────────────────┤
│              │                                │
│              │     CONSOLE                    │
│              │     (bottom area)              │
│              │                                │
│              │     This is where your         │
│              │     program's output shows up. │
│              │     You also type answers here │
│              │     when the program asks you  │
│              │     questions.                 │
│              │                                │
└──────────────┴────────────────────────────────┘
        [ ▶ Run button at the very top ]
```

- **Left panel (Files):** You will see a file called `main.py` listed here. That is where your code lives.
- **Middle panel (Editor):** This is where you paste code. It might already have some starter text in it.
- **Bottom panel (Console):** This is where you will see results when your code runs. **Important:** During the workshop, when the program asks you a question (like "What is the feature name?"), you click inside this bottom panel and type your answer here.
- **Top of the screen:** Look for a green **Run** button. This is the most important button — it runs your code.

### Test that it works

11. Click inside the editor (the big middle area). If there is already some text there, select all of it:
    - **Windows/Chromebook:** Press `Ctrl` and `A` at the same time
    - **Mac:** Press `Cmd` and `A` at the same time
12. Delete the selected text (press the `Delete` or `Backspace` key)
13. Copy this text and paste it into the editor:

```python
print("I'm ready to vibe code!")
name = input("What's your name? ")
print(f"Welcome, {name}! You're all set for the workshop.")
```

14. Click the green **Run** button at the top
15. **What you will see in the bottom panel (Console):**

```
I'm ready to vibe code!
What's your name?
```

16. Click inside the **bottom panel** (the Console area). You will see a blinking cursor.
17. Type your name and press **Enter**
18. **What you will see:**

```
I'm ready to vibe code!
What's your name? Alex
Welcome, Alex! You're all set for the workshop.
```

If you see your name in the welcome message, Replit is working perfectly.

### If something went wrong

| What you see | What to do |
|---|---|
| You cannot find the "Create Repl" button | Look for a **+** button in the top-left area. On some screens it says "Create" instead of "Create Repl." |
| You do not see the Console (bottom panel) | The Console might be collapsed (hidden). Look for a small bar at the bottom of the editor area. Try dragging it upward to reveal the Console. |
| You clicked Run but nothing happened | Make sure your code is in the file called `main.py` (check the tab above the editor). If it says something else, click on `main.py` in the Files panel on the left. |
| You see red text that says "SyntaxError" or "IndentationError" | The code might not have pasted correctly. Select all the text in the editor (Ctrl+A or Cmd+A), delete it, and paste the test code again carefully. Make sure no extra spaces or characters snuck in. |
| You see "What's your name?" but cannot type | You need to click **inside the Console** (the bottom panel) before typing. If you click in the editor (middle panel) instead, you will be typing code, not answering the question. |
| The page is very slow or unresponsive | Refresh the page. Your code is saved automatically — you will not lose anything. If it is still slow, close other browser tabs. |
| It says "This Repl is sleeping" | Free Repls go to sleep when you are not using them. Just click **Run** again and it will wake up. |

---

## Part 3: Test Them Together

This is a dry run of the exact workflow you will use in the workshop. It takes 2 minutes.

1. **Go to your Claude.ai tab.** Paste this into the chat:

```
Write a Python program that asks the user for their favorite color and prints "Great choice! [color] is a wonderful color." Use only print and input.
```

2. **Wait for Claude to respond.** You will see a code block in the response.
3. **Copy the code.** Click the Copy button on the code block.
4. **Go to your Replit tab.** Click inside the editor (middle panel).
5. **Select all** the text that is already there (Ctrl+A or Cmd+A) and **delete** it.
6. **Paste** the new code (Ctrl+V or Cmd+V).
7. Click the green **Run** button.
8. You will see a question in the Console asking for your favorite color. **Click inside the Console** and type a color. Press Enter.
9. **What you will see:** A message like "Great choice! Blue is a wonderful color."

**If that worked, you just did vibe coding.** You described what you wanted, Claude wrote the code, you pasted it into Replit, and it ran. That is the entire workshop workflow.

---

## You Are Done

Here is your checklist. If all four boxes are true, you are ready for the workshop:

- [ ] Claude.ai account works — you pasted a prompt and got a code block back
- [ ] Replit account works — you pasted code, clicked Run, and saw output
- [ ] You tested them together — you copied code from Claude into Replit and ran it
- [ ] You know where the Console is in Replit and how to click inside it to type answers

**Leave both tabs open on workshop day.** You will switch back and forth between them throughout the session.

---

## Quick Reference for Workshop Day

| When the facilitator says... | You do this |
|---|---|
| "Copy the prompt" | Select the prompt text from the participant guide, copy it (Ctrl+C or Cmd+C) |
| "Paste it into Claude" | Click in the Claude chat box, paste (Ctrl+V or Cmd+V), press Enter |
| "Copy the code" | Click the Copy button on the code block in Claude |
| "Paste it into Replit" | Go to Replit, select all in the editor (Ctrl+A), paste (Ctrl+V) |
| "Run it" | Click the green **Run** button at the top of Replit |
| "Type your answer" | Click inside the **Console** (bottom panel in Replit), type your answer, press Enter |
| "My code has an error" | Copy the red error text from the Console, go back to Claude, paste it, and say "fix this error" |

---

## Still Stuck?

If something is not working and you cannot figure it out from the troubleshooting tables above:

1. Take a screenshot of what you see on your screen
2. Show it to the facilitator at the start of the workshop — they will help you get set up in the first few minutes

Do not worry. The most common issues take less than a minute to fix, and the facilitator has seen them all before.
