# harmonic_backtester/signals.py
import pandas as pd

def collect_signals(positions: list[dict]) -> pd.DataFrame:
    """
    Convert list of pyharmonics Position objects (dicts) into a clean DataFrame.
    """
    data = []
    for p in positions:
        data.append({
            "symbol": p.symbol,
            "pattern_name": p.pattern.name,
            "bullish": p.pattern.bullish,
            "strike": p.strike,
            "target": p.targets[0],
            "stop": p.stop,
            "timestamp": p.pattern.x[-1],
        })
    signals = pd.DataFrame(data)
    signals.to_csv('signals.csv')
    return pd.DataFrame(data)
