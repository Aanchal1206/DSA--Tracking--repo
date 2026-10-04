class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)

        for length in range(1, n):
            if n % length == 0:
                pattern = s[:length]

                if pattern * (n // length) == s:
                    return True

        return False