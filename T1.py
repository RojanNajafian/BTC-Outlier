import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = yf.download("BTC-USD", start="2015-01-01", end="2024-12-29")

price = dataframe["Close"]

mean = float(price.mean())
std = float(price.std())

upper_bound = mean + 2 * std
lower_bound = mean - 2 * std

outliers = price[(price > upper_bound) | (price < lower_bound)]

print(outliers)

plt.figure(figsize=(12, 6))
plt.plot(price, label="BTC Price")
plt.axhline(y=upper_bound, color='red', linestyle="--", label="Upper bound")
plt.axhline(y=lower_bound, color='blue', linestyle="--", label="Lower bound")
plt.scatter(outliers.index, outliers, color='green', label="Outliers")

plt.legend()
plt.show()
