# Feature Prioritizer — Prompts

## Build Prompt

Copy and paste this into Claude or ChatGPT:

```
I'm a product manager. Build me a command-line RICE score calculator in Python.

The tool should:
1. Ask for a feature name (text)
2. Ask for Reach — users affected per quarter (whole number)
3. Ask for Impact — on a 1-3 scale (1=minimal, 2=medium, 3=massive)
4. Ask for Confidence — as a decimal from 0.0 to 1.0
5. Ask for Effort — in person-weeks (number)
6. Calculate RICE score: (Reach × Impact × Confidence) / Effort
7. Show the RICE score immediately after each feature
8. Ask "Add another feature? (yes/no)"
9. When done, show a ranked table sorted by RICE score descending
10. Show the top priority feature with a trophy emoji

Use Python built-ins only. Add clear comments. Keep it under 100 lines.
Validate all inputs (handle non-numeric entries gracefully).
```

### Why this prompt works

- **The RICE formula is explicit** so the AI doesn't invent its own version.
- **Scale definitions are included** (1-3 for Impact, 0-1 for Confidence) to prevent ambiguity.
- **"Show the RICE score immediately"** gives the user feedback before entering the next feature.
- **"Ranked table sorted descending"** specifies exact output behavior.

### What you could change

- Replace RICE with MoSCoW by changing the scoring to Must/Should/Could/Won't categories.
- Add a weighted RICE variant where you customize the multipliers for each dimension.
- Include a "quick mode" with preset Reach values for different user segments.

## Customization Prompt

After the base tool works, try this:

```
Add these features:
1. Show a bar chart next to each feature in the ranked table
2. Add a "tier" label: RICE > 200 = "🔥 High Priority", 50-200 = "📋 Medium", < 50 = "📦 Low"
3. Ask at the end if the user wants to export to CSV

Keep existing logic. Add these three things only.
```
