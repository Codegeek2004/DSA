def max_ele(v, i):
    if i == len(v) - 1:
        return v[i]
    return max(v[i], max_ele(v, i + 1))

n = int(input("Enter the number: "))
v = []
for i in range(n):
    t = int(input())
    v.append(t)

print(max_ele(v, 0))
