class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n =  len(nums)
        count = Counter(nums)
        dominant = -1
        freq = 0

        for num, c in count.items():
            if c * 2 > n:
                dominant = num
                freq = c
                break 
        
            
        left_freq = 0

        for i in range(n - 1):
            if nums[i] == dominant:
                left_freq += 1

            left = left_freq * 2 > (i + 1)
            right = (freq - left_freq) * 2 > (n - i - 1)

            if left and right:
                return i
        return -1
