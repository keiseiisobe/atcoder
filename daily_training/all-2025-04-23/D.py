arg = input().split()
M = int(arg[0])
D = [int(arg[i]) for i in range(1, M+1)]

def solve(M, D):
    mid = int((sum(D) + 1) / 2)
    running_sum = 0
    for i in range(M):
        running_sum += D[i]
        if mid <= running_sum:
            return i + 1, D[i] - (running_sum - mid)

m, d = solve(M, D)
print(m, d)
