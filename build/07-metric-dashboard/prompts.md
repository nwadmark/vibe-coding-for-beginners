# Metric Dashboard — Prompts

## Build Prompt

Copy and paste this into Claude or ChatGPT:

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

### Why this prompt works

- **The CSV schema is specified** so the AI generates compatible code.
- **"Week-over-week delta"** is specific — the AI knows to compare to the previous row.
- **"Positive in green, negative in red"** specifies the visual treatment.
- **Libraries are named** (streamlit, pandas, plotly) so the AI uses the right tools.

### What you could change

- Add a second chart type (bar chart for signups, line chart for revenue).
- Include a "goal line" on each metric to show targets.
- Add a CSV upload widget so users can drag in their own data file.

## Customization Prompt

```
Add these features:
1. Add a second tab called "Details" that shows the raw data as a table
2. In the sidebar, add a metric selector dropdown to highlight one metric on the chart
3. Add a "Download Report" button that exports the filtered data as CSV

Keep existing logic. Add these three things only.
```
