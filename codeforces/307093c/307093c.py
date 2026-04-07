n, s = map(int, input().split())
a = list(map(int,input().split()))

left = 0

current = 0
result = 0

for right in range(n):

    current += a[right]

    while current > s:
        current -= a[left]

        left += 1

    result += (right - left + 1)


print(result)