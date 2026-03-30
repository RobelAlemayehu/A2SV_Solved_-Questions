class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n  = len(s)
        difference = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                difference[end + 1] += 1
                difference[start] -= 1
            else:
                difference[end + 1] -= 1
                difference[start] += 1

        diff = 0
        result = [ord(c) - ord("a") for c in s]
        for i in reversed(range(n + 1)):

            diff += difference[i]
            result[i -  1] =  (diff + result[i - 1]) % 26


        s = [chr(ord("a") + n) for n in result]
        return "".join(s)