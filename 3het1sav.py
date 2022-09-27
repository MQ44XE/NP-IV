import numpy as np
import seaborn as sns


expected_returns = np.array([0.1, 0.05])
vols = np.array([0.2, 0.1])
numOfPath = 20


def generated_returns(expected_returns, vols, numOfPath):
    a_exp_rets = expected_returns - ((vols**2)/2)
    num_of_assets = len(expected_returns)
    rets = np.random.normal(a_exp_rets, vols, (numOfPath, num_of_assets))

    return rets

a_rets = generated_returns(expected_returns, vols, numOfPath)
#print(a_rets)

def correlated_std_norm(corr_mat, numOfPath):
    a_corr = np.array(corr_mat)
    a_l = np.linalg.cholesky(a_corr)
    num_of_assets = a_corr.shape[0]
    a_uncorr = np.random.normal(size=(numOfPath, num_of_assets))
    # create correlate std normal
    a_corr = np.dot(a_uncorr, a_l.transpose())

    return a_corr

def test_correlated_std_norm():
    corr_mat = [[1.0, -0.8], [-0.8, 1.0]]
    a_corr = correlated_std_norm(corr_mat, 10000)
    print(np.corrcoef(a_corr.transpose()))
    # print(correlated_std_norm(corr_mat, 100))
    # print(np.matmul(a_l, a_l.transpose()))

test_correlated_std_norm()

def correlated_norm(exp_values, stds, corr_mat, numOfPath):
    a_corr = correlated_std_norm(corr_mat, numOfPath)
    a_res = a_corr * np.array(stds) + np.array(exp_values)

    return a_res

def test_correlated_norm():
    corr_mat = [[1.0, -0.8], [-0.8, 1.0]]
    exp_values = [0.08, 0.0495]
    stds = [0.2, 0.1]
    a_res = correlated_norm(exp_values, stds, corr_mat, 2000)
    print(a_res.mean(axis=0))

test_correlated_norm()
