class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if nums == [0] * len(nums):
            return '0'

        digits = []

        for num in nums:
            digits.append(str(num))

        digits.sort(key=lambda x: x * 10, reverse=True)

        result = "".join(digits)


        return result