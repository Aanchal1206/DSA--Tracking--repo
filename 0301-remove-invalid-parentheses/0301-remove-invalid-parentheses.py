class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_remove = right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(i, left_remove, right_remove, balance, path):
            if i == len(s):
                if left_remove == 0 and right_remove == 0 and balance == 0:
                    result.add("".join(path))
                return

            ch = s[i]

            if ch == '(':
                if left_remove > 0:
                    backtrack(
                        i + 1, left_remove - 1, right_remove,
                        balance, path
                    )

                path.append(ch)
                backtrack(
                    i + 1, left_remove, right_remove,
                    balance + 1, path
                )
                path.pop()

            elif ch == ')':
                if right_remove > 0:
                    backtrack(
                        i + 1, left_remove, right_remove - 1,
                        balance, path
                    )

                if balance > 0:
                    path.append(ch)
                    backtrack(
                        i + 1, left_remove, right_remove,
                        balance - 1, path
                    )
                    path.pop()

            else:
                path.append(ch)
                backtrack(
                    i + 1, left_remove, right_remove,
                    balance, path
                )
                path.pop()

        backtrack(0, left_remove, right_remove, 0, [])
        return list(result)