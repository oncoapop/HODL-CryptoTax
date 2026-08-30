@echo off
title CytoTax Engine - CRA Crypto Tax Ledger
echo Starting CytoTax Streamlit Dashboard...
cd src
uv run --with streamlit --with pandas streamlit run dashboard.py
pause
