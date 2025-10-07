# harmonic_backtester/metrics.py
import pandas as pd
import numpy as np

def compute_statistics(df_results: pd.DataFrame):
    win_rate = ((df_results["result"] != "stop").mean())*100
    avg_return = df_results["return"].mean()
    profit_factor = df_results.loc[df_results["return"] > 0, "return"].sum() / abs(
        df_results.loc[df_results["return"] < 0, "return"].sum()
    )
    sharpe = df_results["return"].mean() / (df_results["return"].std() + 1e-9)
    if df_results.loc[df_results["return"]<0,'return'] == 0:
        risk_to_reward = 'No negative return'
    else:
        risk_to_reward= (df_results.loc[df_results["return"]>0,'return'].mean())/-(df_results.loc[df_results["return"]<0,'return'].mean())

    return {
        "win_rate": round(win_rate, 3),
        "avg_return": round(avg_return, 4),
        "profit_factor": round(profit_factor, 3),
        "sharpe_ratio": round(sharpe, 3),
        "risk_to_reward": round(risk_to_reward, 3),
    }
