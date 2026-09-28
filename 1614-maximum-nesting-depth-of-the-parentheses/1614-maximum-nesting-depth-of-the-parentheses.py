class Solution:
    def maxDepth(self, s: str) -> int:
        current = 0
        maximum = 0

        for ch in s:
            if ch == '(':
                current += 1
                maximum = max(maximum, current)

            elif ch == ')':
                current -= 1

        return maximum