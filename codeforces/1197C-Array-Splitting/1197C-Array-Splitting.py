n, k = map(int, input().split())
a = list(map(int, input().split()))


cost = []
for i in range(n - 1):
    cost.append(a[i + 1] - a[i])

cost.sort()


total = a[-1] - a[0]

for i in range(k - 1):
    total -= cost[-1]
    cost.pop()

print(total)