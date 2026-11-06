from collections import defaultdict

class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        ans = [0] * len(queries)
        count = defaultdict(int)

        left = right = 0

        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        for q, idx in sorted_queries:
            start = q - x

            # Add logs up to query time
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                count[server] += 1
                right += 1

            # Remove logs before window start
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            ans[idx] = n - len(count)

        return ans