## 2024-05-30 - Helpful Empty States in DataFrames
**Learning:** When using Streamlit DataFrames (`st.dataframe`) to display data like ACB pools or transaction history, rendering an empty DataFrame with headers alone is visually confusing and doesn't tell the user what to do next.
**Action:** Check if the DataFrame is empty (`if df.empty:`) before rendering the table. If it's empty, display an `st.info` message explaining why the data is missing and how the user can add it (e.g., "Import CSVs").
