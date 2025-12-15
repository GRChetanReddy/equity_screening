def fundamental_filter(fundamentals):
    if fundamentals["pe_ratio"] is None:
        return False
    if fundamentals["roe"] is None:
        return False

    return (
        fundamentals["pe_ratio"] < 30 and
        fundamentals["roe"] > 0.15 and
        (fundamentals["de_ratio"] is None or fundamentals["de_ratio"] < 1)
    )

def technical_filter(df):
    latest = df.iloc[-1]

    return (
        latest["sma_50"] > latest["sma_200"] and
        latest["Close"] > latest["ema_20"] and
        40 < latest["rsi"] < 70
    )
