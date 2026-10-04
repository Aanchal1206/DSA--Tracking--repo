class Solution:
    def maskPII(self, s):
        if '@' in s:
            name, domain = s.split('@')

            name = name.lower()
            domain = domain.lower()

            return name[0] + "*****" + name[-1] + "@" + domain

        digits = ''.join(c for c in s if c.isdigit())

        country = len(digits) - 10
        local = digits[-10:]

        result = "***-***-" + local[-4:]

        if country > 0:
            result = "+" + "*" * country + "-" + result

        return result