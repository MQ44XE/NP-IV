import sys
import numpy as np
import seaborn as sn

l = [1, 2, 4]
print(l*2)
print(l+ [7, 8])

a_elso = np.array([[1, 2, 3],[4, 5, 6]])
print(a_elso)
print(a_elso*2)

a = 2.1

if a > 2:
    print("nagyobb, mint 2")
else:
    print("nem nagyobb, mint 2")

b = "szia"
print(type(b))

c = [1, 2, "hello", 4, 5, 6]

for element in c:
    print(element)


d_a = {"kor": 2, "nev": "jack"}

print(d_a.keys())
print(d_a.values())
print(list(d_a.keys()))
print(list(d_a.values()))

for key, value in d_a.items():
    print()
    print(key, value)


a = a + 1
a = a + c[0]
#print(a)
sys.exit()

#print(c[-2:])
#print(c[0:2])
#print(type(c))
#print(type(d_a))
#print(type(c[2]))
#print((d_a["nev"]))

def elso_fv(a, b):
    a = a + 1
    return a + b

#print(elso_fv(a,c[0]))