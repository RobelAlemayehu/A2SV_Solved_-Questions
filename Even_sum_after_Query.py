class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        _sum = 0

        for num in nums:
            if num % 2 == 0:
                _sum += num


        result = []
        for value, index in queries:
            num = nums[index]
            nums[index] += value

            if num % 2 == 0 and value % 2 == 0:
                _sum += value

            elif num % 2 != 0 and value % 2 != 0:
                _sum += nums[index]
                
            elif num % 2 == 0 and value % 2 != 2:
                _sum -= num

            result.append(_sum) 

            
        return result