arg = input().split()

S, T = arg[0], arg[1]

def separate_str(str, step):
    new_str = []
    for i in range(0, len(str), step):
        new_str.append(str[i:i+step])
    return new_str

def solve(S, T):
    for i in range(1, len(S)):
        str = separate_str(S, i)
        for j in range(0, i):
            res = []
            for raw in range(len(str)):
                if len(str[raw]) <= j:
                    break
                res.append(str[raw][j])
            if T == ''.join(res):
                return "Yes"
    return "No"

print(solve(S, T))
