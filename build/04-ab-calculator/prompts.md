# A/B Test Calculator — Prompts

## Build Prompt

Copy and paste this into Claude or ChatGPT:

```
I'm a product manager. Build me a command-line A/B test sample size calculator in Python.

The tool should:
1. Ask for baseline conversion rate (as a percentage, like 3.5)
2. Ask for minimum detectable effect (absolute percentage points, like 0.5)
3. Ask for confidence level (offer 90, 95, or 99)
4. Ask for daily traffic (visitors per day)
5. Calculate the required sample size per variant using this formula:
   - Z-scores: 90% → 1.645, 95% → 1.96, 99% → 2.576
   - Power of 80% (Z_beta = 0.84)
   - p1 = baseline rate, p2 = baseline + MDE
   - n = (Z_alpha + Z_beta)² × (p1(1-p1) + p2(1-p2)) / (p2 - p1)²
6. Show:
   - Sample needed per variant
   - Total visitors needed (both variants)
   - Estimated days to reach significance (total / daily traffic)
   - Relative lift percentage
   - A plain-English explanation of what the numbers mean
7. Ask if they want to run another calculation

Use only the math module. No scipy, no numpy.
Add comments explaining each statistical concept.
Keep it under 80 lines.
```

### Why this prompt works

- **The formula is explicit** with Z-score values provided, so the AI doesn't need scipy.
- **Input format is specified** (percentage like 3.5, not decimal like 0.035) to match how PMs think.
- **"Plain-English explanation"** forces the AI to add context, not just raw numbers.

### What you could change

- Add a one-tailed vs two-tailed test option.
- Include multiple power levels (70%, 80%, 90%) to show trade-offs.
- Add a "quick mode" with common baseline rates for e-commerce (checkout, signup, etc.).

## Customization Prompt

```
Add these features:
1. Show a comparison table for all three confidence levels (90%, 95%, 99%) at once
2. Add a warning if the estimated time is over 60 days: "⚠️ Consider increasing traffic or MDE"
3. Show the formula used with actual numbers filled in

Keep existing logic. Add these three things only.
```
