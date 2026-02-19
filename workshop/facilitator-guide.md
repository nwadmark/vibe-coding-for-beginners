# Facilitator Guide

Everything you need to run the Vibe Coding for Beginners workshop. This guide is written for someone running it for the first time — follow it section by section and you will be fine.

---

## Before the Session

### 1 Week Before

- [ ] Send the [pre-work](pre-work.md) link to all participants with a note: "Complete this 15-minute setup before the workshop"
- [ ] Confirm the room or virtual meeting link (Zoom, Google Meet, etc.)
- [ ] Test the projector or screen-share setup
- [ ] Do a full dry run of the build yourself — complete all three prompts end to end
- [ ] Prepare a backup Replit account in case you need to demo from scratch
- [ ] Create a shared chat channel (Slack, Teams, or meeting chat) for sharing links during the session

### 1 Day Before

- [ ] Send a reminder: "Workshop tomorrow — make sure pre-work is done"
- [ ] Open your demo environment and verify everything runs
- [ ] Pre-load Prompt #1 in a text file on your desktop so you can paste it quickly
- [ ] Test your screen share — make sure the font size is large enough (18pt minimum in the editor)
- [ ] Charge your laptop fully

### Day Of

- [ ] Arrive 15 minutes early (or open the meeting room early)
- [ ] Open your demo environment with the finished tool ready to run
- [ ] Open Claude.ai (or ChatGPT) in a separate tab, logged in
- [ ] Open the [participant guide](participant-guide.md) in a tab so you can reference prompt text
- [ ] Open the shared chat and post: "Welcome! Open the participant guide: [link]"
- [ ] Have the [pre-work](pre-work.md) link ready for anyone who did not complete it
- [ ] Set a timer visible to yourself (phone or second screen)

### How to Set Up Your Demo Environment

1. Create a Replit account (or use your existing one)
2. Create a new Python Repl called `demo-decision-tool`
3. Build the tool yourself by completing all three prompts
4. Save the final version — this is what you demo during the Hook
5. Also save a blank version (empty file) — this is what you use to demo the live build
6. Have both Repls open in separate tabs: the finished version and the blank one

---

## The Run Sheet

### 00:00–00:05 — HOOK (5 minutes)

**What you're doing:** Running the finished tool live to show participants what they are about to build.

**Setup:** Share your screen showing the finished Decision Framework tool in Replit.

**Script:**

> *Run the tool on your shared screen without narrating. Enter a feature name and scores while the room watches in silence. Let the result appear.*
>
> *Pause. Let them read the output.*
>
> "I didn't write a single line of code to build that. You're going to build it yourself today. In about 60 minutes."
>
> *Pause for effect.*
>
> "Quick show of hands — who here would describe themselves as technical? Knows some programming?"
>
> *Count hands.*
>
> "And who would say: I've never written code and I'm a little nervous right now?"
>
> *Count hands. Smile.*
>
> "Perfect. This workshop is designed for both of you. By the end, everyone in this room will have a working tool they built themselves."

---

### 00:05–00:15 — ORIENTATION (10 minutes)

**What you're doing:** Teaching the vibe coding concept and explaining how the session works.

**Script — What is vibe coding:**

> "So what is vibe coding? It's building software by describing what you want in plain English and letting an AI write the code."
>
> "Here is how a PM's workflow changes. Before vibe coding: you have an idea, you write a ticket, you wait for engineering, you wait for the build, you review it, you request changes, you wait again. That can take weeks."
>
> "After vibe coding: you have an idea, you describe it to an AI assistant, it generates code in seconds, you paste it and run it, and you iterate with follow-up prompts. You can have a working prototype in under an hour."
>
> "We are not replacing engineers. We are giving PMs the ability to build prototypes, internal tools, and proof-of-concepts without waiting in the engineering queue."

**Script — Why PMs specifically:**

> "PMs are actually the perfect people for this. Think about what vibe coding requires: you need to describe what a tool should do clearly, define inputs and outputs, set acceptance criteria, and iterate based on results. That's your job description."
>
> "The skill is not coding. The skill is writing good requirements. And you already know how to do that."

**Script — How today works:**

