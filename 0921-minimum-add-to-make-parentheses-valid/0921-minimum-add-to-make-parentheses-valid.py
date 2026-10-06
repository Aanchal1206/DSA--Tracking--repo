class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        add = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    add += 1

        return add + balance