# v0 by Vercel Guide

> **Advanced / Paid Tool** — v0 has a limited free tier and a paid plan for full access. It is not required for this workshop. This guide is for participants who want polished UI components for their prototypes.

---

## What v0 Is

v0 is an AI-powered UI component generator made by Vercel. You describe a component in plain English, and v0 generates production-quality React code with modern styling using Tailwind CSS and shadcn/ui.

- **Component generation.** v0 builds individual UI components — not full applications. Think: a pricing table, a dashboard card, a data table, a form.
- **React and Next.js specific.** The output is React code using modern libraries. If you are building with React, the components drop directly into your codebase.
- **Beautiful by default.** v0 generates polished, professional-looking components. The design quality is high without any design input.
- **Copy-paste into your codebase.** Each generated component comes with all the code you need to use it.

---

## When PMs Use v0

- **Need polished UI components for a prototype.** You are building a Streamlit or web app and want one piece of it to look production-quality.
- **Creating mockups for stakeholder presentations.** You need a realistic-looking table, chart, or form to include in a deck or document.
- **Exploring design patterns.** You want to see what a feature could look like before committing to a design direction.
- **Building a component library.** You are collecting reusable UI pieces for your team's prototyping toolkit.

---

## How It Differs from Lovable

| Aspect | v0 | Lovable |
|---|---|---|
| Scope | Individual components | Full applications |
| Output | React code you copy-paste | Deployed web apps |
| Design quality | Very high | High |
| Database/backend | No | Yes |
| Deployment | You handle it | Automatic |
| Best for | UI pieces, mockups | Full prototypes |

**v0 builds the bricks. Lovable builds the house.** Use v0 when you need one beautiful component. Use Lovable when you need a working application.

---

## How It Differs from Vibe Coding

| Aspect | Vibe Coding (Workshop) | v0 |
|---|---|---|
| Output | Python command-line tools | React UI components |
| Language | Python | JavaScript/TypeScript (React) |
| Runs where | Terminal or Replit | Browser (needs React setup) |
| Learning curve | Low (copy, paste, run) | Moderate (need React environment) |
| Best for | Internal tools, data analysis | Visual prototypes, UI design |

For this workshop, vibe coding is the right tool. v0 becomes useful when you need a visual frontend for something you prototyped as a command-line tool.

---

## Example PM Use Case

**The situation:** Alex built a feature prioritization tool as a Python script. Now the team wants a visual version they can use in sprint planning meetings.

**What Alex did:**

1. Used v0 to generate a "feature prioritization table component" — described it as: "A sortable data table with columns for Feature Name, RICE Score, Priority tier (High/Medium/Low with colored badges), and an Action button. Include a search bar and filter dropdowns."

2. v0 generated a polished React component with sorting, colored badges, and a clean design.

3. Alex shared a screenshot of the generated component in the sprint planning channel to show what the tool could look like as a web app.

4. Engineering used the v0 component as a starting point for the production implementation.

**Total time:** 15 minutes to generate and refine the component.

---

## Free vs Paid

| Feature | Free | Premium ($20/mo) |
|---|---|---|
| Generations per month | 10 | 1500+ |
| Component quality | Full | Full |
| Export code | Yes | Yes |
| Private generations | No | Yes |
| Priority access | No | Yes |

The free tier gives you enough to try it out — 10 generations per month. If you use it regularly for prototyping, the paid tier removes the cap.

---

## Getting Started

1. Go to [v0.dev](https://v0.dev)
2. Sign in with your Vercel account (or create one — free)
3. Type a description of the component you want in the prompt box
4. Review the generated component in the preview
5. Click **Code** to see the React source code
6. Copy the code into your project or save a screenshot for reference

**Tip for PMs:** Even if you do not have a React project, v0 is useful for generating realistic screenshots. Describe the component, take a screenshot of the preview, and use it in your presentations or PRDs.

---

## How It Complements This Workshop

- **Workshop builds the logic.** You use vibe coding to figure out the scoring formula, the data flow, and the output format.
- **v0 builds the UI.** Once you know what the tool should do, you describe the visual interface to v0 and get a production-quality component.
- **Together they cover both halves.** Logic (Python command-line) + Interface (React component) = a complete picture of what the product feature could be.

This is a natural progression: build the tool in the workshop, then use v0 to visualize what the production version might look like.
