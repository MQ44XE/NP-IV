f = open('be1.txt', 'r')
print()

K,N,B,L = list(map(int, f.readline().split(" ")))
print(K,N,B,L)
print()

hol_volt = 0
mm = -1

for i in range(N):
    hol, mennyit = list(map(int, f.readline().split(" ")))
    B = B - (hol - hol_volt) / 100 * L + mennyit
    if B > mm:
        mm = B
    hol_volt = hol

print(str(int(mm)))




