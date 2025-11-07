import pandas as pd
import yfinance as yf
import datetime as dt

# === Input your tickers and initial dates ===
data = [
    {"Ticker": "AAPL", "Initial Date": "2025-10-10"},
    {"Ticker": "TSLA", "Initial Date": "2025-09-15"},
    {"Ticker": "MSFT", "Initial Date": "2025-10-01"}
]

df = pd.DataFrame(data)

# === Helper Functions ===
def get_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def analyze_stock(ticker, initial_date):
    start_date = pd.to_datetime(initial_date) - pd.Timedelta(days=30)
    end_date = pd.to_datetime(initial_date) + pd.Timedelta(days=30)

    hist = yf.download(ticker, start=start_date, end=end_date)
    if hist.empty:
        return pd.Series({
            "Initial Price": None, "Final Date": None, "Final Price": None,
            "MA": None, "Lower Bollinger": None, "Upper Bollinger": None,
            "RSI": None, "Percent Change": None
        })

    hist["MA"] = hist["Close"].rolling(window=14).mean()
    hist["STD"] = hist["Close"].rolling(window=14).std()
    hist["Upper"] = hist["MA"] + 2 * hist["STD"]
    hist["Lower"] = hist["MA"] - 2 * hist["STD"]
    hist["RSI"] = get_rsi(hist["Close"])

    # Get initial and final prices
    initial_date = pd.to_datetime(initial_date)
    final_date = initial_date + pd.Timedelta(days=21)

    try:
        initial_price = hist.loc[hist.index.get_loc(initial_date, method='nearest'), "Close"]
    except KeyError:
        initial_price = None

    try:
        final_price = hist.loc[hist.index.get_loc(final_date, method='nearest'), "Close"]
    except KeyError:
        final_price = None

    percent_change = ((final_price - initial_price) / initial_price * 100) if initial_price and final_price else None

    last_row = hist.iloc[-1]

    return pd.Series({
        "Initial Price": initial_price,
        "Final Date": final_date.date(),
        "Final Price": final_price,
        "MA": last_row["MA"],
        "Lower Bollinger": last_row["Lower"],
        "Upper Bollinger": last_row["Upper"],
        "RSI": last_row["RSI"],
        "Percent Change": percent_change
    })

# === Run the Analysis ===
results = df.apply(lambda row: analyze_stock(row["Ticker"], row["Initial Date"]), axis=1)
df = pd.concat([df, results], axis=1)

print(df)
