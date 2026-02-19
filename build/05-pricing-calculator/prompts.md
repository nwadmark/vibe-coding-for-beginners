# Pricing Calculator — Prompts

## Build Prompt

Copy and paste this into Claude or ChatGPT:

```
I'm a product manager. Build me a command-line pricing and revenue calculator in Python.

The tool should:
1. Ask how many pricing tiers (1-5)
2. For each tier, ask for:
   - Tier name (text)
   - Monthly price in dollars (number)
   - Number of customers (whole number)
3. Calculate per tier:
   - MRR (Monthly Recurring Revenue) = price × customers
   - Percentage share of total MRR
4. Display a formatted table with all tiers showing:
   - Tier name, price, customers, MRR, and share percentage
5. Show totals:
   - Total customers
   - Total MRR
   - Total ARR (Annual Recurring Revenue = MRR × 12)
6. Ask if they want to model another scenario

Use Python built-ins only. No pip install.
Format all dollar amounts with commas ($16,605).
Keep it under 90 lines with clear comments.
```

### Why this prompt works

- **Bounded inputs** (1-5 tiers) prevent overcomplication.
- **Per-tier and total calculations** are specified separately so the AI generates both.
- **"Format with commas"** ensures the output looks professional.

### What you could change

- Add annual billing discounts (e.g., "20% off annual plan") and show both monthly and annual pricing.
- Include a free tier with conversion rate to paid tiers.
- Add customer acquisition cost (CAC) and payback period.

## Customization Prompt

```
Add these features:
1. After showing totals, ask "Run a what-if? (yes/no)"
2. If yes, let the user pick a tier and change either the price or customer count
3. Show the old vs new revenue side by side with the delta

Keep existing logic. Add these three things only.
```
