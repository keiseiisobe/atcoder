arg = input().split()

N, M = int(arg[0]), int(arg[1])
As = [int(arg[i]) for i in range(2, N+2)]
Bs = [int(arg[i]) for i in range(N+2, N+M+2)]

res = {}
for i, a in enumerate(As):
    for j, b in enumerate(Bs):
        if b >= a:
            Bs[j] = -1
            res[j] = i + 1

print(res)
