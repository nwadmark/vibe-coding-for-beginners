# A/B Test Calculator

A command-line tool that calculates the sample size needed for an A/B test, estimates how long it will take to reach statistical significance, and explains the key statistical concepts in plain English.

**Estimated build time: 30 minutes**

## Why It's Useful for PMs

- **Prevents launching underpowered tests.** Running a test too short is the most common A/B testing mistake. This tool tells you exactly how long to wait.
- **Answers the #1 stakeholder question.** "How long will this test take?" Now you have a number.
- **No statistics degree required.** The tool explains what each input means and shows the math in plain language.

## How to Run It

### In Replit

1. Create a new Python Repl
2. Copy `replit/main.py` into the editor
3. Click **Run**

### In Cursor

1. Open `replit/main.py` in Cursor
2. Open the terminal and run: `python main.py`

## Sample Interaction

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A/B TEST SAMPLE SIZE CALCULATOR
  Plan your experiment before you ship it
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Baseline conversion rate (%): 3.5
  Minimum detectable effect (%): 0.5
  Confidence level (90/95/99): 95
  Daily traffic (visitors per day): 1000

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TEST PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Baseline rate:     3.50%
  Target rate:       4.00%
  Relative lift:     14.3%

  Sample needed:     ~15,680 per variant
  Total visitors:    ~31,360 across both variants
  Estimated time:    ~32 days

  ℹ️  At 95% confidence, if the true effect is 0.5%
  or larger, this test has ~80% power to detect it.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run another calculation? (yes/no): no
```

## How to Customize It

- Add support for comparing two known rates (post-test analysis)
- Include a "minimum runtime" warning (e.g., always run at least 1 full week)
- Show the sample size for multiple confidence levels side by side

## Prompts

See [prompts.md](prompts.md) for the prompt to build this tool and customization ideas.
