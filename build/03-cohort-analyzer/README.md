# Cohort Analyzer

A command-line tool that reads user data from a CSV file, groups users into weekly signup cohorts, and calculates retention rates for each cohort over time. Shows results as an ASCII retention table.

**Estimated build time: 45 minutes**

## Why It's Useful for PMs

- **Retention is the metric that matters most.** Acquisition means nothing if users leave. This tool shows you exactly where users drop off.
- **Cohort analysis reveals trends over time.** If Week 1 retention is improving across cohorts, your onboarding changes are working.
- **No spreadsheet gymnastics required.** Cohort analysis in Excel takes pivot tables and formulas. This tool does it in one command.

## How to Run It

### In Replit

1. Create a new Python Repl
2. Copy `replit/main.py` into the editor
3. Upload `replit/sample-data.csv` to the same folder (drag it into the Files panel)
4. Click **Run**

### In Cursor

1. Put both `main.py` and `sample-data.csv` in the same folder
2. Open the terminal and run: `python main.py`

## Sample Output

```
COHORT RETENTION ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cohort       Users  Week0  Week1  Week2  Week3  Week4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2024-W01       14   100%    64%    43%    29%    21%
2024-W02       13   100%    62%    38%    23%    15%
2024-W03       12   100%    58%    42%    25%     --
2024-W04       11   100%    55%    36%     --     --
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY INSIGHTS
  Avg Week 1 retention: 60%
  Avg Week 2 retention: 40%
  Biggest drop: Week 0 → Week 1 (40% loss)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## How to Customize It

- Change the cohort grouping from weekly to monthly
- Add a "source" column to the CSV and compare retention by acquisition channel
- Export the retention table to a new CSV for use in presentations

## Prompts

See [prompts.md](prompts.md) for the prompt to build this tool and customization ideas.
