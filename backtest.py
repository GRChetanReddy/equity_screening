import pandas as pd
import numpy as np

def backtest_portfolio(price_data, weights):
    returns = pd.DataFrame()

    for stock, df in price_data.items():
        returns[stock] = df["Close"].pct_change()

    returns = returns.dropna()
    portfolio_returns = sum(returns[stock] * weight for stock, weight in weights.items())

    cumulative_return = (1 + portfolio_returns).cumprod()

    metrics = {
        "total_return": cumulative_return.iloc[-1] - 1,
        "volatility": portfolio_returns.std() * (252 ** 0.5),
        "max_drawdown": (cumulative_return / cumulative_return.cummax() - 1).min()
    }

    return cumulative_return, metrics
