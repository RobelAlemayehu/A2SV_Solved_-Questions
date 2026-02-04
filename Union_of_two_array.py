class Solution:    
    def findUnion(self, a, b):
        res = []
        
        seen = set()
        
        for item in (a + b):
            if item not in seen:
                res.append(item)
            seen.add(item)
        
        return res 