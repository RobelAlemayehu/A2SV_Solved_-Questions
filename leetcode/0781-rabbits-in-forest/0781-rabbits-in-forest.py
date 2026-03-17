class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        result = 0

        count = Counter(answers)

        print(count)

        for answer, freq in count.items():
            same_color = answer + 1

            groups = (freq + answer)  // same_color

            result += groups * same_color


        return result 