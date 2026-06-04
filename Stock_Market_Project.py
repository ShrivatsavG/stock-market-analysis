# Introduction
# Stock prices change every day due to various market and economic factors.
# Analyzing historical stock data helps us understand trends and identify patterns.

import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

df = pd.read_csv("TATAMOTORS.csv")
print(df.head())

print(df.info())
print("\nColumns in Dataset:")
print(df.columns)

df['Date'] = pd.to_datetime(df['Date'])
print(df[['Date', 'Close']].head())

print(df.isnull().sum())

print(df.describe())

plt.figure(figsize=(12,6))

plt.plot(df['Date'], df['Close'])

plt.title("Tata Motors Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.show()

df['MA50'] = df['Close'].rolling(window=50).mean()

plt.figure(figsize=(12,6))

plt.plot(df['Date'], df['Close'], label='Closing Price')
plt.plot(df['Date'], df['MA50'], label='50-Day Moving Average')

plt.title("Closing Price vs 50-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

df['Daily_Return'] = df['Close'].pct_change()
print(df[['Date', 'Daily_Return']].head())

plt.figure(figsize=(10,6))
plt.hist(df['Daily_Return'].dropna(), bins=30)
plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close'], linewidth=1)
plt.title("Historical Closing Price Trend of Tata Motors")
plt.xlabel("Year")
plt.ylabel("Closing Price (INR)")
plt.grid(True, alpha=0.3)
plt.show()

print("Project completed successfully!")
