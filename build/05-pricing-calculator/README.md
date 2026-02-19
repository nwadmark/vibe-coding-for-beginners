# Pricing Calculator

A command-line tool that models pricing tiers and calculates monthly and annual recurring revenue. Enter up to 5 pricing tiers with name, price, and customer count, and see a complete revenue breakdown with percentage splits.

**Estimated build time: 30 minutes**

## Why It's Useful for PMs

- **Revenue modeling in 30 seconds.** Test "what if we raise the Pro tier by $10?" without opening a spreadsheet.
- **Shows revenue concentration risk.** If 80% of revenue comes from 5% of customers, you need to see that clearly.
- **Great for pricing reviews and board decks.** The output format is clean enough to screenshot and share.

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
  PRICING & REVENUE CALCULATOR
  Model your tiers, see your revenue
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

How many pricing tiers? (1-5): 3

Tier 1:
  Name: Starter
  Monthly price ($): 29
  Number of customers: 200

Tier 2:
  Name: Professional
  Monthly price ($): 79
  Number of customers: 80

Tier 3:
  Name: Enterprise
  Monthly price ($): 299
  Number of customers: 15

REVENUE BREAKDOWN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Tier            Price   Customers       MRR    Share
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Starter          $29       200       $5,800    34.9%
  Professional     $79        80       $6,320    38.1%
  Enterprise      $299        15       $4,485    27.0%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TOTALS
  Customers:     295
  MRR:           $16,605
  ARR:           $199,260
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Model another scenario? (yes/no): no
```

## How to Customize It

- Add a "what-if" mode that shows the revenue impact of changing one tier's price
- Include a customer growth rate to project revenue 3, 6, and 12 months out
- Add ARPU (Average Revenue Per User) calculation

## Prompts

See [prompts.md](prompts.md) for the prompt to build this tool and customization ideas.
