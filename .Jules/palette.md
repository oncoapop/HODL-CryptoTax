## 2024-05-20 - Empty States in Data Dashboards
**Learning:** Blank pandas DataFrames in Streamlit render as confusing empty tables, which users mistake for broken UI or loading issues rather than a lack of data.
**Action:** Always check `df.empty` and provide an actionable `st.info` empty state message to guide the user on how to populate the data.
