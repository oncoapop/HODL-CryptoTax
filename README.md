# 🇨🇦 CytoTax Engine — CRA Crypto Tax & ACB Ledger

**CytoTax** is an open-source, self-hosted Canadian cryptocurrency tax calculation engine and portfolio ledger designed to replace paid services like Koinly.

It calculates **Adjusted Cost Base (ACB)** per token under Canadian Revenue Agency (CRA) rules, segregates the **2024 CRA inclusion rate shift** (`2024 P1` vs `2024 P2`), tracks **Line 13000 / T2125 income** (mining, staking, lending interest, rewards), and generates **CRA Schedule 3 capital gains reports**.

---

## 🛠️ Features
- **CRA ACB Engine**: Weighted-average cost basis tracking per token pool across all wallets/exchanges.
- **2024 Inclusion Rate Shift**: Automatically separates 2024 tax period 1 (Jan 1 – Jun 24, 50% inclusion) and period 2 (Jun 25 – Dec 31).
- **Schedule 3 Exporter**: Exports ready-to-file CRA Schedule 3 CSV line items (Proceeds, ACB, Outlays, Capital Gains/Losses).
- **Streamlit Web Dashboard**: Interactive local UI to inspect portfolio balances, ACB pools, realized gains, and historical transaction ledgers.
- **Historical Benchmark Verification**: Milestone test suite to verify calculated annual totals against prior filed CRA Schedule 3 returns.

## 🏛️ CRA Compliance & Directive Alignment
CytoTax is engineered to strictly follow official **Canada Revenue Agency (CRA)** tax legislation and administrative directives:
1. **Income Tax Act (ITA) Section 47 (ACB)**: Weighted-average cost pooling for identical properties across all non-registered wallets and exchanges.
2. **ITA Section 54 (Dispositions)**: Taxable dispositions on crypto-to-fiat, crypto-to-crypto trades, and fee payments.
3. **Line 13000 / T2125 Income**: 100% CAD FMV valuation on date of receipt for mining, staking, rewards, and lending interest.
4. **2024 Schedule 3 Inclusion Rate Shift**: Automatic period segregation (`2024 P1` Jan 1 – Jun 24 vs `2024 P2` Jun 25 – Dec 31).

Read the complete [CRA Compliance & Directive Alignment Statement](file:///e:/CODEX/Cytotax/docs/CRA_COMPLIANCE_STATEMENT.md) for full statutory references.

---

## 📂 Project Structure

```
Cytotax/
├── .gitignore              # Privacy filter excluding personal PDF/CSV/DB files
├── README.md               # Documentation & usage guide
├── LICENSE                 # MIT License
├── examples/               # Anonymized sample data format
│   └── sample_transactions.csv
├── Schedule3/              # Drop prior filed CRA Schedule 3 PDF reports here
├── Transactions/           # Drop your historical transaction CSV exports here
└── src/
    ├── db.py               # SQLite database initialization
    ├── importer.py         # Multi-CSV ingestion engine & deduplicator
    ├── acb.py              # CRA ACB math algorithm & income tracking
    ├── reporter.py          # Schedule 3 CSV export generator
    ├── test_reconciliation.py # Verification suite against Schedule 3 milestones
    └── dashboard.py        # Streamlit web UI
```

---

## 📊 Standard CSV Data Format & Converters

CytoTax reads standard transaction CSVs containing the following headers (skipping title rows):

| Column Name | Description |
| :--- | :--- |
| `Date` | Timestamp in UTC (`YYYY-MM-DD HH:MM:SS UTC`) |
| `Type` | Transaction type (`buy`, `sell`, `transfer`, `exchange`, `crypto_deposit`, `crypto_withdrawal`, `fiat_deposit`, `fiat_withdrawal`) |
| `Tag` | Special tag (`Mining`, `Staking`, `Reward`, `Lending interest`, `Airdrop`, `Cost`) |
| `Sending Wallet` | Origin exchange or wallet name |
| `Sent Amount` | Quantity of asset sent |
| `Sent Currency` | Currency ticker sent (e.g. `BTC`, `ETH`, `CAD`) |
| `Receiving Wallet` | Destination exchange or wallet name |
| `Received Amount` | Quantity of asset received |
| `Received Currency` | Currency ticker received |
| `Fee Amount` / `Fee Currency` | Fee incurred |
| `Gain (CAD)` / `Net Value (CAD)` | CAD spot valuation at timestamp |

### Converting Other Formats to CytoTax Format
If you have raw exchange CSVs (Coinbase, Kraken, Bitbuy, CoinTracker):
1. **Coinbase CSVs**: Map `Timestamp` $\rightarrow$ `Date`, `Transaction Type` $\rightarrow$ `Type`, `Quantity Transacted` $\rightarrow$ `Sent/Received Amount`, `Spot Price at Transaction` $\rightarrow$ `Net Value (CAD)`.
2. **On-Chain RPC / Etherscan / Solscan**: Map block timestamps to UTC `Date`, token transfer logs to `Sent`/`Received Amount`, and query CoinGecko / Yahoo Finance for historical CAD spot rate.

---

## 📜 Recommended Open Source License

We recommend releasing CytoTax under the **MIT License**.

### Why MIT?
- **Tax & Legal Protection**: Crucially includes an explicit **"AS IS" disclaimer of liability** so the author is not legally responsible for user tax filings.
- **Permissive & Standard**: Allows anyone to run, customize, and extend the tool freely.

---

## 🚀 Quick Start

1. Install dependencies using `uv`:
   ```bash
   uv sync
   ```
2. Run historical milestone verification:
   ```bash
   cd src
   uv run python test_reconciliation.py
   ```
3. Launch the visual web dashboard:
   ```bash
   uv run streamlit run dashboard.py
   ```
