# PM Use Cases for Vibe Coding

You built a Decision Framework tool in the workshop. Now what? This document maps out the concrete ways product managers can use vibe coding in their day-to-day work — beyond the workshop, with your real data and your real problems.

---

## The Three Categories

PM vibe coding use cases fall into three buckets:

| Category | What It Means | Examples |
|---|---|---|
| **Analysis tools** | Scripts that process data and surface insights | Cohort retention, feedback sentiment, metric trends |
| **Decision tools** | Interactive tools that structure your thinking | Feature scoring, prioritization frameworks, pricing models |
| **Workflow tools** | Utilities that automate repetitive PM tasks | Status report generators, data formatters, template creators |

---

## Analysis Tools

### Cohort Retention Analyzer

**The problem:** You have user data in a CSV and want to see retention by signup cohort. Doing this in a spreadsheet is tedious and error-prone.

**What to build:** A script that reads a CSV with `user_id`, `signup_date`, and `last_active_date`, groups users into weekly or monthly cohorts, and displays a retention table.

**Prompt starting point:** See [Build 03: Cohort Analyzer](../build/03-cohort-analyzer/)

**Where the data comes from:** Export from your analytics tool (Amplitude, Mixpanel, or even a database query).

---

### Feedback Sentiment Sorter

**The problem:** You have 200 pieces of user feedback from a survey, NPS, or support tickets. You need to find the patterns.

**What to build:** A script that reads feedback from a text file, classifies each line as positive/neutral/negative using keyword matching, and shows the distribution with sample quotes from each category.

**Prompt starting point:** See [Build 06: Feedback Analyzer](../build/06-feedback-analyzer/)

**Real-world enhancement:** After the basic version works, add a "topics" layer — count mentions of specific features (e.g., "onboarding," "search," "export") to see which areas get the most feedback.

---

### Survey Results Summarizer

**The problem:** You ran a survey with quantitative ratings and open-text responses. You need a quick summary.

**What to build:** A script that reads survey CSV data, calculates averages and distributions for numeric questions, and groups free-text responses by theme.

**Prompt starting point:**
```
Build me a Python tool that reads survey-results.csv with columns:
respondent_id, q1_rating (1-5), q2_rating (1-5), q3_text (free text)

Show:
- Average and distribution for each rating question
- A bar showing how many gave each rating (1-5)
- For text responses, count the 10 most common words (ignoring "the", "a", "is", etc.)

Use Python built-ins only.
```

---

## Decision Tools

### Feature Prioritization (RICE, MoSCoW, or Custom)

**The problem:** You have 10 feature ideas and need to rank them for the next quarter.

**What to build:** An interactive tool that scores each feature on your team's criteria and produces a ranked list. The workshop Decision Framework is one version of this; the RICE calculator in Build 02 is another.

**Prompt starting point:** See [Build 02: Feature Prioritizer](../build/02-feature-prioritizer/)

**Real-world enhancement:** Add an export feature that saves the ranked list as a Markdown table you can paste directly into a planning document or Confluence page.

---

### Pricing Scenario Modeler

**The problem:** You are considering changing your pricing tiers and need to model the revenue impact.

**What to build:** An interactive tool that takes tier names, prices, and customer counts, then shows MRR/ARR with a what-if mode to test changes.

**Prompt starting point:** See [Build 05: Pricing Calculator](../build/05-pricing-calculator/)

**Real-world enhancement:** Add a "scenario comparison" mode that lets you save two or three pricing models and compare them side by side.

---

### A/B Test Planning Calculator

**The problem:** You want to run an A/B test but need to know how long it will take to reach statistical significance.

**What to build:** A calculator that takes your baseline conversion rate, minimum detectable effect, and daily traffic, then tells you the sample size needed and estimated test duration.

**Prompt starting point:** See [Build 04: A/B Test Calculator](../build/04-ab-calculator/)

**Real-world enhancement:** Add a multi-scenario view that shows sample sizes at 90%, 95%, and 99% confidence so you can discuss trade-offs with your team.

---

### Go/No-Go Decision Checklist

**The problem:** Before launching a feature, you need to verify that a set of criteria are met — legal review, localization, analytics instrumentation, etc.

**What to build:** An interactive checklist tool that walks through your launch criteria, flags any that are not complete, and produces a summary with a go/no-go recommendation.

