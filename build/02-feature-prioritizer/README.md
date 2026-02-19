# Feature Prioritizer (RICE Score Calculator)

A command-line tool that ranks features using the RICE scoring framework. Enter multiple feature ideas with Reach, Impact, Confidence, and Effort, and the tool produces a ranked priority list sorted by RICE score.

**Estimated build time: 30 minutes**

## Why It's Useful for PMs

- **Makes prioritization meetings shorter.** Instead of debating opinions, you score features on four dimensions and let the math rank them.
- **RICE is an industry standard.** Used by Intercom, Atlassian, and thousands of product teams. Learning it here means you can apply it anywhere.
- **Produces a shareable artifact.** The ranked table can go straight into a sprint planning doc or roadmap review.

## How to Run It

### In Replit

1. Create a new Python Repl
2. Copy the code from `replit/main.py` into the editor
3. Click **Run**
4. Enter features one at a time, then see the ranked table

### In Cursor

1. Open `replit/main.py` in Cursor
2. Open the terminal and run: `python main.py`

## Sample Interaction

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  RICE FEATURE PRIORITIZER
  Rank features by Reach, Impact, Confidence, Effort
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Feature name: Bulk CSV import
  Reach (users affected per quarter): 500
  Impact (1=minimal, 2=medium, 3=massive): 2
  Confidence (0.0 to 1.0): 0.8
  Effort (person-weeks): 3
  → RICE Score: 266.7

Add another feature? (yes/no): yes

Feature name: Mobile app
  Reach (users affected per quarter): 2000
  Impact (1=minimal, 2=medium, 3=massive): 3
  Confidence (0.0 to 1.0): 0.6
  Effort (person-weeks): 12
  → RICE Score: 300.0

Add another feature? (yes/no): yes

Feature name: Advanced filters
  Reach (users affected per quarter): 300
  Impact (1=minimal, 2=medium, 3=massive): 2
  Confidence (0.0 to 1.0): 0.9
  Effort (person-weeks): 2
  → RICE Score: 270.0

Add another feature? (yes/no): yes

Feature name: API v2
  Reach (users affected per quarter): 150
  Impact (1=minimal, 2=medium, 3=massive): 3
  Confidence (0.0 to 1.0): 0.7
  Effort (person-weeks): 8
  → RICE Score: 39.4

Add another feature? (yes/no): no

RANKED FEATURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Rank  Feature              RICE Score
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1.   Mobile app               300.0
  2.   Advanced filters          270.0
  3.   Bulk CSV import           266.7
  4.   API v2                     39.4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 Top priority: Mobile app
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## How to Customize It

- Change the Impact scale from 1-3 to 1-5 for more granularity
- Add a "category" field to group features by theme (growth, retention, infrastructure)
- Export the ranked table to a CSV file for use in spreadsheets

## Prompts

See [prompts.md](prompts.md) for the prompt to build this tool and customization ideas.
