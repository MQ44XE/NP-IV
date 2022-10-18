import numpy as np
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

plt.plot(spots, prices, spots, pays)
plt.show()