## 2024-11-02 - Streamlit Empty States
**Learning:** In Streamlit, rendering empty pandas DataFrames creates confusing blank tables for users.
**Action:** Always check `if df.empty:` and render helpful `st.info` messages explaining the empty state and providing guidance.
