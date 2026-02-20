class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        count = 0

        citations.sort(reverse=True)

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                count += 1


        return count