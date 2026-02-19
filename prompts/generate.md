# Prompts for Building New PM Tools

Use these prompts when you want to build a new tool from scratch. Each prompt follows the same anatomy — a structure you can reuse for any tool you imagine.

---

## Prompt Template Anatomy

Every effective "build me a tool" prompt has five sections. Here is the skeleton:

```
I'm a product manager. Build me a command-line [TOOL DESCRIPTION] in Python.

The tool should:
1. [INPUT — what the user provides]
2. [INPUT — more data the user provides]
3. [CALCULATION — the formula or logic]
4. [OUTPUT — what the tool displays]
5. [OUTPUT — additional display or action]
6. [LOOP — ask if they want to repeat]

Use Python built-ins only (no pip install needed).
Add plain-English comments explaining each section.
Keep it under [LINE LIMIT] lines.
```

### Why each section matters

| Section | Purpose | What happens if you skip it |
|---|---|---|
| **Role** ("I'm a PM") | Sets the audience. The AI writes simpler, clearer code. | You get developer-oriented code with terse variable names. |
| **Inputs** (numbered) | Tells the AI exactly what data to collect. | The AI guesses what inputs to ask for — and usually gets it wrong. |
| **Calculation** (formula) | You control the logic. | The AI invents its own formula, different every time. |
| **Outputs** (format) | Specifies what the result looks like. | The AI chooses its own format — usually a raw number dump. |
| **Constraints** (builtins, line limit) | Keeps the code simple and runnable. | The AI imports heavy libraries and writes 300+ lines. |

---

## Tool Prompts

### Decision Framework (Build 01)

See [workshop-prompts.md](workshop-prompts.md) — Prompt #1 covers this tool.

---

### Feature Prioritizer — RICE Calculator (Build 02)

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

**What you could change:** Replace RICE with MoSCoW categories. Add weighted multipliers. Include a "quick mode" with preset Reach values.

---

### Cohort Analyzer (Build 03)

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

**What you could change:** Switch to monthly cohorts. Add a segment column. Show churn rate alongside retention.

---

### A/B Test Calculator (Build 04)

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

**What you could change:** Add one-tailed vs two-tailed options. Show multiple power levels. Include preset baselines for common scenarios.

---

### Pricing Calculator (Build 05)

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

**What you could change:** Add annual billing discounts. Include a free tier with conversion rate. Add CAC and payback period.

---

### Feedback Analyzer (Build 06)

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

**What you could change:** Add keyword weights for nuanced scoring. Add topic analysis for feature mentions. Let users add custom keywords at runtime.

---

### Metric Dashboard (Build 07)

```
I'm a product manager. Build me a web-based metric dashboard using Streamlit and Python.

The tool should:
1. Read from a CSV file called sample-metrics.csv with columns:
   date, active_users, new_signups, revenue, retention_rate
2. Show 4 metric cards at the top of the page:
   - Active Users (with week-over-week delta)
   - New Signups (with week-over-week delta)
   - Revenue (formatted as dollars, with delta)
   - Retention Rate (formatted as percentage, with delta)
3. Show a line chart with all four metrics over time (use Plotly)
4. Add a date range selector in the sidebar to filter the data
5. Show positive deltas in green, negative in red

Use streamlit, pandas, and plotly.
Add comments explaining each section.
Keep it under 80 lines.
```

**Note:** This is the only build project that requires `pip install` (streamlit, pandas, plotly). All others use Python built-ins only.

**What you could change:** Add a bar chart for signups. Include goal lines. Add a CSV upload widget.

---

## Build Your Own: Starter Template

Want to build a tool that is not in the list above? Use this template:

```
I'm a product manager. Build me a command-line [describe your tool] in Python.

The tool should:
1. Ask for [first input — describe what and what format]
2. Ask for [second input]
3. Calculate [describe the formula or logic in detail]
4. Display [describe the output format — include an example if possible]
5. Show [any additional output — summaries, warnings, insights]
6. Ask if the user wants to [repeat / save / export]

Use Python built-ins only (no pip install needed).
Add plain-English comments explaining each section.
Keep it under [80-120] lines.
```

**Tip:** The more specific you are about inputs, calculations, and output format, the better the result. Show the AI what you want the output to look like — if you can sketch it as ASCII text, include it.
