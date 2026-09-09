-- 1. Overall KPIs
SELECT
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount), 2) AS total_transaction_value,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) AS fraud_rate_pct,
    ROUND(SUM(CASE WHEN is_fraud = 1 THEN amount ELSE 0 END), 2) AS fraud_value
FROM payment_transactions;

-- 2. Fraud by merchant category
SELECT
    merchant_category,
    COUNT(*) AS transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) AS fraud_rate_pct,
    ROUND(SUM(CASE WHEN is_fraud = 1 THEN amount ELSE 0 END), 2) AS fraud_value
FROM payment_transactions
GROUP BY merchant_category
ORDER BY fraud_rate_pct DESC;

-- 3. Fraud by transaction type
SELECT
    transaction_type,
    COUNT(*) AS transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) AS fraud_rate_pct
FROM payment_transactions
GROUP BY transaction_type
ORDER BY fraud_rate_pct DESC;

-- 4. Geographical fraud analysis
SELECT
    city,
    COUNT(*) AS transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) AS fraud_rate_pct,
    ROUND(SUM(CASE WHEN is_fraud = 1 THEN amount ELSE 0 END), 2) AS fraud_value
FROM payment_transactions
GROUP BY city
ORDER BY fraud_rate_pct DESC;

-- 5. Suspicious transactions
SELECT *
FROM payment_transactions
WHERE anomaly_flag = 1
ORDER BY anomaly_score DESC;

-- 6. High-value fraudulent transactions
SELECT transaction_id, timestamp, amount, merchant_category,
       transaction_type, city, anomaly_score
FROM payment_transactions
WHERE is_fraud = 1
ORDER BY amount DESC
LIMIT 20;

-- 7. Monthly trend
SELECT
    month,
    COUNT(*) AS transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) AS fraud_rate_pct
FROM payment_transactions
GROUP BY month
ORDER BY month;
