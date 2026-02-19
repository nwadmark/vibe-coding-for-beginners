# Track B — Build a Data Analysis Tool

Build a tool that analyzes real product data and produces insights you will actually use. Automate a recurring analysis or answer a question that has been sitting in your backlog.

---

## What You Will Build

A Python tool that takes data you already have (CSV exports, spreadsheet data, log files) and produces analysis you currently do manually — or have been meaning to do but never had time for.

The output should be something you can paste into Slack, a planning doc, or a stakeholder email. The tool should be something you run weekly or monthly, not a one-off.

---

## Why This Track

Choose Track B if:

- You work with data regularly (metrics, cohorts, feedback, surveys)
- You have a recurring analysis that takes too long in spreadsheets
- You want to automate something you do every sprint or every month
- You have a data question that has been sitting in your backlog

---

## Success Criteria

Your capstone is done when:

- [ ] It reads real data (or realistic sample data in the same format as your real data)
- [ ] It produces analysis you would actually use in a meeting or document
- [ ] The output is formatted for sharing (not raw numbers — formatted tables, summaries, insights)
- [ ] You can run it again next week with new data and get updated results
- [ ] You built it in under 4 hours

---

## The Process

### Step 1: Identify the Analysis (30 minutes)

Answer these questions:

1. **What data do you have?** Where does it come from? What format is it in? What columns/fields does it contain?
2. **What question do you want to answer?** Be specific — "How is retention?" is vague. "What is Week 4 retention by signup cohort for the past 8 weeks?" is specific.
3. **What would you do with the answer?** Where would you share it? What decision does it inform?
4. **How often do you need this?** One-time or recurring?

**Example — ShopFlow retention analysis:**

1. Data: CSV export from analytics tool. Columns: `user_id`, `signup_date`, `last_active_date`, `plan_tier`.
2. Question: What is Week 1 through Week 8 retention by signup cohort, broken down by plan tier (Free vs Paid)?
3. Use: Include in the bi-weekly product review. Inform decisions about onboarding investments.
4. Frequency: Every two weeks before the product review meeting.

### Step 2: Prepare Your Data (15 minutes)

**Option A: Use real data.** Export from your analytics tool, CRM, or database. Remove any PII or sensitive fields you do not need. Save as CSV.

**Option B: Create realistic sample data.** If you cannot use real data (privacy, access), create a CSV with the same columns and realistic values. The AI can help:

```
Generate a CSV file with 200 rows of sample user data.
Columns: user_id, signup_date, last_active_date, plan_tier
- user_id: integers 1-200
- signup_date: random dates between 2024-01-01 and 2024-06-30
- last_active_date: signup_date + random 0-90 days (some users churn early)
- plan_tier: "free" (70%) or "paid" (30%)

Output as CSV format that I can save to a file.
```

### Step 3: Build the Core Analysis (60 minutes)

Your first prompt should cover:

- What file to read and what format
- What calculation or grouping to perform
- What the output should look like

**Example prompt:**

```
Build me a Python tool that analyzes user retention by cohort.

Input: Read user-data.csv with columns: user_id, signup_date, last_active_date, plan_tier

Analysis:
1. Group users into weekly cohorts by signup_date
2. For each cohort, calculate retention at Week 0, 1, 2, 3, 4, 5, 6, 7, 8
   - A user is "retained" in Week N if last_active_date >= signup_date + N weeks
3. Show retention as percentages

Output:
1. An ASCII table showing cohort (rows) x week (columns) with retention percentages
2. Use "--" for weeks that haven't happened yet
3. Below the table, show:
   - Average retention at each week across all cohorts
   - The biggest week-over-week drop (which transition loses the most users)
   - The best-performing cohort and worst-performing cohort

Use only Python built-ins (csv, datetime). No pip install.
Add comments explaining the retention calculation.
```

### Step 4: Add the Breakdown You Need (45 minutes)

The core analysis answers the top-level question. Now add the breakdown that makes it actionable.

**Example follow-up prompt:**

```
Add a plan tier breakdown.

After the main retention table, show a second table filtered to "free" users only
and a third table filtered to "paid" users only.

Below all three tables, show:
- Side-by-side comparison of free vs paid retention at each week
- The week where free and paid retention diverge the most
- A plain-English summary: "Paid users retain X% better at Week 4"

Keep existing output. Add the breakdown below it.
```

