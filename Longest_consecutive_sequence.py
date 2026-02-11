class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_length = 1
        current_length = 1

        if len(nums) == 0:
            return 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            
            if nums[i] == nums[i + 1] - 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        return max(current_length, max_length)