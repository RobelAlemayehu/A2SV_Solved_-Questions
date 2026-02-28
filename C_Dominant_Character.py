t = int(input())

for _ in range(t):
  
  n = int(input())
  words = input()

  if "aa" in words:
    print(2)
    continue
  elif "aba" in words or "aca" in words:
    print(3)
    continue
  elif "acba" in words or "abac" in words or "acab" in words or "abca" in words:
    print(4)
    continue
  elif "abbaca" in words or "accaba" in words:
    print(6)
    continue
  elif "abbacca" in words or "accabba" in words:
    print(7)
    continue
  else:
    print(-1)
    continue




