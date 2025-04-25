import numpy as np

D = int(input())
N = int(input())

L_R = []
for n in range(N):
    line = input().split()
    L_R.append([int(i) for i in line])

res = np.zeros(D)

for l_r in L_R:
    l = l_r[0] - 1
    r = l_r[1]
    for n in range(l, r):
        res[n] += 1
print(res)
