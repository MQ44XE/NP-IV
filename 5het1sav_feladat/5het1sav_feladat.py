import pandas as pd

df_funds = pd.read_csv("fundamentals.csv")
df_prices = pd.read_csv("prices.csv")
df_psplit = pd.read_csv("prices-split-adjusted.csv")
df_secs = pd.read_csv("securities.csv")

#print(df_prices)

def process_prices(df):
    df["date"] = df["date"].apply(lambda x: x[:10])
    df_filtered = df[["date", "symbol", "close"]]
    df_pivot = pd.pivot_table(df_filtered, index=["date"], columns=["symbol"], values=["close"])
    df_pivot.columns = df_pivot.columns.droplevel()

    return df_pivot

df_prices_processed = process_prices(df_prices)
df_prices_adjusted_processed = process_prices(df_psplit)

#print(df_prices_adjusted_processed)

def add_effective_return(df):
    df_out = pd.DataFrame()
    for col in df.columns:
        df_out[col + "_effective_return"] = df[col] / df[col].shift(1) - 1
    return df_out

df_prices_processed_with_returns = add_effective_return(df_prices_processed)
df_prices_adjusted_processed_with_returns = add_effective_return(df_prices_adjusted_processed)
#print(df_prices_processed_with_returns)

df_merged = df_prices_processed_with_returns.merge(df_prices_adjusted_processed_with_returns, on="date", suffixes=("_normal", "_adjusted"))
#print(df_merged)

symbols = df_prices_processed.columns
splits = []
for symbol in symbols:
    df_symbol = df_merged[[symbol + "_effective_return_normal", symbol + "_effective_return_adjusted"]]
    difference_array = df_symbol[symbol + "_effective_return_normal"] - df_symbol[symbol + "_effective_return_adjusted"] > 0.001
    if len(df_symbol.loc[difference_array]) > 0:
        splits.append(symbol)

#print(splits, len(splits))
# 1-es feladat válasza hány split a len(), melyik cégeknél a split

# 2-es Feladat

print(df_prices_adjusted_processed_with_returns)
import numpy as np
def add_log_return(df):
    df_out = pd.DataFrame()
    for col in df.columns:
        df_out[col] = np.log(df[col] / df[col].shift(1) - 1)
    return df_out

df_prices_adjusted_log_return = add_log_return(df_prices_adjusted_processed_with_returns)
return_dict = {}
for col in df_prices_adjusted_log_return.columns:
    col_notnull = df_prices_adjusted_log_return.loc[df_prices_adjusted_log_return[col].notnull(), col]
    yearly_return = 255 * col_notnull.mean()
    return_dict[col] = yearly_return
df_secs["yearly_return"] = df_secs["Ticker symbol"].map(return_dict)
sector_avg_returns = df_secs.groupby("GICS Sector").mean()

#print(sector_avg_returns)

df_filtered = df_prices_adjusted_log_return[["A"]]
df_filtered["cumsum"] = df_filtered.cumsum()

import matplotlib.pyplot as plt
df_filtered["cumsum"].plot()
# plt.savefig("A_stock_price.pdf")
plt.show()