> "We are going to go through three loops. Each loop follows the same pattern: you describe what you want, the AI generates code, you paste it, you run it, and you observe the result."
>
> "Loop 1 — Generate: We build the base tool from scratch. You will paste one prompt and get a working decision framework."
>
> "Loop 2 — Improve: We add visual score bars and input labels. This is like iterating on a feature."
>
> "Loop 3 — Customize: You pick one of three options to make the tool your own. This is where you make product decisions."
>
> "Everyone has the participant guide open? Good. That has all the prompts and instructions you will need."

**Script — Tool check:**

> "Quick check. Raise your hand if you have your AI assistant open — Claude or ChatGPT."
>
> *Wait for hands. Help anyone who does not.*
>
> "Raise your hand if you have Replit or Cursor open and ready."
>
> *Wait for hands. Help anyone who does not.*
>
> "If you did not finish the pre-work, pair up with someone next to you and we will get you set up in the first couple of minutes. For everyone else — we are starting."

---

### 00:15–00:20 — FIRST PROMPT (5 minutes)

**What you're doing:** Getting everyone to paste Prompt #1 and watch the AI generate code.

**Script — Sharing the prompt:**

> "Open your participant guide and scroll to Part 2, Loop 1. You will see Prompt #1 in a box."
>
> "I'm also pasting it in the chat right now."
>
> *Paste Prompt #1 into the shared chat.*
>
> "Copy that entire prompt. Every word matters — it's your specification. Then paste it into Claude or ChatGPT and hit send."
>
> "Do that now. I'll give you a minute."

**Script — The "watch what happens" moment:**

> *Wait about 30-60 seconds. Walk around or watch the chat.*
>
> "Is the AI generating code? You should see it writing Python — lines of code appearing in real time."
>
> "Do not worry about understanding the code. Focus on the structure: do you see sections that match what you asked for? Score inputs, a calculation, a recommendation?"
>
> "The AI is reading your requirements and building exactly what you described."

**Script — "You wrote code" reaction:**

> "When it finishes, take a look at the result. The AI generated 80 to 120 lines of Python from one paragraph of plain English."
>
> "You did not write code. You wrote a product spec. The AI did the engineering. That's the core idea."

---

### 00:20–00:35 — BUILD (15 minutes)

**What you're doing:** Walking everyone through copy, paste, run, and handling first errors.

**Script — Copy, paste, run demo:**

> "Now let's get this running. Follow the steps in the participant guide."
>
> "In Claude, click the Copy button on the code artifact. In ChatGPT, hover over the code block and click Copy Code."
>
> "Switch to Replit. Select all the existing code — Ctrl+A or Cmd+A — delete it, and paste the new code."
>
> "Click Run."
>
> *Demo this on your screen with the blank Repl while you talk.*
>
> "I'm doing it right now on my screen. Watch — I paste the code, I click Run, and the tool starts asking me questions."

**Script — The first error moment:**

> "Now — some of you may see an error instead of the tool running. A red message in the console. That's completely normal."
>
> "Errors are part of the process. Even experienced developers see errors constantly. This does not mean you did something wrong."
>
> "If you see an error, here is what to do: copy the entire error message, go back to your AI assistant, paste it, and say: 'I got this error when I ran the code. Fix it.' The AI will give you corrected code."
>
> "That's the workflow. Describe, generate, run, observe, iterate. Errors are part of the iterate step."
>
> *Give the room 3-4 minutes to get their tools running. Walk around and help people who are stuck.*

**Script — Fixing it together:**

> *If several people have the same error:*
>
> "I'm seeing a few people hit the same issue. Let me fix it on screen so everyone can see."
>
> *Paste the error into your AI assistant on the shared screen. Show the fix process in real time.*

**Script — Celebrating first working build:**

> "Raise your hand when your tool is running and you have evaluated at least one feature."
>
> *Wait for most hands to go up.*
>
> "Look around the room. Everyone here has a working Python tool they built in the last 10 minutes. No programming courses. No bootcamps. You described what you wanted, and it exists."

---

### 00:35–00:50 — ITERATE (15 minutes)

**Script — Introducing Prompt #2:**

