from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "payment_transactions.csv"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RAW)
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

for c in ["merchant_category","city","device_type","transaction_type","channel"]:
    if c in df:
        df[c] = df[c].fillna("Unknown")

df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(df["amount"].median())
df["failed_attempts"] = pd.to_numeric(df["failed_attempts"], errors="coerce").fillna(0)
df["is_international"] = pd.to_numeric(df["is_international"], errors="coerce").fillna(0).astype(int)
df["is_fraud"] = pd.to_numeric(df["is_fraud"], errors="coerce").fillna(0).astype(int)

df["hour"] = df["timestamp"].dt.hour
df["day_of_week"] = df["timestamp"].dt.day_name()
df["month"] = df["timestamp"].dt.to_period("M").astype(str)
df["is_night"] = ((df["hour"] <= 5) | (df["hour"] >= 23)).astype(int)

df = df.drop_duplicates(subset=["transaction_id"])
df.to_csv(OUT/"clean_transactions.csv", index=False)

print("Rows:", len(df))
print("Fraud rate:", round(df["is_fraud"].mean()*100, 2), "%")
