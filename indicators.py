import pandas as pd
from ta.trend import SMAIndicator, EMAIndicator
from ta.momentum import RSIIndicator

def add_technical_indicators(df):
    df = df.copy()

    df["sma_50"] = SMAIndicator(df["Close"], 50).sma_indicator()
    df["sma_200"] = SMAIndicator(df["Close"], 200).sma_indicator()
    df["ema_20"] = EMAIndicator(df["Close"], 20).ema_indicator()
    df["rsi"] = RSIIndicator(df["Close"], 14).rsi()

    return df
