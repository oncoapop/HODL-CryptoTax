## 2025-02-12 - Empty State for Streamlit DataFrames
**Learning:** Streamlit dataframes render as a somewhat confusing, tiny blank box when `df.empty` is true. Users may not realize the table is intentionally empty versus broken.
**Action:** When working with Streamlit dashboards displaying dynamic data, explicitly check `if df.empty:` and render a helpful call-to-action or guidance using `st.info` before attempting to render the table.
