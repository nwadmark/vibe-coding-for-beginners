---
marp: true
theme: default
paginate: true
---

# Vibe Coding for Beginners

**Build your first AI-powered PM tool.**
**No coding experience required.**

<!--
Speaker notes:
Welcome everyone. Today you are going to build a working PM tool from scratch using AI. It does not matter if you have never written a line of code — by the end of this session, you will have a tool you built yourself.
-->

---

# What You Will Build Today

**The PM Decision Framework**

A command-line tool that:
- Takes a feature idea as input
- Scores it on 4 criteria (1-10 each)
- Calculates a weighted decision score
- Recommends: **Go**, **Maybe**, or **No Go**
- Suggests a PM action for each outcome

<!--
Speaker notes:
This is a real tool you can use in your day-to-day work. Every time you need to evaluate whether a feature is worth building, you run this tool. By the end of today, it will be yours.
-->

---

# Who Is in the Room?

**Raise your hand if...**

You have written code before?

You have never written code and are a little nervous right now?

<!--
Speaker notes:
Get a read on the room. Count hands for each. Reassure the non-technical group: this workshop is designed for you. Acknowledge the technical group: you will find new workflow patterns here. Both groups will walk out with the same working tool.
-->

---

# What Is Vibe Coding?

Building software by **describing what you want** in plain English.

```
    DESCRIBE  →  GENERATE  →  RUN  →  OBSERVE  →  ITERATE
       ↑                                              │
       └──────────────────────────────────────────────┘
```

**You** write the prompts. **AI** writes the code.

<!--
Speaker notes:
Vibe coding is not about learning to program. It is about using AI as your developer. You describe what you want — the same way you write a product spec or a Jira ticket — and the AI turns that description into working software. Then you test it, refine it, and repeat.
-->

---

# Why PMs Specifically?

| Before Vibe Coding | After Vibe Coding |
|---|---|
| Write a spec | Describe it to AI |
| Wait for engineering | Code generated in seconds |
| Wait for the build | Paste and run |
| Review → request changes → wait | Iterate with follow-up prompts |
| **Weeks** | **Minutes** |

<!--
Speaker notes:
PMs are perfect for this. Vibe coding requires defining clear requirements, setting acceptance criteria, and iterating on output. That is literally your job description. The skill is not coding. The skill is writing good requirements. You already have that skill.
-->

---

# How Today Works

**Three loops. Same pattern each time.**

| Loop | What Happens | Time |
|---|---|---|
| 1. Generate | Build the base tool from one prompt | 10 min |
| 2. Improve | Add visual bars and labels | 15 min |
| 3. Customize | Choose your own feature to add | 10 min |

Then: **Ship** → **Reflect** → **Next Steps**

<!--
Speaker notes:
Each loop follows the same cycle: describe, generate, run, observe, iterate. Loop 1 gets you a working tool. Loop 2 makes it better. Loop 3 makes it yours. We will ship it at the end and talk about what comes next.
-->

---

# [LIVE DEMO] Prompt #1

The full prompt is in your **participant guide — Part 2, Loop 1**.

It describes a Decision Framework tool that:
- Asks for a feature idea
- Scores it on 4 weighted criteria
- Calculates a recommendation
- Suggests a PM action

**Copy the prompt. Paste it into Claude or ChatGPT. Hit send.**

<!--
Speaker notes:
Share the prompt in the chat as well. Give participants about a minute to paste it. Walk them through what is happening: the AI is reading their requirements and writing Python code to match. Remind them — they do not need to understand the code. They need to understand what they asked for.
-->

---

# [LIVE DEMO] Copy → Paste → Run

**Three steps:**

1. **Copy** the code from your AI assistant
2. **Paste** it into Replit (or Cursor)
3. **Click Run**

Try evaluating:
*"Add one-click checkout to ShopFlow mobile app"*

<!--
Speaker notes:
Demo this live on your screen. Copy from Claude, paste into Replit, click Run. Enter the ShopFlow feature with scores 8, 6, 7, 5. Show the output. Then tell them to do the same. Give 3-4 minutes for everyone to get their tool running.
-->

---

# When Things Break

**Errors are normal.** Every developer sees them constantly.

