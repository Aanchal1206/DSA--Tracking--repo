
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]],
                       s: str, queries: list[str]) -> list[bool]:

        # 1. Build the tree
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 2. DFS: parent, depth, and Euler tour intervals
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, False)]

        while stack:
            u, p, exiting = stack.pop()

            if not exiting:
                parent[u] = u if p == -1 else p
                depth[u] = 0 if p == -1 else depth[p]
                if p != -1:
                    depth[u] += 1

                tin[u] = timer
                timer += 1

                stack.append((u, p, True))
                for v in reversed(adj[u]):
                    if v != p:
                        stack.append((v, u, False))
            else:
                tout[u] = timer

        # 3. Binary lifting table for LCA
        LOG = n.bit_length()
        up = [parent[:]]

        for j in range(1, LOG):
            prev = up[j - 1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            j = 0
            while diff:
                if diff & 1:
                    u = up[j][u]
                diff >>= 1
                j += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # 4. Fenwick tree supporting range XOR updates
        bit = [0] * (n + 2)

        def add(index, value):
            index += 1
            while index < len(bit):
                bit[index] ^= value
                index += index & -index

        def range_xor(left, right, value):
            add(left, value)
            add(right, value)

        def point_query(index):
            index += 1
            result = 0
            while index > 0:
                result ^= bit[index]
                index -= index & -index
            return result

        # One bit represents each character a-z
        def char_mask(ch):
            return 1 << (ord(ch) - ord('a'))

        current = [char_mask(ch) for ch in s]

        # Each node's character contributes to its subtree's range
        for u in range(n):
            range_xor(tin[u], tout[u], current[u])

        # 5. Process queries
        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_mask = char_mask(parts[2])

                change = current[u] ^ new_mask
                range_xor(tin[u], tout[u], change)
                current[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)

                mask = (
                    point_query(tin[u])
                    ^ point_query(tin[v])
                    ^ current[ancestor]
                )

                # True if zero or one bits are set
                answer.append((mask & (mask - 1)) == 0)

        return answer
