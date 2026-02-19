# Metric Dashboard
# A web-based product metrics dashboard built with Streamlit.
# NOTE: This is the only tool that requires external libraries.
# Install first: pip install streamlit pandas plotly
# Run with: streamlit run main.py

import streamlit as st
import pandas as pd
import plotly.express as px

# ── Page config ──────────────────────────────────────────────────────

st.set_page_config(page_title="Product Metrics Dashboard", layout="wide")
st.title("Product Metrics Dashboard")

# ── Load data ────────────────────────────────────────────────────────

@st.cache_data
def load_data():
    df = pd.read_csv("sample-metrics.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# ── Sidebar: date range filter ───────────────────────────────────────

st.sidebar.header("Filters")
min_date = df["date"].min().date()
max_date = df["date"].max().date()
start, end = st.sidebar.date_input(
    "Date range", value=(min_date, max_date), min_value=min_date, max_value=max_date
)
filtered = df[(df["date"].dt.date >= start) & (df["date"].dt.date <= end)]

# ── Metric cards ─────────────────────────────────────────────────────
# Show the latest value and week-over-week change for each metric

if len(filtered) >= 2:
    latest = filtered.iloc[-1]
    previous = filtered.iloc[-2]
else:
    latest = filtered.iloc[-1] if len(filtered) >= 1 else None
    previous = None

if latest is not None:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        delta = int(latest["active_users"] - previous["active_users"]) if previous is not None else None
        st.metric("Active Users", f"{int(latest['active_users']):,}", delta=delta)

    with col2:
        delta = int(latest["new_signups"] - previous["new_signups"]) if previous is not None else None
        st.metric("New Signups", f"{int(latest['new_signups']):,}", delta=delta)

    with col3:
        delta = round(latest["revenue"] - previous["revenue"], 2) if previous is not None else None
        st.metric("Revenue", f"${latest['revenue']:,.0f}", delta=f"${delta:,.0f}" if delta else None)

    with col4:
        delta = round(latest["retention_rate"] - previous["retention_rate"], 1) if previous is not None else None
        st.metric("Retention Rate", f"{latest['retention_rate']:.1f}%", delta=f"{delta:.1f}%" if delta else None)

# ── Trend chart ──────────────────────────────────────────────────────
# Line chart showing all four metrics over time

st.subheader("Trends Over Time")

# Melt the dataframe so each metric becomes a row (long format for Plotly)
chart_data = filtered.melt(
    id_vars=["date"],
    value_vars=["active_users", "new_signups", "revenue", "retention_rate"],
    var_name="Metric",
    value_name="Value",
)

fig = px.line(chart_data, x="date", y="Value", color="Metric", markers=True)
fig.update_layout(height=400, xaxis_title="Date", yaxis_title="Value")
st.plotly_chart(fig, use_container_width=True)

# ── Footer ───────────────────────────────────────────────────────────

st.caption(f"Showing {len(filtered)} of {len(df)} data points")
