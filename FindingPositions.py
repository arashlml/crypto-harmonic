from pyharmonics import  Position, Technicals
from pyharmonics.marketdata import  BinanceCandleData
from pyharmonics.search import HarmonicSearch


def find_positions(symbol,intervals,horizon):
    y = BinanceCandleData()
    y.get_candles(symbol,intervals,horizon)
    t = Technicals(y.df, y.symbol, y.interval)
    m = HarmonicSearch(t)
    m.search()
    patterns = m.get_patterns(family=m.XABCD)
    positions=[]
    for pattern in patterns['XABCD']:
        position = Position(pattern,  pattern.y[-1], 1000)
        positions.append(position)
    return positions