The fix:
1. Copy the error message
2. Paste it into your AI assistant
3. Say: *"I got this error. Fix it."*
4. Copy the fixed code, paste, run again

**That is the workflow.** Errors are part of the iterate step.

<!--
Speaker notes:
Normalize errors. This is critical for non-technical participants. If someone gets an error, they may think they did something wrong. Reassure them: errors happen to everyone. The fix is mechanical — paste the error, ask the AI, try again. Demo an error fix live if you can.
-->

---

# [LIVE DEMO] Prompt #2 — Improve

Add three things to the tool:

1. **Labels** after each input (Low / Medium / High / Maximum)
2. **Visual bars** showing each score:
   ```
   Customer Value    ████████░░  8/10
   Strategic Align   ███████░░░  7/10
   ```
3. **Separator lines** between evaluations

Paste Prompt #2 in the **same conversation**.

<!--
Speaker notes:
Emphasize: same conversation, not a new one. The AI needs context from Prompt #1. Paste Prompt #2 in the chat. After they run it, point out: you wrote a change request. Three features to add, keep everything else. That is a product spec. The skill transfers directly.
-->

---

# [LIVE DEMO] Prompt #3 — Your Choice

**Pick one:**

| Option | What It Adds |
|---|---|
| **A — Decision Log** | Saves evaluations to a file for future reference |
| **B — Comparison Mode** | Evaluate multiple features, see a ranked table |
| **C — Custom Criteria** | Replace scoring criteria with your team's priorities |

**This is your product decision.** The AI builds. You choose what.

<!--
Speaker notes:
This is the most important slide conceptually. They are making a product decision — which feature adds the most value for their use case. The AI is the developer. They are the PM. Let them choose and give 8-10 minutes to build.
-->

---

# Ship It

**In Replit:** Click **Share** → copy the link → post it in the chat.

**In Cursor:** Take a screenshot → share it.

**Show us what you built.**

<!--
Speaker notes:
Give 2 minutes for sharing. React to links and screenshots that come in. Call out interesting ones. This is a celebration moment — everyone in the room built a working tool.
-->

---

# What Just Happened?

Three questions to think about:

1. **What surprised you?**
2. **Where did you steer?** What product decisions did *you* make?
3. **What would you build next?**

<!--
Speaker notes:
Pause for 30 seconds of quiet thinking. Then ask for one or two volunteers to share. Listen for moments of surprise and ownership. Frame the takeaway: you walked in as a PM who does not code. You are walking out as a PM who builds.
-->

---

# Six Things to Build Next

| Tool | What It Does | Time |
|---|---|---|
| Feature Prioritizer | RICE, MoSCoW, custom ranking | 30-45 min |
| Cohort Analyzer | User retention patterns | 30-45 min |
| A/B Test Calculator | Sample size and significance | 20-30 min |
| Pricing Calculator | Pricing tiers and revenue models | 30-45 min |
| Feedback Analyzer | Theme extraction from feedback | 30-45 min |
| Metric Dashboard | Visualize key product metrics | 45-60 min |

<!--
Speaker notes:
These are all in the build/ folder of the repo. Each one stands on its own — same format as today. Point them to the participant guide's Next Steps section for links and reading recommendations.
-->

---

# Resources

| Resource | What It Is |
|---|---|
| `theory/` | Deeper dive into vibe coding concepts |
| `prompts/` | Copy-paste prompt library |
| `guides/` | Reference guides for tools and debugging |
| `capstone/` | Optional bigger challenge |
| `community/` | Share your builds, see what others made |

**Everything is in the repo. Keep building.**

<!--
Speaker notes:
Quick walkthrough — do not dwell here. Point out the prompts library as especially useful for their next builds. Mention the capstone for anyone who wants a bigger challenge. Remind them the community folder is for sharing.
-->

---

# Q&A

**Ask anything.**

- Can I use this at work?
- Is the free tier really enough?
- What if I do not understand the code?
- What comes after this workshop?

<!--
Speaker notes:
Open the floor. Refer to the facilitator guide for standard answers to common questions. Keep answers short and practical. If a question goes deep, offer to follow up after the session. End on time — respect the clock.
-->
