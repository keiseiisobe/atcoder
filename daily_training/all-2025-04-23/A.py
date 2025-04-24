arg = input().split()

N = int(arg[0])
eval = arg[1]

if "o" in eval and not "x" in eval:
    print("Yes")
else:
    print("No")

