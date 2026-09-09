from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw"
OUT.mkdir(parents=True, exist_ok=True)

def generate(n=5000, seed=42):
    np.random.seed(seed)
    cats = ["Grocery","Electronics","Travel","Fashion","Food & Dining",
            "Entertainment","Healthcare","Utilities","Online Services","Jewelry"]
    types = ["Online","POS","ATM","Bank Transfer","Mobile Wallet"]
    locs = [("Mumbai","India"),("Delhi","India"),("Bengaluru","India"),
            ("Hyderabad","India"),("Chennai","India"),("Pune","India"),
            ("Kolkata","India"),("Ahmedabad","India"),("Jaipur","India"),
            ("Lucknow","India")]

    start = pd.Timestamp("2026-01-01")
    dates = start + pd.to_timedelta(np.random.randint(0,181,n), unit="D")
    times = pd.to_timedelta(np.random.randint(0,86400,n), unit="s")
    ts = dates.normalize() + times

    merchant = np.random.choice(cats,n,p=[.13,.11,.09,.12,.14,.08,.08,.08,.10,.07])
    ttype = np.random.choice(types,n,p=[.30,.27,.10,.16,.17])
    li = np.random.randint(0,len(locs),n)
    city = np.array([locs[i][0] for i in li])
    amount = np.clip(np.random.lognormal(7.0,.8,n),50,250000).round(2)
    hour = ts.hour
    night = ((hour <= 5) | (hour >= 23)).astype(int)
    intl = np.random.binomial(1,.07,n)
    failed = np.random.poisson(.25,n)
    risk = (-4.15 + .000012*amount + .65*night + .55*intl +
            .22*failed + .35*(ttype=="Online") +
            .25*np.isin(merchant,["Electronics","Jewelry"]))
    p = 1/(1+np.exp(-risk))
    fraud = np.random.binomial(1,p)
    if fraud.mean() < .045:
        need = int(.045*n)-int(fraud.sum())
        candidates = np.where(fraud==0)[0]
        fraud[np.random.choice(candidates, max(0,need), replace=False)] = 1

    out = pd.DataFrame({
        "transaction_id":[f"TXN{100000+i}" for i in range(n)],
        "timestamp":ts,
        "transaction_date":ts.date.astype(str),
        "amount":amount,
        "merchant_category":merchant,
        "transaction_type":ttype,
        "city":[locs[i][0] for i in li],
        "country":["India"]*n,
        "channel":np.where(ttype=="POS","In-Store",
                           np.where(ttype=="ATM","ATM",
                                    np.where(ttype=="Mobile Wallet","Mobile","Digital"))),
        "device_type":np.random.choice(["Android","iOS","Windows","MacOS"],n,p=[.42,.28,.18,.12]),
        "is_international":intl,
        "failed_attempts":failed,
        "is_fraud":fraud
    })
    out.to_csv(OUT/"payment_transactions.csv", index=False)
    print(f"Created {len(out)} transactions at {OUT/'payment_transactions.csv'}")

if __name__ == "__main__":
    generate()
