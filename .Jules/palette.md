## 2024-09-09 - [Streamlit Empty State Handlings]
**Learning:** In Streamlit dashboards displaying pandas DataFrames, when the DataFrame is empty (checked using `df.empty`), rendering it natively results in confusing blank tables or error-like artifacts. Users prefer clear guidance on why data is missing and what actions to take.
**Action:** Always check `df.empty` before rendering a DataFrame in Streamlit. If empty, use `st.info(message, icon="ℹ️")` to render helpful empty state messages with guidance instead of displaying blank tables.
