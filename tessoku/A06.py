arg1 = input().split()
arg2 = input().split()

N, Q = int(arg1[0]), int(arg1[1])
A = [int(i) for i in arg2]

qs = []
for i in range(Q):
    line = input().split()
    L = int(line[0])
    R = int(line[1])
    qs.append([L, R])

for q in qs:
    begin = q[0]
    end = q[1]
    print(sum(A[begin-1:end]))
    
