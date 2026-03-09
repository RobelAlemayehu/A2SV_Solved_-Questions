class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []

        for ch in s:
            if ch.isalnum():
                stack.append(ch)
            elif ch == '*':
                stack.pop()

        return "".join(stack)