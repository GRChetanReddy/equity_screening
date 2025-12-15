import pandas as pd

def build_equal_weight_portfolio(selected_stocks):
    if len(selected_stocks) == 0:
        return {}

    weight = 1 / len(selected_stocks)
    return {stock: weight for stock in selected_stocks}
