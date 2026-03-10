t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    word = input()

    whites = 0 # 1 0 

    i, j = 0, 0 # 0, 1 0, 2  1, 1 
    mini = n # 1

    while j < n:
        if word[j] == 'W':
            whites += 1

        if j - i + 1 < k:
            j += 1
            continue
        
        mini = min(mini, whites)

        j += 1
        if word[i] == 'W':
            whites -= 1

        i += 1


    print(mini)