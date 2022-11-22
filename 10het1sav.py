import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns

# Modern Portfolio Theory

price_hist_df = pd.read_csv("Price_history.csv", index_col=0)

# one-liner list comp

#price_hist_df.columns = ['BLK', 'KO', 'GE', 'ATVI', 'JPM']
price_hist_df.columns = [colname.replace("_price","") for colname in price_hist_df.columns]
price_hist_df.index = pd.to_datetime(price_hist_df.index)

price_hist_df.fillna(method="ffill") # NaN értékeket a következő értékkel helyettesíti

# 1. írjunk függvényt, ami kiszámolja a fontosabb eszközmetrikákat
# - return
# - várható return
# - std (szórás) return
# - cov return
# - corr return

def asset_metrics(price_df):
    return_asset = price_df / price_df.shift(1)-1
    mean_asset = return_asset.mean() * 12
    std_asset = return_asset.std() * np.sqrt(12)
    cov_asset = return_asset.cov() * 12
    corr_asset = return_asset.corr()
    return return_asset, mean_asset, std_asset, cov_asset, corr_asset

return_asset, mean_asset, std_asset, cov_asset, corr_asset = asset_metrics(price_hist_df)

return_asset_ext = return_asset.copy()
return_asset_ext["Pre-2015"] = return_asset_ext.index.year<2015

# plt.scatter(return_asset["BLK"], return_asset["KO"])
# plt.suptitle("BLK és KO hozamok")
# plt.show()

# sns.pairplot(return_asset_ext, hue="Pre-2015")
# plt.show()


# 2. Portfolio 2 eszközre
# - függvény (várh hozam, kock) 2 eszközre
# - ábrázoljuk kül súlyozás mellett

def calc_2asset_mean_std(w1, w2, ret1, ret2, sd1, sd2, corr):
    ptf_return = w1*ret1+w2*ret2
    ptf_sd = w1**2 * sd1**2 + w2**2 * sd2**2
    ptf_sd = ptf_sd + 2 * w1*w2*sd1*sd2*corr # vagy ptf_sd += 2 * w1*w2*sd1*sd2*corr
    ptf_sd = np.sqrt(ptf_sd)
    return ptf_return, ptf_sd

w1s = np.linspace(-1, 1, 11)
twoassetptf_dict = {}

for w1 in w1s:
    ptf_return, ptf_sd = calc_2asset_mean_std(w1, 1-w1, mean_asset["BLK"], mean_asset["JPM"], std_asset["BLK"], std_asset["JPM"], corr_asset.loc["BLK", "JPM"])
    twoassetptf_dict[w1] = (ptf_return, ptf_sd)
twoassetptf_df = pd.DataFrame(twoassetptf_dict).transpose()
twoassetptf_df.columns = ["Portfolio Return", "Portfolio Std.Dev."]

twoassetptf_df.plot(x = "Portfolio Std.Dev.", y = "Portfolio Return")
# plt.show()

# 3. Portfolio n eszközre hozam, kockázat
# - függvény

def calc_nasset_mean(w, mean_return):
    return np.sum(w * mean_return)

def calc_nasset_std(w, cov_matrix):
    return np.sqrt(np.dot(np.dot(w, cov_matrix), w.transpose()))

def calc_nasset_mean_std(w, mean_return, cov_matrix):
    ret = calc_nasset_mean(w, mean_return)
    std = calc_nasset_std(w, cov_matrix)
    return ret, std

calc_nasset_mean_std(np.array([1, 0, 0, 0, 0]), mean_asset, cov_asset)

grid = np.array(np.meshgrid(w1s, w1s, w1s, w1s))
grid = grid.reshape((4, -1)).transpose()
grid = np.c_[grid, 1-grid.sum(axis=1)]

nsasset_mean_std = []
for i in range(grid.shape[0]):
    ret, std = calc_nasset_mean_std(grid[i], mean_asset, cov_asset)
    nsasset_mean_std.append((ret, std))

nsasset_mean_std_df = pd.DataFrame(nsasset_mean_std)
nsasset_mean_std_df.columns = ["Portfolio Return", "Portfolio Std.Dev."]
nsasset_mean_std_df.plot.scatter(x="Portfolio Std.Dev.", y="Portfolio Return")
plt.show()

# 4. Optimalizáció
# - Std Dev minimalizálása adott hozamszint mellett
# - constraintek megadása

return_target = 0.2
cons = ({"type": "eq", "fun": lambda weight: return_target - calc_nasset_mean(weight, mean_asset)},
        {"type": "eq", "fun": lambda weight: np.sum(weight)-1})
# eq = equality, fun = function

sp.optimize.minimize(calc_nasset_std, np.array([1, 0, 0, 0, 0]), args = (cov_asset), constraints=cons)

pass
