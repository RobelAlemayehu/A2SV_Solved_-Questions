#User function Template for python3

class Solution:
    def isSubset(self, a, b):
        a.sort()
        b.sort()
        
        i, j = 0,0
        
        while j < len(a) and i < len(b):
            if a[j] == b[i]:
                i += 1
                j += 1
            else:
                j += 1
                
        if i == len(b):
            return True
        else:
            return False
    
    
    
    
