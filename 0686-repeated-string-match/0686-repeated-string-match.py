class Solution:
    def repeatedStringMatch(self, a, b):
        count = (len(b) + len(a) - 1) // len(a)

        s = a * count

        if b in s:
            return count

        if b in s + a:
            return count + 1

        return -1