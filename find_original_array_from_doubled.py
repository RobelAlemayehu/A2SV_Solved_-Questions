class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        counts = Counter(changed)
        original = []
        
        for x in changed:
            if counts[x] == 0:
                continue
                
            if counts[2 * x] > 0:
                original.append(x)
                counts[x] -= 1
                counts[2 * x] -= 1
            else:
                return []
                
        return original