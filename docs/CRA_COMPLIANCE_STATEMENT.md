# 🇨🇦 Canada Revenue Agency (CRA) Compliance & Directive Alignment Statement

## Executive Overview
The **CytoTax Engine** is engineered to strictly align with official Canada Revenue Agency (CRA) income tax legislation, published tax guides, and administrative directives regarding cryptocurrency and digital asset taxation in Canada.

This statement documents the accounting methods, legal statutory references, and CRA directives implemented within the calculation engine.

---

## 🏛️ Implemented CRA Directives & Statutory Framework

### 1. Property Classification & Disposition Events
* **CRA Directive**: The CRA treats cryptocurrency as a commodity property under the *Income Tax Act* (ITA).
* **Taxable Dispositions**: Under Section 54 of the ITA, taxable dispositions occur whenever crypto assets are:
  - Sold for fiat currency (CAD, USD, etc.).
  - Traded or exchanged for another cryptocurrency or digital asset (e.g. BTC $\rightarrow$ ETH).
  - Used to pay transaction fees or purchase goods and services.
* **Non-Taxable Events**: Wallet-to-wallet transfers between accounts owned by the same taxpayer are non-taxable internal transfers.

### 2. Weighted-Average Adjusted Cost Base (ACB) Tracking
* **Statutory Provision**: Section 47 of the *Income Tax Act* mandates the **weighted-average cost method** for identical properties.
* **Engine Implementation**:
  - All identical tokens (e.g., BTC, ETH, SOL) held across non-registered accounts, exchanges, and on-chain wallets are pooled into a single universal ACB pool.
  - When new units are acquired, the total cost (acquisition price + transaction fees) is added to the pool's ACB.
  - Upon disposition, the ACB of the disposed units is computed using the average unit cost at the exact time of trade:
    $$\text{Unit Cost} = \frac{\text{Total ACB (CAD)}}{\text{Total Quantity}}$$
    $$\text{Realized Gain/Loss} = \text{Proceeds of Disposition (CAD)} - \text{Disposed ACB (CAD)} - \text{Outlays/Expenses (CAD)}$$

### 3. Income vs. Capital Gain Classification (Line 13000 & Form T2125)
* **CRA Directive**: Income generated from active or passive crypto activities—including **mining payouts, staking rewards, lending interest, and airdrops**—is classified as Income (Business/Other Income).
* **Engine Implementation**:
  - Income items are valued at 100% Fair Market Value (FMV in CAD) on the date of receipt and recorded for **Line 13000 / Form T2125**.
  - The receipt FMV is simultaneously added to the asset's ACB pool, establishing the cost basis for future dispositions.

### 4. 2024 CRA Capital Gains Inclusion Rate Segregation (Form T1-2024 Schedule 3)
* **CRA Directive**: Effective **June 25, 2024**, the CRA updated Schedule 3 (Capital Gains or Losses) to divide dispositions into two distinct periods:
  - **Period 1 (Jan 1, 2024 – Jun 24, 2024)**: Standard 50% inclusion rate (Schedule 3 Line 10693 / 10694).
  - **Period 2 (Jun 25, 2024 – Dec 31, 2024)**: Updated rules (Schedule 3 Line 15199 / 15300).
* **Engine Implementation**: Dispositions are automatically assigned to Period 1 or Period 2 based on UTC transaction timestamps to output exact Schedule 3 line items.

### 5. Superficial Loss Rules
* **Statutory Provision**: Subsection 54(1) of the ITA denies capital losses if identical property is acquired within **30 calendar days before or after disposition** by the taxpayer or an affiliated person and held at the end of the 30-day window. Denied losses are added back to the asset's ACB.

---

## ⚖️ Tax Disclaimer & User Responsibility

> **Notice**: While CytoTax is designed to rigorously implement CRA guidelines, tax legislation and administrative policies are subject to ongoing revision. This software is provided for informational and calculation assistance only and does not replace certified professional advice. Taxpayers remain responsible for verifying their tax filings with the Canada Revenue Agency or a qualified Chartered Professional Accountant (CPA).
