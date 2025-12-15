import yfinance as yf
import pandas as pd

def get_price_data(ticker, period="2y"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df

def get_fundamentals(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    fundamentals = {
        "pe_ratio": info.get("trailingPE"),
        "roe": info.get("returnOnEquity"),
        "de_ratio": info.get("debtToEquity"),
        "market_cap": info.get("marketCap")
    }
    return fundamentals
