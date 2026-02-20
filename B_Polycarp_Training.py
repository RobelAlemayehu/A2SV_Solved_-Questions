n = int(input())
a = list(map(int, input().split()))


a.sort()
counter = 1


for i in range(n):
    if a[i] >= counter:
        counter += 1
print(counter - 1)