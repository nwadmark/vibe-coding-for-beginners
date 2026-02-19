# Feedback Analyzer — Prompts

## Build Prompt

Copy and paste this into Claude or ChatGPT:

```
I'm a product manager. Build me a command-line feedback sentiment analyzer in Python.

The tool should:
1. Read feedback from a text file called sample-feedback.txt (one item per line)
2. Classify each line as positive, neutral, or negative using keyword matching:
   - Positive keywords: love, great, awesome, easy, helpful, excellent, amazing, fast, intuitive, perfect
   - Negative keywords: hate, broken, confusing, slow, frustrating, terrible, awful, bug, crash, unusable
   - Neutral: anything that doesn't match positive or negative keywords
3. Count the number in each category
4. Show percentages for each category
5. Show up to 3 sample quotes from each category
6. Use emoji labels: 😊 Positive, 😐 Neutral, 😞 Negative

Use Python built-ins only. No TextBlob, no NLTK, no pip install.
Add comments explaining the classification logic.
Keep it under 100 lines.
```

### Why this prompt works

- **Keyword lists are explicit** so the AI doesn't invent its own sentiment model.
- **"One item per line"** specifies the file format clearly.
- **"Up to 3 sample quotes"** keeps the output readable.
- **"No TextBlob, no NLTK"** prevents the AI from reaching for heavy libraries.

### What you could change

- Add keyword weights (e.g., "love" = 2 points, "good" = 1 point) for more nuanced scoring.
- Add a "topics" analysis that counts mentions of specific features (import, export, dashboard, etc.).
- Let the user add custom keywords at runtime.

## Customization Prompt

```
Add these features:
1. Show which keywords were matched for each feedback item
2. Add a "top issues" section that counts the 3 most common negative keywords
3. At the end, ask if the user wants to save the analysis to a file

Keep existing logic. Add these three things only.
```