> "Now we are going to improve the tool. Scroll to Loop 2 in the participant guide."
>
> "Prompt #2 adds three things: labels that appear after each score input, visual bars that show your scores as a chart, and separator lines between evaluations."
>
> "Paste Prompt #2 in the same conversation in your AI assistant. Do not start a new conversation — the AI needs the context from Prompt #1."
>
> *Paste Prompt #2 in the chat as well.*
>
> "Same cycle: copy the new code, replace everything in your editor, and run it."

**Script — "This is a PRD" insight:**

> "Look at what Prompt #2 says. It says: add these features, keep existing logic, add these three things only."
>
> "That's a feature spec. That's what you put in a Jira ticket. The format is slightly different, but the skill — defining what to build, what to keep, and what to change — is exactly the same."
>
> "Vibe coding is not about learning a new skill. It's about applying a skill you already have in a new context."

**Script — Loop 3 options introduction:**

> "For Loop 3, you get to choose. Scroll to Loop 3 in the participant guide. There are three options:"
>
> "Option A: Add a decision log — the tool saves every evaluation to a file so you can review past decisions."
>
> "Option B: Add comparison mode — evaluate multiple features and see them ranked in a table."
>
> "Option C: Custom criteria — replace the default scoring criteria with your team's specific priorities."
>
> "Pick the one that sounds most useful to you. There is no wrong choice."
>
> *Give the room 8-10 minutes to work through Loop 3.*

**Script — Calling out interesting customizations:**

> *Walk around and notice what people chose. Call out interesting examples:*
>
> "I see someone over here added comparison mode and is ranking three features against each other — that's a prioritization meeting in your terminal."
>
> "Someone else customized the criteria to match their team's OKRs. That's exactly the kind of ownership we are talking about."

---

### 00:50–01:00 — SHIP + REFLECT (10 minutes)

**Script — Share your work moment:**

> "You have a working tool. Time to ship it. If you're in Replit, click Share and copy the link. If you're in Cursor, take a screenshot of the tool running."
>
> "Drop your link or screenshot in the chat. I want to see what everyone built."
>
> *Give 2 minutes for sharing. React to a few that come in.*

**Script — The 3 reflection questions:**

> "Before we wrap up, I want you to think about three things. You do not have to share — but think about your answers."
>
> "First: What surprised you? Was there a moment where the AI did something you did not expect?"
>
> "Second: Where did you steer? Think about a decision you made that shaped the tool. The AI wrote the code, but you drove the product."
>
> "Third: What would you build next? If you had another hour, what tool would you describe?"
>
> *Pause for 30 seconds. Then ask for one or two volunteers to share.*

**Script — The mindset shift framing:**

> "Here is what I want you to take away from today. You walked in as a PM who does not code. You're walking out as a PM who builds."
>
> "That does not mean you're an engineer now. It means you have a new tool in your toolkit. When you need a quick analysis, a prototype, or an internal tool — you can build it yourself in an hour instead of waiting weeks."
>
> "The boundary matters too. These tools are great for prototyping, internal use, and personal utilities. Shipping to production still needs engineering. But the gap between idea and prototype shrunk from weeks to minutes today."

---

### 01:00–01:10 — NEXT STEPS + Q&A (10 minutes)

**Script — Previewing next builds:**

> "The participant guide has a Next Steps section with six more tools you can build on your own. A Feature Prioritizer, Cohort Analyzer, A/B Test Calculator, Pricing Calculator, Feedback Analyzer, and Metric Dashboard."
>
> "Each one is a standalone project in the build folder. Same format as today — prompts, instructions, and expected output."

**Script — Resource walkthrough:**

> "Three things to check out after this session. The theory folder has deeper material on vibe coding concepts. The prompts folder has a library of copy-paste prompts for common patterns. And the guides folder has reference material for Replit, Cursor, and debugging."
>
> "There is also an optional capstone project if you want a bigger challenge."

**Standard Answers for Common Questions:**

**"Can I use this at work?"**
> "Yes — these tools are designed for PM work. The Decision Framework, Feature Prioritizer, and others are all tools you can use in your day-to-day. Be aware of your company's AI usage policies, especially regarding proprietary data in prompts."

**"Is the free tier really enough?"**
> "For everything in this workshop, yes. The free tiers of Claude, ChatGPT, and Replit cover all seven projects. You only need a paid tier if you want higher rate limits or advanced features like Claude's Projects or Cursor's AI autocomplete."

