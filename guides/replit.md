# Replit Guide

Replit is a browser-based code editor and runtime. It is the recommended code editor for this workshop because it requires zero installation — you open a browser tab, paste code, and click Run.

---

## Why Replit for Beginners

- **Zero installation.** No Python download, no terminal setup, no PATH configuration. Everything runs in the browser.
- **Works on any device.** Chromebook, iPad, old laptop, library computer — if it has a browser, it runs Replit.
- **Automatic saving.** Your code is saved as you type. No "forgot to save" disasters.
- **One-click sharing.** Click Share, copy the link, and anyone can see and run your code.
- **Built-in Python environment.** Python is pre-installed. You can run scripts immediately without any setup.

---

## Getting Started

### Sign Up (2 minutes)

1. Go to [replit.com](https://replit.com)
2. Sign up with email, Google, or GitHub account
3. You are ready to create your first project

### Creating Your First Repl

1. Click **Create Repl** (or the **+** button)
2. Search for **Python** in the template list
3. Name it something like `decision-framework`
4. Click **Create Repl**

### Understanding the Interface

```
┌─────────────┬──────────────────────────────┐
│             │                              │
│   Files     │       Code Editor            │
│   Panel     │       (main.py)              │
│             │                              │
│  main.py    │                              │
│  + New file │                              │
│             ├──────────────────────────────┤
│             │                              │
│             │       Console                │
│             │       (output appears here)  │
│             │                              │
│             │  > Click here to type input  │
│             │                              │
└─────────────┴──────────────────────────────┘
                    [ ▶ Run ]  [ Share ]
```

- **Left:** Files panel — your project files
- **Center top:** Code editor — where you write or paste code
- **Center bottom:** Console — where output appears and where you type input
- **Top:** Run button (green) and Share button

---

## Running Python Code

### The basic workflow

1. Write or paste code into `main.py` in the editor
2. Click the green **Run** button at the top
3. See output in the Console panel at the bottom
4. If the program asks for input, click in the Console and type your answers

### How to stop a running program

- Click the **Stop** button (the Run button turns into a Stop button while code is running)
- Or press `Ctrl+C` in the Console

### Replacing code with a new version

When the AI gives you updated code (Prompt #2, Prompt #3):

1. Click in the code editor
2. Select all: `Ctrl+A` (Windows/Linux) or `Cmd+A` (Mac)
3. Paste the new code: `Ctrl+V` / `Cmd+V`
4. Click **Run**

---

## Working with Files

### Creating new files

1. Click the **+** icon in the Files panel (or right-click in the Files panel)
2. Choose **New File**
3. Name it (e.g., `sample-data.csv` or `decision_log.txt`)

### Organizing into folders

1. Click the **+** icon in the Files panel
2. Choose **New Folder**
3. Drag files into the folder

### Uploading files (CSV, TXT)

If you have a data file to analyze:

1. Click the three dots (**...**) at the top of the Files panel
2. Click **Upload File**
3. Select your CSV or TXT file from your computer
4. The file appears in the Files panel and your code can read it

### Downloading files

If your tool creates output files (like `decision_log.txt`):

1. Click the file in the Files panel
2. Click the three dots next to the filename
3. Click **Download**

---

## Installing Packages (If Needed)

### Most PM tools use built-ins

The tools in this workshop are designed to use Python's built-in modules only. You do not need to install anything for Builds 01 through 06.

### If you need an external package

Build 07 (Metric Dashboard) uses Streamlit, pandas, and plotly. To install:

1. In the Files panel, look for a file called `requirements.txt` (or create one)
2. Add the package names, one per line:
   ```
   streamlit
   pandas
   plotly
   ```
3. Replit automatically detects `requirements.txt` and installs the packages when you run the code

### If auto-install does not work

Open the Console and type:

```
pip install streamlit pandas plotly
```

Press Enter and wait for the installation to finish.

---

## Sharing Your Work

### Share a link

1. Click the **Share** button in the top right
2. Copy the link
3. Share it in the workshop chat, Slack, or email

Anyone with the link can view your code and run it in their browser.

### Important: Free tier means public

On the free tier, all your Repls are public. Anyone with the link can see the code. Do not put sensitive data (API keys, real customer data, passwords) in a free Repl.

### Sharing during the workshop

When the facilitator asks you to share your work:

1. Click **Share**
2. Copy the link
3. Paste it in the workshop chat

---

## Free vs Pro Comparison

| Feature | Free | Replit Core ($7/mo) |
|---|---|---|
| Public Repls | Unlimited | Unlimited |
| Private Repls | No | Yes |
| Storage | 500 MB | 50 GB |
| CPU/RAM | Basic (0.5 vCPU) | More power |
| Always-on Repls | No | Yes |
| Custom domains | No | Yes |

**When to upgrade:** Only if you need private projects (e.g., working with real company data) or more computing power. The free tier is sufficient for everything in this workshop and for ongoing PM tool building.

---

## Common Issues and Fixes

| Problem | Solution |
|---|---|
| Repl will not load or is stuck | Refresh the page. Try a different browser (Chrome works best). Clear browser cache if needed. |
| My code disappeared | Click the clock icon (Version History) in the top menu. You can restore any previous version. |
| Output not showing | Make sure you are looking at the **Console** panel (bottom section). If it is collapsed, drag the divider up. |
| Input not working | Click **inside the Console panel** to type your answers. Do not type in the code editor — that changes the code. |
| Package will not install | Check that `requirements.txt` has the correct package name (one per line, no extra characters). Try `pip install [package]` in the Console. |
| Slow performance | The free tier has limited CPU. If code is very slow, try reducing the data size or switch to Cursor for local execution. |
| "Unexpected indent" error | The code may have mixed tabs and spaces from copy-paste. Select all code (Ctrl+A), delete it, and paste again carefully. |
| File not found error | Make sure the file (CSV, TXT) is in the same directory as `main.py`. Check the Files panel to verify the filename matches exactly what the code expects. |
| Repl auto-stops | Free tier Repls go to sleep after inactivity. Click Run again to restart. Your code is saved — you will not lose anything. |
