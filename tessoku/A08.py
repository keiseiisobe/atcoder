arg = input().split()

H, W = int(arg[0]), int(arg[1])

X = []
for h in range(H):
    x = input().split()
    X.append([int(i) for i in x])

Q = int(input())

A = []
for q in range(Q):
    a = input().split()
    A.append([int(i) for i in a])

for a in A:
    ai = a[0]
    bi = a[1]
    ci = a[2]
    di = a[3]

    height = ci - ai + 1
    width = di - bi + 1

    sum = 0
    for h in range(ai, ci+1):
        for w in range(bi, di+1):
            sum += X[h - 1][w - 1]
            
    print(sum)
