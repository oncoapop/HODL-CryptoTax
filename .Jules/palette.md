## 2024-05-24 - [Empty States in Streamlit DataFrames]
**Learning:** When DataFrames are empty, Streamlit renders confusing blank grids.
**Action:** Always check `df.empty` and provide helpful `st.info` messages.
