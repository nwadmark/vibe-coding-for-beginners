# Frequently Asked Questions

Practical answers to the most common questions from workshop participants.

---

### 1. Is the free tier really enough?

Yes. Claude.ai free gives you enough messages for 2-3 tool-building sessions per day. ChatGPT free gives you unlimited messages. Replit free runs all the Python code in this workshop. You might hit Claude's message cap during an intensive session — if so, switch to ChatGPT to keep working. Hundreds of participants have completed this workshop entirely on free tiers.

---

### 2. Will I need to keep paying for tools after the workshop?

No. Every tool in this workshop runs on free tiers. The only paid tools mentioned (Lovable, v0, Cursor Pro) are optional extras for people who want to go further. You can build and use PM tools indefinitely with Claude free + Replit free.

---

### 3. I am not technical at all. Can I really do this?

Yes. This workshop is designed for people who have never written a line of code. You do not write code — you write prompts in plain English, the AI writes the code, and you paste it into an editor that runs it. The skills you need are PM skills: describing requirements clearly, testing output against expectations, and iterating based on feedback.

---

### 4. What if I do not understand the code?

That is fine. You do not need to understand the code to use the tools. You need to understand the *output* — does the score look right? Does the recommendation make sense? If you want to learn more about what the code does, use the explanation prompts in [prompts/explain.md](../prompts/explain.md). Understanding grows naturally over time.

---

### 5. Can I use this at work? What about sensitive data?

You can use the tools at work for internal analysis. However, be careful with data: do not paste proprietary data, customer PII, or confidential information into Claude or ChatGPT unless your company's AI usage policy allows it. For sensitive data, either use anonymized/sample data in your prompts or run the tools locally with Cursor (files stay on your machine).

---

### 6. How is this different from just using ChatGPT?

You probably already use ChatGPT for writing and brainstorming. Vibe coding is different because the output is *executable* — it is a working program, not text. You get a tool that takes input, runs calculations, and produces structured output. The workshop teaches you a specific methodology: describe, generate, run, observe, iterate. That loop is what makes vibe coding reliable and repeatable.

---

### 7. Do I need to know Python?

No. The prompts tell the AI to use Python, and the AI handles the syntax. You do not need to read, write, or understand Python. Over time, you will start recognizing patterns in the generated code — which helps you write better prompts — but it is not a prerequisite.

---

### 8. What if the AI gives me wrong code?

This is normal and expected. The AI generates code that *usually* works, but sometimes it has bugs. When that happens: (1) copy the error message, (2) paste it back into the AI with "fix this error," and (3) the AI corrects it. Most errors are fixed in one round. The [debug prompts](../prompts/debug.md) give you templates for common error types.

---

### 9. How long until I can build things independently?

Most participants can build simple tools independently after the workshop plus 2-3 self-paced builds. That is roughly 3-5 hours of total practice. You will not be an expert — but you will be comfortable with the loop and able to build tools for your own use without following a guide.

---

### 10. What is the difference between Cursor and Replit?

Replit runs in your browser with zero setup — best for beginners and quick projects. Cursor is a desktop application with AI built into the editor — best for ongoing development and private projects. Start with Replit. Move to Cursor when you want files on your own computer or need private projects. See the full comparison in [guides/cursor.md](../guides/cursor.md).

---

### 11. Should I use Claude or ChatGPT?

Either works for this workshop. Claude is better at following complex structured prompts and has the Artifacts feature (a side panel for code). ChatGPT has unlimited free messages, which is great for rapid iteration. Many participants use both: Claude for the initial build, ChatGPT for debugging and iteration. Try both and see which you prefer.

---

### 12. How do I know when to upgrade to paid tools?

Upgrade when a free tier limit blocks your workflow. If you hit Claude's message cap regularly, consider Claude Pro. If you need private projects in Replit, consider Replit Core. If you code with AI daily, consider Cursor Pro. For this workshop and occasional tool building, free tiers are sufficient. Do not pay preemptively.

---

### 13. What comes after this workshop?

Three paths: (1) Build the 6 self-paced projects in the `build/` folder to practice the vibe coding loop with different tool types. (2) Attempt the optional [capstone project](../capstone/) to build something for your real job. (3) Start building your own tools from scratch using the [prompts library](../prompts/) as a starting point. Most participants follow path 1 first, then jump to path 3 when they feel confident.

---

### 14. Can I run this workshop with my team?

Yes. Everything you need is in this repository. The [facilitator guide](../workshop/facilitator-guide.md) has a minute-by-minute run sheet, talking points, and troubleshooting tips. The workshop is designed for 6-30 participants and takes 60-70 minutes. All you need is a room (or Zoom), a screen to share slides, and participants with free Claude + Replit accounts set up beforehand.
