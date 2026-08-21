import streamlit as st
import sqlite3
import pandas as pd
from db import get_db, init_db
from acb import process_transactions

st.set_page_config(page_title="CytoTax - CRA Crypto Tax Engine", page_icon="🇨🇦", layout="wide")

st.title("🇨🇦 CytoTax Engine — Canadian Crypto Tax & Portfolio Ledger")
st.markdown("Custom Koinly replacement for CRA Schedule 3 capital gains & T2125 income reporting.")

# Sidebar controls
st.sidebar.header("Controls & Actions")
if st.sidebar.button(
    "Re-run Ingestion & Tax Computation",
    type="primary",
    use_container_width=True,
    help="Re-read transaction CSVs and recalculate tax data"
):
    with st.spinner("Re-indexing database and computing tax data..."):
        from importer import import_csvs
        import_csvs()
    st.sidebar.success("Database re-indexed successfully!")

# Compute tax totals
yearly_data = process_transactions()

tabs = st.tabs(["📊 Schedule 3 Tax Summary", "💰 Asset ACB Pools", "📜 Transaction History", "⚙️ Active Wallets (2026+)", "🏛️ CRA Compliance Statement"])

with tabs[0]:
    st.header("CRA Schedule 3 & Income Summary by Tax Year")
    
    selected_year = st.selectbox("Select Tax Period", list(yearly_data.keys()), index=len(yearly_data)-1 if yearly_data else 0)
    data = yearly_data.get(selected_year, {'Proceeds': 0.0, 'ACB': 0.0, 'Gain': 0.0, 'Income': 0.0})
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Proceeds of Disposition", f"${data['Proceeds']:,.2f}")
    col2.metric("Adjusted Cost Base (ACB)", f"${data['ACB']:,.2f}")
    
    gain_val = data['Gain']
    col3.metric("Realized Gain / Loss", f"${gain_val:,.2f}", delta=f"{gain_val:,.2f}" if gain_val >= 0 else f"{gain_val:,.2f}")
    col4.metric("Taxable Income (Line 13000)", f"${data['Income']:,.2f}")
    
    st.markdown("---")
    st.subheader("All Tax Years Summary Table")
    summary_df = pd.DataFrame.from_dict(yearly_data, orient='index')
    st.dataframe(summary_df.style.format("${:,.2f}"), use_container_width=True)

with tabs[1]:
    st.header("Active Currency Pools & Adjusted Cost Base (ACB)")
    conn = get_db()
    pools_df = pd.read_sql_query("SELECT currency, quantity, total_acb_cad, unit_cost_cad FROM acb_pools WHERE quantity > 0 ORDER BY total_acb_cad DESC", conn)
    conn.close()
    
    st.dataframe(pools_df.style.format({
        "quantity": "{:,.4f}",
        "total_acb_cad": "${:,.2f}",
        "unit_cost_cad": "${:,.4f}"
    }), use_container_width=True)

with tabs[2]:
    st.header("Historical Transaction Ledger")
    conn = get_db()
    tx_df = pd.read_sql_query("SELECT date, type, tag, sending_wallet, sent_amount, sent_currency, receiving_wallet, received_amount, received_currency, gain_cad, net_value_cad FROM transactions ORDER BY date DESC LIMIT 100", conn)
    conn.close()
    
    st.dataframe(tx_df, use_container_width=True)

with tabs[3]:
    st.header("Active 2026+ HODL Tracking Setup")
    st.info("Since you only HODL and receive passive rewards, your active 2026 sources are listed below:")
    
    st.markdown("""
    - **Centralized Exchanges**: Coinbase, KuCoin, Nexo, Kraken, Bitbuy, StakeCube.
    - **On-Chain Wallets**: Solana (`Helium`), Bitcoin (`Ledger`), Ethereum (`0x...`).
    - **Custom Chains**: SafeDeal (SFD), BiblePay (BBP).
    """)

with tabs[4]:
    st.header("🏛️ CRA Compliance & Directive Alignment Statement")
    st.success("CytoTax Engine is built to follow official Canada Revenue Agency (CRA) directives and Income Tax Act (ITA) statutory provisions.")
    
    st.markdown("""
    ### Implemented Statutory Framework:
    1. **ITA Section 47 (ACB Pools)**: Weighted-average cost basis pooling across all identical properties in non-registered accounts.
    2. **ITA Section 54 (Dispositions)**: Taxable dispositions on crypto-to-fiat sales, crypto-to-crypto trades, and transaction fee payments.
    3. **Line 13000 / Form T2125 (Income)**: 100% CAD Fair Market Value (FMV) reporting on date of receipt for mining, staking, lending interest, and rewards.
    4. **2024 Schedule 3 Inclusion Rate Shift**: Automatic period segregation into `2024 P1` (Jan 1 - Jun 24) and `2024 P2` (Jun 25 - Dec 31).
    5. **ITA Subsection 54(1) (Superficial Loss Rule)**: Loss denial on identical property re-acquired within 30 days before/after disposition.
    
    *Disclaimer: CytoTax is an open-source calculation assistance tool. Taxpayers are responsible for final verification of filings with the CRA or a certified CPA.*
    """)