**Prompt starting point:**
```
Build me a Python tool that walks through a launch readiness checklist.

The checklist:
1. Legal review complete? (yes/no)
2. Localization ready? (yes/no)
3. Analytics instrumented? (yes/no)
4. Performance benchmarked? (yes/no)
5. Rollback plan documented? (yes/no)
6. Stakeholders notified? (yes/no)

After all questions:
- If all yes: 🟢 Ready to launch
- If 1-2 no: 🟡 Launch with caveats — show which items are missing
- If 3+ no: 🔴 Not ready — show blockers

Save the checklist result to launch_check.txt with today's date.
Use Python built-ins only.
```

---

## Workflow Tools

### Weekly Status Report Generator

**The problem:** Every week you write the same status report with metrics, accomplishments, and next steps. You spend 30 minutes formatting it.

**What to build:** A tool that asks for this week's key metrics, accomplishments, and blockers, then formats them into your team's report template.

**Prompt starting point:**
```
Build me a Python tool that generates a weekly PM status report.

Ask for:
1. Product area name
2. 3 key metrics with current and previous values
3. Up to 5 accomplishments this week (enter blank to stop)
4. Up to 3 blockers (enter blank to stop)
5. Up to 3 priorities for next week (enter blank to stop)

Output a formatted report:
- Metric table with deltas (▲ or ▼ with percentage change)
- Bulleted accomplishments
- Bulleted blockers (flagged with ⚠️)
- Bulleted next-week priorities

Save to status_report_[date].txt.
Use Python built-ins only.
```

---

### Meeting Notes Formatter

**The problem:** You take rough meeting notes and need to share clean action items.

**What to build:** A tool that reads raw meeting notes from a text file and extracts action items, decisions, and open questions into a structured format.

**Prompt starting point:**
```
Build me a Python tool that reads meeting-notes.txt and organizes the content.

Rules:
- Lines starting with "AI:" or "Action:" are action items
- Lines starting with "Decision:" are decisions
- Lines starting with "?" or "Q:" are open questions
- Everything else is a discussion point

Output:
📌 Action Items (numbered list)
✅ Decisions Made (numbered list)
❓ Open Questions (numbered list)
📝 Discussion Points (bulleted list)

Use Python built-ins only.
```

---

### Data Format Converter

**The problem:** You get data in one format (CSV) and need it in another format (Markdown table, Jira-compatible, or JSON).

**What to build:** A tool that reads a CSV and converts it to your desired format.

**Prompt starting point:**
```
Build me a Python tool that converts CSV files to Markdown tables.

Ask for the CSV filename.
Read the file.
Output a Markdown table with:
- A header row from the CSV column names
- Aligned columns
- A separator row with dashes

Also print the Markdown to the console and save it to [filename]_table.md.
Use Python built-ins only.
```

---

## How to Go from Workshop to Real Use

1. **Start with your actual data.** Replace sample-data.csv with a real export from your analytics tool. Replace sample-feedback.txt with real user feedback. The tools work the same way with real data.

2. **Customize the criteria.** The Decision Framework defaults are generic. Replace them with your team's actual prioritization criteria and weights.

3. **Build in the same conversation.** Start with the base prompt, add features incrementally, and iterate based on what you see. Three prompts to get a useful tool is typical.

4. **Save your prompts.** When you find a prompt that produces good results, save it. The [Prompts Library](../prompts/) is a starting point — add your own to it.

5. **Share the output, not the code.** Your stakeholders do not care about Python. They care about the ranked feature list, the retention table, or the pricing model. Run the tool, copy the output, and paste it into Slack or your planning doc.

---

## What to Build First

If you finished the workshop and want to keep going, here is a prioritized path:

| Priority | Build | Why |
|---|---|---|
| 1 | Feature Prioritizer (Build 02) | Directly useful for sprint planning — produces a ranked list you can bring to the next meeting |
| 2 | Feedback Analyzer (Build 06) | If you have user feedback sitting in a file, this gives you instant categorization |
| 3 | Pricing Calculator (Build 05) | Useful if you are working on pricing or monetization |
| 4 | A/B Test Calculator (Build 04) | Quick, focused, and useful every time you plan an experiment |
| 5 | Cohort Analyzer (Build 03) | Requires a data export, but powerful once you have the CSV |
| 6 | Metric Dashboard (Build 07) | The most complex build — requires Streamlit — but produces a real dashboard |
