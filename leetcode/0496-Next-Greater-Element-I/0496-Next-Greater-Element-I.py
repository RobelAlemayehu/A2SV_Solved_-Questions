class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stay in the stack until bigger element is found

        stack = []
        greater = defaultdict(lambda: -1)

        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] =  num
            stack.append(num)
        print(stack)

        return [greater[num] for num in nums1]