class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        def four(n):
            if n == 1:
                return True
            
            if n < 1:
                return False

            return four(n / 4)

        return four(n)





        