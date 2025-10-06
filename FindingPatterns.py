from pyharmonics.marketdata import BinanceCandleData
from pyharmonics.plotter import Plotter
from pyharmonics.search import HarmonicSearch
from pyharmonics.technicals import Technicals

import os
os.environ["PLOTLY_SERVER_PORT"] = "8050"

def find_harmonic_patterns(symbol,intervals,horizon):
    y = BinanceCandleData()
    y.get_candles(symbol,intervals,horizon)
    t = Technicals(y.df, y.symbol, y.interval)
    m = HarmonicSearch(t)
    m.search()
    patterns = m.get_patterns(family=m.XABCD)
    p = Plotter(technicals=t)
    p.add_harmonic_plots(m.get_patterns(family=m.XABCD))
    return p.main_plot

def main():
    find_harmonic_patterns("BTCUSDT",100000)

if __name__ == "__main__":
    main()