import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

from np6het2sav import Option

filename = "KO.csv"
df = pd.read_csv(filename)

print(df.describe()) # adott oszlopok mutatószámai
print(df.columns)
# Open interest: összesen mennyi kontraktot nyitottak meg
# mid : Best bid és Best offer átlag

# CALC time to expiry
df["date"] = pd.to_datetime(df["date"])
df["expiry"] = pd.to_datetime(df["expiry"])
df["daysToExp"] = (df.expiry - df.date).dt.days
df = df.set_index("date")
print(df[:6])


# Plot forward price vs time
df.groupby(df.index).forward_price.median().plot()
plt.show()

# Calc implied vola and greeks
def calcVolaMid(row):
    opt = Option(row.cp_flag, row.strike, row.expiry, 1)
    if row.forward_price * row.daysToExp * row.mid > 0:
        return opt.calcVola(row.forward_price, row.daysToExp / 365, row.mid)
    else:
        return np.nan

df0 = df[df.index<"2018-03-01"]

# Calc vola: takes a few minutes
df0.loc[:, "implied_vola_mid"] = df0.apply(calcVolaMid, axis=1)
#print(df0)

# Volatility smile
dates = df0.index.unique()
# example:
df_ = df0[df0.index == dates[23]]
df_ = df0[df0.daysToExp == 102]
# Filtering out lagged data
df_ = df_[df_.last_date == "2018-02-05"]
df_.groupby(df_.strike).implied_vola_mid.median().plot()
plt.show()