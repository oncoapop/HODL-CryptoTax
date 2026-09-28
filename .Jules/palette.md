## 2024-05-24 - Empty DataFrames in Streamlit
**Learning:** Displaying an empty DataFrame using st.dataframe() in Streamlit results in a blank, unhelpful UI element. It is better to check if the DataFrame is empty (using df.empty) and display a helpful message instead (using st.info).
**Action:** Always check if a pandas DataFrame is empty before rendering it in a Streamlit table. If empty, provide a descriptive empty state message.
