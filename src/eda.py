from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
IN = ROOT / "data" / "processed" / "fraud_analysis_data.csv"
OUT = ROOT / "reports" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(IN)

def save_bar(series, title, filename, xlabel):
    ax = series.sort_values(ascending=False).plot(kind="bar", figsize=(10,5))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Fraud Rate")
    plt.tight_layout()
    plt.savefig(OUT/filename, dpi=160)
    plt.close()

fraud_by_cat = df.groupby("merchant_category")["is_fraud"].mean()
save_bar(fraud_by_cat, "Fraud Rate by Merchant Category",
         "fraud_rate_by_merchant_category.png", "Merchant Category")

fraud_by_type = df.groupby("transaction_type")["is_fraud"].mean()
save_bar(fraud_by_type, "Fraud Rate by Transaction Type",
         "fraud_rate_by_transaction_type.png", "Transaction Type")

daily = df.groupby("transaction_date").agg(
    transactions=("transaction_id","count"),
    fraud_transactions=("is_fraud","sum")
)
daily["fraud_rate"] = daily["fraud_transactions"]/daily["transactions"]
ax = daily["fraud_rate"].plot(figsize=(11,5))
ax.set_title("Daily Fraud Rate")
ax.set_xlabel("Date")
ax.set_ylabel("Fraud Rate")
plt.tight_layout()
plt.savefig(OUT/"daily_fraud_rate.png", dpi=160)
plt.close()

print("EDA charts saved to reports/figures/")
