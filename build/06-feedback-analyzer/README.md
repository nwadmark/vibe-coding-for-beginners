# Feedback Analyzer

A command-line tool that reads user feedback from a text file, classifies each item as positive, neutral, or negative using keyword matching, and shows a sentiment summary with sample quotes from each category.

**Estimated build time: 45 minutes**

## Why It's Useful for PMs

- **See the signal in the noise.** When you have 50 pieces of feedback, you need to know the overall sentiment before reading every line.
- **Spot patterns quickly.** The category breakdown shows whether your users are mostly happy, mostly frustrated, or somewhere in between.
- **No NLP libraries required.** Simple keyword matching gets you 80% of the way there with zero setup.

## How to Run It

### In Replit

1. Create a new Python Repl
2. Copy `replit/main.py` into the editor
3. Upload `replit/sample-feedback.txt` to the same folder
4. Click **Run**

### In Cursor

1. Put both `main.py` and `sample-feedback.txt` in the same folder
2. Open the terminal and run: `python main.py`

## Sample Output

```
FEEDBACK SENTIMENT ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total feedback items: 30

😊 Positive: 12 (40.0%)
   "Love the bulk import feature, saves me hours"
   "Super easy to set up, great onboarding"
   "The dashboard is really helpful for tracking"

😐 Neutral: 10 (33.3%)
   "Works as expected"
   "Got the job done, nothing special"
   "Basic but functional"

😞 Negative: 8 (26.7%)
   "Import is painfully slow with large files"
   "Confusing interface, took forever to find settings"
   "Broken export function, lost my data"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## How to Customize It

- Add more keywords to improve classification accuracy
- Group feedback by topic (e.g., "import", "export", "UI") alongside sentiment
- Export results to CSV with columns: feedback, sentiment, keywords matched

## Prompts

See [prompts.md](prompts.md) for the prompt to build this tool and customization ideas.
