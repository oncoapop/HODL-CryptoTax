## 2024-08-25 - Hiding Index in DataFrames Built from Dictionaries
**Learning:** When using `pd.DataFrame.from_dict(..., orient='index')`, the keys of the dictionary become the index. Hiding the index using `hide_index=True` in `st.dataframe()` will unintentionally hide this critical data column. Only hide the index for tables where the index is arbitrary (e.g. integer row numbers from SQL queries).
**Action:** Verify if the index contains meaningful data (like tax years) before applying `hide_index=True` to clean up tables.