### Step 5: Format for Sharing (30 minutes)

Make the output something you can paste directly into Slack, a doc, or an email.

```
Format the entire output so I can paste it into Slack.

- Use fixed-width formatting for tables (wrap in triple backticks)
- Add a header line: "Retention Report — [today's date]"
- Add a "Key Takeaways" section at the end with 3 bullet points
  summarizing the most important findings
- At the very end, add: "Generated by PM Retention Tool"

Keep existing analysis. Change only the formatting.
```

### Step 6: Make It Reusable (30 minutes)

If this is a recurring analysis, add features that make it easy to run again:

```
Add these features:
1. At the start, ask for the CSV filename (default: user-data.csv)
2. Ask for the time period to analyze (default: all data)
3. At the end, ask "Save report to file? (yes/no)"
4. If yes, save to retention_report_[date].txt

Keep existing analysis and formatting.
```

---

## ShopFlow Example Project

Alex, PM at ShopFlow, needed retention data for the bi-weekly product review but the analytics team was backlogged. Alex had access to a CSV export.

**Data:** Weekly CSV export from the analytics dashboard. 2,400 users over 3 months. Columns: `user_id`, `signup_date`, `last_active_date`, `plan_tier`.

**Question:** What is retention by weekly cohort, and how does free vs paid retention compare?

**What Alex built:**

1. Core retention table (Week 0-8 by signup cohort)
2. Free vs paid breakdown with comparison
3. "Key Takeaways" summary auto-generated from the data
4. Save-to-file feature for archiving reports

**Time taken:** 3.5 hours (30 min planning, 60 min core analysis, 45 min breakdown, 30 min formatting, 30 min reusability, 15 min testing)

**Key finding:** Free users dropped to 12% retention by Week 4, while paid users held at 61%. The divergence started at Week 2 — suggesting that the first two weeks of the free experience were the critical window for conversion.

**Impact:** Alex brought this data to the product review and the team prioritized an onboarding redesign focused on the Week 1-2 experience for free users.

**What did not work initially:**
- The first version miscounted weeks because it used calendar weeks instead of "weeks since signup." Alex had to specify: "Use weeks relative to each user's signup date, not calendar weeks."
- The ASCII table was too wide for Slack (it got line-wrapped). Alex asked: "Limit the table to 80 characters wide. Abbreviate column headers if needed."
- Saving to file saved the table without the summary. Alex had to say: "Save the complete output including the Key Takeaways section."

---

## Your Turn

Fill in this worksheet before you start building:

```
Data source: _________________________________
File format:  [ ] CSV  [ ] TXT  [ ] JSON  [ ] Other
Key columns: _________________________________

Question to answer:
______________________________________________

Who sees the output: _________________________
Where you'll share it: ______________________
How often you'll run it: ____________________

What would make this analysis useful?
______________________________________________
```

---

## Prompts for Common PM Data Analyses

### Retention / Cohort Analysis

```
Build a Python tool that reads [filename].csv with columns: [your columns].
Group users into [weekly/monthly] cohorts by [date column].
Calculate retention at [Week/Month] 0 through [N].
Show an ASCII table and summary statistics.
Use Python built-ins only (csv, datetime).
```

### Feedback / Survey Analysis

```
Build a Python tool that reads [filename].txt with one feedback item per line.
Classify each as positive, neutral, or negative using these keywords:
- Positive: [your positive words]
- Negative: [your negative words]
Show counts, percentages, and 3 sample quotes from each category.
Add a "top issues" section showing the most common negative keywords.
Use Python built-ins only.
```

### Metric Trend Analysis

```
Build a Python tool that reads [filename].csv with columns: date, [metric 1], [metric 2], [metric 3].
For each metric:
- Show the current value and previous value
- Calculate week-over-week and month-over-month change
- Flag any metric that dropped more than [X]%
Show a summary table and highlight concerning trends.
Use Python built-ins only.
```

### Funnel Analysis

```
Build a Python tool that reads [filename].csv with columns: user_id, [step 1 timestamp], [step 2 timestamp], ..., [step N timestamp].
For each step in the funnel:
- Count how many users reached that step
- Calculate the conversion rate from the previous step
- Calculate the overall conversion rate from step 1
Show a funnel visualization using ASCII bars.
Highlight the step with the biggest drop-off.
Use Python built-ins only.
```
