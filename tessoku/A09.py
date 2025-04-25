import numpy as np

arg = input().split()

H, W, N = int(arg[0]), int(arg[1]), int(arg[2])

X = []
for n in range(N):
    x = input().split()
    X.append([int(i) for i in x])

res = np.zeros((H, W))
for x in X:
    a = x[0] - 1
    b = x[1] - 1
    c = x[2] - 1
    d = x[3] - 1
    for h in range(a, c+1):
        for w in range(b, d+1):
            res[h, w] += 1
    
print(res)
