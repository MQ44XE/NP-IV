import numpy as np
import matplotlib.pyplot as plt

def osszead(a,b=0):
    return print(a+b)
# default value függvény, def value csak végén lehet
osszead(5)
print()


r_eff = np.array([[0.1,0.2],[0.3,0.4],[0.5,0.6]])
print(r_eff)
print(type(r_eff))
print()

ic = np.exp(r_eff)
print(ic)
print()

ic_2y = ic**2
print(ic_2y)
# ic^2
print()
r_2y = np.log(ic_2y)
print(r_2y)
print()

print(r_eff.shape)
# mátrix dimenzió
print()

a_elso = np.array([[1,2],[2,5],[2,8]])
print(a_elso)
print()
# átlag, összeg, kumulálás, min, max, szórás

print(np.sum(a_elso))
print(np.sum(a_elso, axis=0))
print(np.sum(a_elso, axis=1))
print()

print(np.mean(a_elso, axis=0))
print()
print(np.std(a_elso, axis=0))
print()
print(np.min(a_elso, axis=0))
print()
print(np.max(a_elso, axis=0))
print()
print(np.diff(a_elso, axis=0))
print()

b_diff = np.diff(a_elso, axis=1)
print(b_diff.shape)
print(b_diff)
print()

c = a_elso - np.mean(a_elso)
# centralizálás
print(c)
print(np.mean(c))
print(c.mean())
print()

is_pos = c > 0
# indexing
print(is_pos)
print()

d = c.copy()
e = c.copy()
d[is_pos] = d[is_pos] + 100
e[~is_pos] = e[~is_pos] + 100
print(d)
print(e)
print(c)
print()

a_new = np.array([[2,2],[2,4],[0,4]])
print(a_new)
print(a_new.std(axis=1, ddof=0))
print(a_new.std(axis=1, ddof=1))
print()

# random numbers (GPT-3, DALL-E)
a_rnd = np.random.random((3,2))
print(a_rnd)
np.random.seed(112)
a_rnd_uniform = np.random.random((3,2))
print(a_rnd_uniform)
print()
a_rnd_normal = np.random.normal([1, 8.2], [1, 1], (10, 2))
print(a_rnd_normal)
print()

# Feladat
# mu1=5% mu2=10% sig1=10% sig2=20% 10000x2-es mátrixban

a_r = np.random.normal([0.05, 0.1], [0.1, 0.2], (10000, 2))
print(a_r)
a_initial_price = np.array([[50, 100]])
print(a_initial_price.shape)
a_price = a_initial_price * np.exp(a_r)
print()

# matplotlib.pyplot
plt.hist(a_price[:, 0], bins=100)
plt.hist(a_price[:, 1], bins=100)
plt.figure()
plt.scatter(a_price[:, 0], a_price[:, 1])
plt.show()

# list comprehension
l_uj = [x*2 for x in range(5)]
print(l_uj)