**"What if I don't understand the code?"**
> "You do not need to. Focus on what the tool does, not how it works under the hood. If something breaks, describe the problem to the AI and it will fix it. That said, over time you will naturally start recognizing patterns — and that understanding is a bonus, not a requirement."

**"How is this different from just using ChatGPT?"**
> "You're using ChatGPT — or Claude — but in a structured way. The difference is the workflow: writing prompts as product specs, iterating like you would on a feature, and building tools that persist and run independently. It's the difference between having a conversation and building a product."

**"What about Cursor, Lovable, v0?"**
> "Those are all great tools. Cursor is included as an option in this workshop. Lovable and v0 are better for building web apps with visual interfaces. This workshop focuses on command-line tools because they require zero setup and let you focus on the prompting skill. Once you're comfortable with that skill, tools like Lovable and v0 are a natural next step."

**"What comes after this workshop?"**
> "Three paths. One: build more tools from the reference library. Two: read the theory material to deepen your understanding. Three: try the capstone project for a bigger challenge. And if you build something interesting, submit it to the community showcases."

---

## Troubleshooting During the Session

### Half the room cannot get Replit working

> "If Replit is not loading, try a different browser — Chrome tends to work best. If it's still not working, pair up with someone who has it running and share a screen. You can both paste prompts and one person runs the code. We will troubleshoot your setup after the session."

*If the problem is widespread, switch to a live-coding demo format: you type on screen, everyone watches, and they can build on their own afterward.*

### Different AI outputs from different participants

> "Everyone's code will look slightly different. AI assistants generate unique code each time. That's expected. As long as your tool asks for scores and gives a recommendation, you're on track. The exact variable names and formatting do not matter."

### Running behind schedule

| Behind By | What to Cut |
|---|---|
| 5 minutes | Shorten the reflection to one question instead of three |
| 10 minutes | Skip Loop 3 — go straight from Loop 2 to Ship + Reflect |
| 15 minutes | Skip Loop 3 and Next Steps — go from Loop 2 to a quick share and wrap |
| 20+ minutes | Stop after Loop 1, demo Loop 2 live, and send participants the guide to finish on their own |

### Group moving fast

Stretch goals for groups that finish early:
- Try a second Prompt #3 option (they already did one)
- Start building `02-feature-prioritizer` from the self-paced library
- Challenge: modify the scoring formula and explain why their formula is better
- Challenge: combine two Prompt #3 options (e.g., comparison mode + decision log)

### Non-technical group feeling overwhelmed

> "Take a breath. You're doing great. Remember — you're not writing code. You're writing descriptions of what you want. The AI handles the code part."
>
> "If something is not working, that's not your fault. Copy the error, paste it to the AI, and ask it to fix it. That's the workflow for everyone, including experienced developers."

*Slow down the pace. Do each step on screen first, then have them follow. Consider pairing non-technical participants with someone further along.*

### Technical group feeling bored

> "If you're finding this comfortable, good — use the extra time to push further. Try combining multiple Prompt #3 options. Or open the prompts library and build something completely custom. The capstone project in the repo is designed as a bigger challenge if you want it."

*Give technical participants permission to go off-script. They will produce interesting showcases.*

---

## Post-Session

### Post-Session Checklist

- [ ] Save any links or screenshots shared in the chat
- [ ] Send a follow-up message to participants with: the repo link, the participant guide link, and a reminder of the next steps section
- [ ] Collect showcases — ask participants to share their finished tools or screenshots in the community channel
- [ ] Note which questions came up during Q&A for the FAQ below
- [ ] Write a brief retrospective: what worked, what to adjust for next time

### How to Update the FAQ Based on Questions Asked

After each session, review the questions that came up during Q&A. If a question was asked by multiple participants or required a long explanation, add it to:
1. The troubleshooting table in [pre-work.md](pre-work.md)
2. The Stuck? table in [participant-guide.md](participant-guide.md)
3. The common questions section above in this guide

Keep the language conversational and the answers short. If a question reveals a gap in the materials, update the relevant section directly.

### How to Collect Showcases

1. Create a thread or channel for showcases after the session
2. Ask participants to share: a screenshot or Replit link, which Prompt #3 they chose, and one sentence about what they would build next
3. With permission, add notable showcases to the `community/showcases/` folder in the repo
