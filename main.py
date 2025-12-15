from data_fetch import get_price_data, get_fundamentals
from indicators import add_technical_indicators
from screening import fundamental_filter, technical_filter
from portfolio import build_equal_weight_portfolio
from backtest import backtest_portfolio
import matplotlib.pyplot as plt

# Example NIFTY stocks (replace / expand if needed)
stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS"]

selected_stocks = {}
price_data = {}

for stock in stocks:
    fundamentals = get_fundamentals(stock)
    if not fundamental_filter(fundamentals):
        continue

    df = get_price_data(stock)
    df = add_technical_indicators(df)

    if technical_filter(df):
        selected_stocks[stock] = df
        price_data[stock] = df

portfolio = build_equal_weight_portfolio(selected_stocks.keys())

cumulative_return, metrics = backtest_portfolio(price_data, portfolio)

print("Portfolio Metrics:")
for k, v in metrics.items():
    print(f"{k}: {v:.2f}")

cumulative_return.plot(title="Portfolio Cumulative Returns")
plt.show()
