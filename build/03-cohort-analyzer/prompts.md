# Cohort Analyzer — Prompts

## Build Prompt

Copy and paste this into Claude or ChatGPT:

```
I'm a product manager. Build me a command-line cohort retention analyzer in Python.

The tool should:
1. Read a CSV file called sample-data.csv with columns: user_id, signup_date, last_active_date
   - Dates are in YYYY-MM-DD format
2. Group users into weekly cohorts by signup_date (use ISO week numbers)
3. Calculate retention for each cohort at Week 0, 1, 2, 3, and 4
   - A user is "retained" in Week N if their last_active_date is >= N weeks after signup
4. Display an ASCII table showing:
   - Cohort label (like 2024-W01)
   - Number of users in the cohort
   - Retention percentage for each week
   - Use "--" for weeks that haven't happened yet
5. Show key insights below the table:
   - Average retention at each week across all cohorts
   - Biggest retention drop (which week transition loses the most users)

Use only Python built-ins (csv, datetime). No pip install.
Add comments explaining the retention calculation.
Keep it under 120 lines.
```

### Why this prompt works

- **The CSV schema is specified** so the AI generates compatible code.
- **"ISO week numbers"** is precise — without it the AI might group by calendar week starting Sunday vs Monday.
- **The retention definition is explicit** — "last_active_date >= N weeks after signup" prevents ambiguity.
- **"Use -- for weeks that haven't happened"** handles the edge case of newer cohorts cleanly.

### What you could change

- Switch from weekly to monthly cohorts for longer-term analysis.
- Add a "segment" column and show retention by user segment.
- Calculate and display churn rate instead of (or alongside) retention rate.

## Customization Prompt

```
Add these features:
1. At the start, ask the user for the CSV filename (default: sample-data.csv)
2. Add a simple ASCII bar next to each retention percentage
3. Highlight any retention rate below 30% with a ⚠️ warning

Keep existing logic. Add these three things only.
```
