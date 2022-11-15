import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_daily_risk_free_rate():
    df = pd.read_csv("DTB3.csv")
    df.index = pd.to_datetime(df["DATE"])
    df = df[["DTB3"]]
    df.columns = ["risk_free_daily"]
    msk = df["risk_free_daily"] != "."
    df = df[msk]
    df = df.astype(float)
    df = df / 252

    return df

# df = get_daily_risk_free_rate()
# print(df)

filename = "BRK-B.csv"
df = pd.read_csv(filename)

df["ret_log_daily"] = np.log(df["Adj Close"]/df["Adj Close"].shift(1))
print(df)

df.index = pd.to_datetime(df["Date"])
df_risk_free = get_daily_risk_free_rate()
df_joined = df.join(df_risk_free)
df["ret_log_daily_exc"] = df["ret_log_daily"] - df["risk_free_daily"]
df["ret_log_daily"].plot()
plt.show()

df["vol_rolling1y"] = df["ret_log_daily"].rolling(252).std()
df["vol_rolling2y"] = df["ret_log_daily"].rolling(504).std()
df[["vol_rolling1y", "vol_rolling2y"]].plot()
plt.show()

t_day_in_year = 252
vol_windows_in_y = [0.25, 1, 3, 10]
cols_vol, cols_ret, cols_beta = [], [], []
for year in vol_windows_in_y:
    col_vol = "vol_" + str(year) + "y"
    col_ret = "ret_yearly_" + str(year) + "y"
    col_ret = "ret_yearly_" + str(year) + "y"

    cols_vol.append(col_vol)
    cols_ret.append(col_ret)
    df[col_vol] = np.sqrt(t_day_in_year) * df["ret_log_daily"].rolling(int(year * t_day_in_year)).std()
    df[col_ret] = t_day_in_year * df["ret_log_daily"].rolling(int(year * t_day_in_year)).mean()
df["ret_log_daily"].plot()
df["cols_vol"].plot()
plt.show()

