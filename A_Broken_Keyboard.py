t = int(input())

for _ in range(t):
    s = input().strip()
    i = 0
    functional = set()
    
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            i += 2
        else:
            functional.add(s[i])
            i += 1
    
    print("".join(sorted(functional)))