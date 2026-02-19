# Cursor Guide

Cursor is a code editor with AI built in. It is a fork of VS Code — the most popular code editor in the world — with added AI features for generating, editing, and understanding code. Use Cursor if you want a local development setup with files on your computer.

---

## What Cursor Is

- **VS Code fork.** If you have used VS Code, Cursor feels identical. All the same shortcuts, extensions, and layout.
- **AI built in.** Generate code, edit existing code, and ask questions — all without leaving the editor.
- **Free tier available.** 50 premium AI requests per month (Ctrl+K and Ctrl+L), plus 2000 autocomplete suggestions.
- **Local development.** Your files live on your computer, not in the cloud. Private by default.

---

## Who Should Use Cursor

- **Technical PMs** who are comfortable installing software and running terminal commands
- **People coding regularly** who want a professional IDE, not just a learning environment
- **Anyone who wants private projects** — files are on your machine, not public like free Replit
- **Those familiar with VS Code** — the transition is seamless

If you have never used a code editor before, start with Replit instead. Cursor has a learning curve that Replit does not.

---

## Installation and Setup

### Download and Install (5 minutes)

1. Go to [cursor.com](https://cursor.com)
2. Download the installer for your operating system (Mac, Windows, or Linux)
3. Install it like any application (drag to Applications on Mac, run installer on Windows)
4. Open Cursor and sign up for a free account

### Python Setup

Cursor needs Python installed on your computer to run Python scripts.

**Mac:** Python 3 is pre-installed on modern macOS. Open Terminal and type `python3 --version` to verify.

**Windows:** Download Python from [python.org](https://python.org). During installation, check the box that says **"Add Python to PATH"** — this is important. After installation, open Command Prompt and type `python --version` to verify.

**Linux:** Open Terminal and run `sudo apt install python3` (Ubuntu/Debian) or `sudo dnf install python3` (Fedora).

---

## AI Features Overview

Cursor has three main AI features:

### Ctrl+K / Cmd+K — Quick AI Edit

Select code (or place your cursor on an empty line) and press `Ctrl+K`. A prompt box appears. Type what you want and the AI edits the code in place.

**Example:** Select a function and type "Add input validation to this function." The AI modifies the selected code directly.

### Ctrl+L / Cmd+L — AI Chat Panel

Opens a chat panel on the right side. You can have a conversation with the AI about your code. It can see your open files.

**Example:** Open your decision tool and press `Ctrl+L`. Type "Add a comparison mode to this tool." The AI generates the updated code in the chat. You can then apply it.

### Tab — AI Autocomplete

As you type, Cursor suggests completions. Press `Tab` to accept a suggestion. This is powered by AI and is context-aware — it reads your file and suggests relevant code.

### @ Mentions — Reference Specific Files

In the chat panel (Ctrl+L), type `@filename` to tell the AI to look at a specific file. Useful when your project has multiple files.

---

## Using Cursor for PM Tools

### Create a project folder

1. Create a folder on your computer called `pm-tools`
2. In Cursor, go to **File > Open Folder** and select it
3. This becomes your workspace

### Create a new file

1. In the Explorer panel (left sidebar), click the **New File** icon
2. Name it `decision_tool.py`
3. Paste your generated code into the file
4. Save: `Ctrl+S` / `Cmd+S`

### Run the file

**Option 1: Right-click**
- Right-click in the editor
- Click **Run Python File in Terminal**

**Option 2: Terminal**
- Open the terminal: `` Ctrl+` `` (backtick)
- Type: `python3 decision_tool.py` (Mac/Linux) or `python decision_tool.py` (Windows)
- Press Enter

### Generate code with AI

1. Open an empty file
2. Press `Ctrl+K`
3. Paste your workshop prompt (e.g., the full Prompt #1)
4. Press Enter — the AI generates code directly in the file
5. Press `Ctrl+S` to save
6. Run it

---

## Free Tier Limits

| Feature | Free | Pro ($20/mo) |
|---|---|---|
| Autocomplete (Tab) | 2000 suggestions/month | Unlimited |
| AI requests (Ctrl+K, Ctrl+L) | 50 premium requests/month | 500 requests/month |
| Model | GPT-4o mini and Claude Sonnet | GPT-4o, Claude Sonnet, and more |
| Local files | Unlimited | Unlimited |
| Privacy | Files stay on your machine | Files stay on your machine |

**Is the free tier enough?** For the workshop and occasional tool building, yes. The 50 premium requests cover about 2-3 tool-building sessions. If you code daily with AI assistance, you will want Pro.

---

## Cursor vs Replit

| Aspect | Cursor | Replit |
|---|---|---|
| Setup time | 10 min (download + Python install) | 2 min (browser only) |
| Where files live | Your computer | Cloud (Replit servers) |
| Sharing | Copy file or push to GitHub | One-click share link |
| Privacy | Private by default | Public on free tier |
| AI integration | Built into editor (Ctrl+K, Ctrl+L, Tab) | Separate AI tab |
| Offline use | Yes (except AI features) | No (requires internet) |
| Best for | Ongoing development, private projects | Quick starts, sharing, beginners |

**Bottom line:** Start with Replit if you are new. Move to Cursor when you want a permanent local setup or need private projects.

---

## Tips for PM Use

- **Use alongside Claude.ai.** Use Claude's chat for complex prompts and long conversations. Use Cursor's Ctrl+K for quick inline edits. They complement each other well.
- **Create templates.** Save a blank template file for each tool type (decision framework, RICE calculator, etc.) so you can quickly start new variants.
- **Use Ctrl+P to find files.** Press `Ctrl+P` and start typing a filename. This is the fastest way to navigate projects with multiple files.
- **Terminal access.** Press `` Ctrl+` `` to open the integrated terminal. Run scripts, install packages (`pip install streamlit`), and manage files without leaving the editor.
- **Version control.** Cursor has built-in Git support. Use it to track changes to your tools over time. The Source Control panel (left sidebar, branch icon) shows what has changed.
- **Split the editor.** Drag a file tab to the right side of the editor to view two files side by side. Useful when comparing versions or referencing one file while editing another.
