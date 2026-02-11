class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = ""

        for num in nums:
            answer += str(num)

        return [int(ch) for ch in answer]

        

