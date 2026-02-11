from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    count_a = 0
    count_b = 0
    count_c = 0

    for ch in s:
        if ch == 'a':
            count_a += 1
        elif ch == 'b':
            count_b += 1
        else:
            count_c += 1


    if count_a > count_b and count_a > count_c:
        