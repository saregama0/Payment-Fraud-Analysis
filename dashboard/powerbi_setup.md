# Power BI Dashboard Setup

## Import
1. Open Power BI Desktop.
2. Select **Get Data → Text/CSV**.
3. Import `data/processed/fraud_analysis_data.csv`.
4. Rename the table to `payment_transactions`.
5. Set `timestamp` to Date/Time, `transaction_date` to Date, and `amount` to Decimal Number.
6. Add the measures from `dashboard/measures.dax`.

## Recommended dashboard layout

### KPI cards
- Total Transactions
- Total Transaction Value
- Fraud Transactions
- Fraud Rate
- Fraud Value
- Suspicious Transactions

### Visual 1 — Fraud trend
- Line chart
- X-axis: `transaction_date`
- Y-axis: `Fraud Rate`

### Visual 2 — Merchant category
- Clustered bar chart
- Axis: `merchant_category`
- Values: `Fraud Transactions` or `Fraud Rate`

### Visual 3 — Transaction type
- Donut or bar chart
- Legend/Axis: `transaction_type`
- Values: `Fraud Transactions`

### Visual 4 — Geography
- Bar chart
- Axis: `city`
- Values: `Fraud Rate`
- Optional: map using `city` if your Power BI environment supports the required map visual.

### Visual 5 — Fraud amount
- Column chart
- Axis: `merchant_category`
- Values: `Fraud Value`

### Visual 6 — Suspicious activity
- Table
- Columns: transaction_id, timestamp, amount, merchant_category,
  transaction_type, city, anomaly_flag, anomaly_score

## Suggested slicers
- transaction_date
- merchant_category
- transaction_type
- city
- channel
- device_type
- is_fraud

## Dashboard title
**Payment Fraud Analysis Dashboard**

## Business questions answered
- How many transactions are fraudulent?
- What is the fraud rate?
- Which merchant categories have the highest fraud rate?
- Which transaction types show more suspicious activity?
- Which cities show higher fraud concentration?
- What transaction value is exposed to fraud?
- Which transactions are flagged as anomalies?
