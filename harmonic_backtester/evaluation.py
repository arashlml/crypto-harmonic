import numpy as np
import pandas as pd

def evaluate_signal(df_prices: pd.DataFrame, signal: dict, max_horizon: int = 200):
    ts = pd.Timestamp(signal["timestamp"])
    strike = signal["strike"]
    stop = signal["stop"]
    target = signal["target"]
    bullish = signal["bullish"]

    # --- FIX timezone issue ---
    if df_prices.index.tz is not None:
        if ts.tzinfo is None:
            ts = ts.tz_localize(df_prices.index.tz)
        else:
            ts = ts.tz_convert(df_prices.index.tz)
    # ---------------------------

    future = df_prices[df_prices.index > ts].head(max_horizon)
    if future.empty:
        return {"result": np.NAN , "return": 0.0}

    if bullish:
        for _, row in future.iterrows():
            if row["low"] <= stop:
                return {"result": "stop", "return": (stop - strike) / strike}
            if row["high"] >= target:
                return {"result": "t1", "return": (target - strike) / strike}
    else:
        for _, row in future.iterrows():
            if row["high"] >= stop:
                return {"result": "stop", "return": (strike - stop) / strike}
            if row["low"] <= target:
                return {"result": "t1", "return": (strike - target) / strike}

    return {"result": np.NAN, "return": 0.0}



def evaluate_all(df_prices: pd.DataFrame, df_signals: pd.DataFrame, max_horizon: int = 200):
    results = []
    for _, sig in df_signals.iterrows():
        res = evaluate_signal(df_prices, sig.to_dict(), max_horizon)
        results.append(res)
    if len(results) == 0:
        raise Exception("Not enough data to evaluate")
    results=pd.DataFrame(results)
    results.to_csv("results.csv")
    return results.dropna()
