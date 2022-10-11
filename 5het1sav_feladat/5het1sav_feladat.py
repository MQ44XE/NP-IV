import pandas as pd

df_funds = pd.read_csv("fundamentals.csv")
df_prices = pd.read_csv("prices.csv")
df_psplit = pd.read_csv("prices-split-adjusted.csv")
df_secs = pd.read_csv("securities.csv")

print(df_prices)