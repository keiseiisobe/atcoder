import numpy as np

N = int(input())

arr = np.zeros(N)
arr[0] = 1
arr[1] = 1

for i in range(2, N):
    arr[i] = (arr[i-1] + arr[i-2]) % 1000000007

print(arr[-1])

