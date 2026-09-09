# Payment Fraud Analysis

**Tech Stack:** Python, Pandas, NumPy, Scikit-learn, SQL, Power BI  
**Project Type:** Self Project  
**Dataset:** 5,000 synthetic payment transactions  
**Date Range:** January–June 2026

## Project objective

Clean, process, and analyze payment transaction data to identify fraud patterns and suspicious transactions. The project combines Python preprocessing, SQL analysis, anomaly detection, exploratory data analysis, and a Power BI-ready dashboard.

## Key analysis areas

- Transaction amount
- Merchant category
- Transaction type
- City/geographical distribution
- Device and channel
- International transactions
- Failed attempts
- Fraud rate and fraud value
- Anomaly/suspicious transaction detection

## Project structure

```text
payment-fraud-analysis/
├── data/
│   ├── raw/payment_transactions.csv
│   └── processed/
├── src/
│   ├── generate_data.py
│   ├── preprocess.py
│   ├── anomaly_detection.py
│   └── eda.py
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
├── dashboard/
│   ├── measures.dax
│   └── powerbi_setup.md
├── reports/figures/
├── requirements.txt
├── .gitignore
└── README.md
```

## Run locally

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/preprocess.py
python src/anomaly_detection.py
python src/eda.py
```

The main Power BI source is:

`data/processed/fraud_analysis_data.csv`

## Methodology

### 1. Data preprocessing
- Converted timestamps and dates
- Handled missing categorical values
- Filled numeric missing values using appropriate defaults/median
- Removed duplicate transaction IDs
- Created hour, day-of-week, month, and night-time features

### 2. EDA
Fraud trends are analyzed across:
- merchant categories
- transaction types
- cities
- transaction dates
- transaction value

### 3. Anomaly detection
An **Isolation Forest** model identifies unusual transactions using:
- log transaction amount
- failed attempts
- international transaction indicator
- night-time activity

The model's output is stored in `anomaly_flag` and `anomaly_score`.

**Important:** anomaly detection is used as a suspicious-activity signal; it is not treated as ground-truth fraud classification.

### 4. SQL analysis
SQL queries calculate:
- total transactions
- total transaction value
- fraud transactions
- fraud rate
- fraud value
- category/type/geographical breakdowns
- high-value fraudulent transactions
- suspicious transactions

### 5. Power BI
The dashboard is designed around KPI cards, fraud trends, merchant-category analysis, transaction-type analysis, geographical analysis, and a suspicious-transaction table.

## Resume-aligned project description

> Cleaned, processed, and analyzed payment transaction data using Python and SQL to identify anomalies and suspicious transaction patterns. Performed EDA to investigate fraud trends across transaction amount, merchant category, transaction type, and geographical location. Developed an interactive Power BI dashboard to visualize fraud distribution and monitor fraud-related KPIs across merchant categories and transaction types.

## Interview talking points

**Why this project?**  
To demonstrate an end-to-end analytics workflow where raw transaction data is transformed into business insights and a fraud-monitoring dashboard.

**Why Isolation Forest?**  
Fraud datasets can be imbalanced and suspicious behavior may not always have a simple rule. Isolation Forest is an unsupervised anomaly-detection method that isolates unusual observations efficiently.

**Fraud vs anomaly:**  
Fraud is the labeled business outcome (`is_fraud`). An anomaly is an observation that looks unusual based on selected behavioral/numeric features. An anomaly is not automatically fraud.

**Why Power BI?**  
Python is useful for preprocessing and modeling, SQL is useful for querying and aggregation, while Power BI makes the resulting KPIs and trends interactive for business users.

## Notes

This repository contains a **synthetic dataset** created for portfolio/interview demonstration. It does not contain real customer or financial information.

The repository includes everything needed to reproduce the analysis and build the Power BI dashboard. The Power BI binary `.pbix` file is not generated automatically because it requires Power BI Desktop; the dashboard data, DAX measures, and exact visual layout are included.
