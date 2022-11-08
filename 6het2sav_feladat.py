import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

from np6het2sav import Option

opt = Option("C", 100, "20221215", 1)
print(opt.calcPayoff(139))

K = 500
expiry = "20221215"
C = Option("C", K, expiry, 1)
P = Option("P", K, expiry, -1)

S = 124.35
t = 0.23
vola = 0.12

print(C.calcPrice(S, t, vola) + P.calcPrice(S, t, vola) - S + K)

# prices vs spot
spots = range(250, 500, 5)
prices = [C.calcPrice(s, 1, vola) for s in spots]
pays = [C.calcPayoff(s) for s in spots]

# plt.plot(spots, prices, spots, pays)
# plt.show()

# 8. HÉT

# set volatility
#opt_c.vola = 0.3
#opt_p.vola = 0.3

# calc price at given spot and time to maturity
#opt_c.calcPrice(362, 1 / 12)
#opt_p.calcPrice(362, 1 / 12)

# check put call parity
S = 362
t = 1 / 12


# Geometriai Brown mozgás

def __init__(self):
    pass

def generate(S0, mu, sigma, T, N):
    # dS = mu*S*dt + sigma*S*dWt
    # S(t+dt) = S(t) * exp( (mu-sigma^2/2)*dt + sigma*sqrt(dt)
    dt = T/N
    X = np.exp((mu - sigma**2/2)*dt + sigma * np.random.normal(0, np.sqrt(dt), N))
    return S0*np.cumprod(X)

sigma = 0.35
N = 250
S0 = 100
spots = generate(S0, 0, sigma, 1, N)
times = np.arange(0, 1, 1/N)
# plt.plot(times, spots)
# plt.show()

opt = Option("C", S0, None, 1)

vola = 0.3
prices = []
deltas = []
for (t,S) in zip(times, spots):
    price = opt.calcPrice(S, 1-t, vola)
    delta = opt.calcDelta(S, 1-t, vola)
    prices.append(price)
    deltas.append(delta)

plt.plot(times, np.array(prices))
plt.show()

# Using Dataframes

df = pd.Dataframe({"time":times, "spot":spots})

K = 100
def calcPrice(row):
    opt = Option("C", K, None, 1)
    vola = 0.3
    return opt.calcPrice(row.spot, 1-row.time, vola)

df["price"] = df.apply(calcPrice, axis=1)