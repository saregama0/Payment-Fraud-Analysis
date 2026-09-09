from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
IN = ROOT / "data" / "processed" / "clean_transactions.csv"
OUT = ROOT / "data" / "processed"
df = pd.read_csv(IN)

features = ["amount","failed_attempts","is_international","is_night"]
X = df[features].copy()
X["log_amount"] = np.log1p(X["amount"])
X = X[["log_amount","failed_attempts","is_international","is_night"]]

X = StandardScaler().fit_transform(X)
model = IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42
)
pred = model.fit_predict(X)
score = model.decision_function(X)

df["anomaly_flag"] = (pred == -1).astype(int)
df["anomaly_score"] = -score
df.to_csv(OUT/"fraud_analysis_data.csv", index=False)

print("Anomalies:", int(df["anomaly_flag"].sum()))
print("Fraud transactions:", int(df["is_fraud"].sum()))
