import yfinance as yf

# Your portfolio: symbol -> number of shares
portfolio = {
    'AAPL': 10,
    'GOOGL': 5,
    'TSLA': 2,
    'MSFT': 7
}

def get_portfolio_value(portfolio):
    total_value = 0
    print("\n--- Portfolio Summary ---")
    for symbol, shares in portfolio.items():
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")['Close'][0]
        value = shares * price
        total_value += value
        print(f"{symbol}: {shares} shares x ${price:.2f} = ${value:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    get_portfolio_value(portfolio)