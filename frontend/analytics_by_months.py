import streamlit as st
import requests
import pandas as pd
from datetime import datetime

API_URL = "http://localhost:8000"

def analytics_months_tab():
    st.title("Monthly Expense Analytics")

    try:
        response = requests.get(f"{API_URL}/analytics/monthly")
        response.raise_for_status()
        data = response.json()

        if not data:
            st.warning("No data available.")
            return

        # Format "2024-08" → "August 2024"
        def format_month(month_str):
            dt = datetime.strptime(month_str, "%Y-%m")
            return dt.strftime("%B %Y")

        # Aggregate totals by month only
        month_totals = []
        for month, categories in data.items():
            total = sum(categories.values())
            month_totals.append({
                "Month": format_month(month),
                "Total": total
            })

        df = pd.DataFrame(month_totals)
        df = df.sort_values("Month")

        st.subheader("Total Expenses by Month")
        st.bar_chart(data=df.set_index("Month"))

        st.subheader("Monthly Total Table")
        df["Total"] = df["Total"].map("{:.2f}".format)
        st.dataframe(df.reset_index(drop=True), use_container_width=True)

    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch analytics: {e}")
