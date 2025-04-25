N = int(input())

A_str = input().split()
A = [int(a) for a in A_str]

D = int(input())

L_R = []
for d in range(D):
    l_r = input().split()
    L_R.append([int(i) for i in l_r])

for lr in L_R:
    l = lr[0] - 1
    r = lr[1] - 1
    sep = A[:l] + A[r+1:]
    print(max(sep))

