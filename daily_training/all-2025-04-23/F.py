arg = input().split()
N, M = int(arg[0]), int(arg[1])

B = []
for n in range(N):
    row = input().split()
    B.append([int(row[i]) for i in range(len(row))])

print(B)

def create_sub_A(i, next_i, j, next_j):
    sub_A = []
    for m in range(next_i - i):
        for n in range(next_j - j):
            sub_A.append([(i - 1) * 7 + j])


for i in range(1, 10**100 + 1):
    for j in range(1, 7 + 1):
        A_value = (i - 1) * 7 + j
        if A_value == B[0][0]:
            sub_A = create_sub_A(i-1, N, j-1, M)
            print(f"sub_A: {sub_A}")
            if sub_A == B:
                print("Yes")
                exit()
print("No")
