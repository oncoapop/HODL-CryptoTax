## 2024-05-18 - Streamlit Empty DataFrame States
**Learning:** Displaying empty pandas DataFrames via `st.dataframe` renders an unhelpful blank table structure which can confuse users expecting data.
**Action:** When working with data ingestion workflows, always check `df.empty` before rendering. If empty, return a contextual `st.info` block with actionable next steps (like "Please upload CSVs") instead of the bare table.
