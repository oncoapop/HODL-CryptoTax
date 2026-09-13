## 2024-11-20 - [DataFrames Empty States]
**Learning:** Displaying blank or empty dataframes in Streamlit can confuse users, making them think the application is broken or stuck loading. Using `df.empty` checks allows displaying a contextual, helpful empty state message explaining *why* the data is empty (e.g., "No transactions found. Import CSV files.").
**Action:** Always verify if a dataframe might be empty before rendering it. Use `st.info` to display actionable guidance instead of rendering an empty table shell.
