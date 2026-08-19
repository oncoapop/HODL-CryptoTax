@echo off
title CytoTax Engine - CRA Crypto Tax Ledger
echo Starting CytoTax Streamlit Dashboard...
cd /d "e:\CODEX\Cytotax\src"
"C:\Users\damia\.local\bin\uv.exe" run --with streamlit --with pandas streamlit run dashboard.py
pause
