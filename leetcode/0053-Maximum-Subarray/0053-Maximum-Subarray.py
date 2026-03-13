class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            max_sum = max(nums[i], nums[i] + max_sum)
            sum_ = max(max_sum, sum_)

        return sum_