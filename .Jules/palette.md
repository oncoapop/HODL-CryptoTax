## 2024-03-24 - Streamlit Empty States
**Learning:** Streamlit renders confusing blank tables for empty DataFrames by default. Users need explicit empty states.
**Action:** Always check df.empty before rendering st.dataframe() and provide a helpful st.info() message with guidance.
