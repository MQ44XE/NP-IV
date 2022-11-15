import numpy as np
from scipy.stats import norm

# Opció árazás
class Option:
    def __init__(self, right:str, strike:float, expiry:str, pos:int):
        # right = call or put
        # pos = long(1) or short(-1)
        # strike = kötési árfolyam
        self.right = right
        self.pos = pos
        self.strike = strike
        self.expiry = expiry
        self.vola = np.nan
    def calcPrice(self, S:float, timeToExp:float, vola:float, rate:float):
        if not np.isnan(vola):
            IV = vola
        else:
            IV = self.vola if not np.isnan(self.vola) else self.initVola
        if np.isnan(IV):
            print("Vola is not set")
            return np.nan
        t = timeToExp
        if t > 0:
            d1 = (np.log(S / self.strike) + (rate + IV ** 2 / 2) * t) / (IV * np.sqrt(t))
            d2 = d1 - IV * np.sqrt(t)
            if self.right == 'C':
                return (S * norm.cdf(d1) - norm.cdf(d2) * self.strike * np.exp(-rate * t)) * self.pos
            else:
                return (norm.cdf(-d2) * self.strike * np.exp(-rate * t) - S * norm.cdf(-d1)) * self.pos
        elif t == 0:
            return self.calcPayoff(S)
        else:
            print("expired!")
            return np.nan

    def initVola(self):
        self.vola = 0.2

    def calcPayoff(self, spot:float) -> float:
        if self.right == "C":
            return max(spot-self.strike, 0) * self.pos
        elif self.right == "P":
            return max(self.strike-spot, 0) * self.pos
        else:
            print("Wrong Option Type")
            return None


opt = Option("C", 100, "20221215", 1)
print(opt.calcPrice(110, 0.5, 0.3, 0.04))