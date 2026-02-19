# Metric Dashboard (Advanced)

A web-based dashboard built with Streamlit that visualizes key product metrics from a CSV file. Shows metric cards with week-over-week deltas, a trend line chart, and a date range selector.

**Estimated build time: 60 minutes**

**This is the ONLY tool in the workshop that requires external libraries.** All other tools use Python built-ins only.

## Dependencies

Before running, install the required libraries:

```
pip install streamlit pandas plotly
```

## Why It's Useful for PMs

- **A real dashboard in under an hour.** Most PMs wait weeks to get a dashboard from the data team. Build your own prototype in 60 minutes.
- **Web-based and shareable.** Streamlit apps run in the browser, so you can share them with stakeholders.
- **Customizable without code changes.** Update the CSV with new data and the dashboard updates automatically.

## How to Run It

### In Replit

1. Create a new Python Repl
2. Copy `replit/main.py` into the editor
3. Upload `replit/sample-metrics.csv` to the same folder
4. In the Replit Shell (not Console), run: `pip install streamlit pandas plotly`
5. Then run: `streamlit run main.py`
6. Replit will open the web preview — click the URL to see your dashboard

### In Cursor

1. Put both `main.py` and `sample-metrics.csv` in the same folder
2. Open the terminal and run:
   ```
   pip install streamlit pandas plotly
   streamlit run main.py
   ```
3. Your browser will open with the dashboard

## Sample Output

The dashboard shows:

- **4 metric cards** at the top: Active Users, New Signups, Revenue, Retention Rate — each with a week-over-week change indicator
- **A line chart** showing all four metrics over time
- **A date range selector** in the sidebar to filter the data

## How to Customize It

- Replace the sample CSV with your own product metrics
- Add more metric columns to the CSV (they'll show up automatically)
- Change the chart type from line to bar or area

## Prompts

See [prompts.md](prompts.md) for the prompt to build this tool and customization ideas.
