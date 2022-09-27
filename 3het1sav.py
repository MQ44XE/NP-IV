import numpy as np
import seaborn as sns


rs = np.array([0.1, 0.05])
vols = np.array([0.2, 0.1])
numOfPath = 20

def generated_returns(r_exp, vols, numOfPath):
    num_of_assets = len(r_exp)
    rets = np.random.normal()
    yields = np.random.normal(r_exp, vols, numOfPath)
    sns.scatterplot(yields)

    return yields
print(generated_returns(r_exp, vols, numOfPath))
