
import heapq
from collections import defaultdict

class DualHeap:
    def __init__(self):
        self.small = []  # Max heap
        self.large = []  # Min heap
        self.delayed = defaultdict(int)

        self.small_size = 0
        self.large_size = 0
        self.small_sum = 0
        self.large_sum = 0

    def prune(self, heap, is_small):
        while heap:
            num = -heap[0] if is_small else heap[0]

            if self.delayed[num] == 0:
                break

            heapq.heappop(heap)
            self.delayed[num] -= 1

    def balance(self):
        if self.small_size > self.large_size + 1:
            self.prune(self.small, True)

            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)

            self.small_size -= 1
            self.large_size += 1
            self.small_sum -= num
            self.large_sum += num

            self.prune(self.small, True)

        elif self.small_size < self.large_size:
            self.prune(self.large, False)

            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)

            self.large_size -= 1
            self.small_size += 1
            self.large_sum -= num
            self.small_sum += num

            self.prune(self.large, False)

    def add(self, num):
        self.prune(self.small, True)

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
            self.small_sum += num
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
            self.large_sum += num

        self.balance()

    def remove(self, num):
        self.prune(self.small, True)

        if num <= -self.small[0]:
            self.small_size -= 1
            self.small_sum -= num
        else:
            self.large_size -= 1
            self.large_sum -= num

        self.delayed[num] += 1

        if self.small and num == -self.small[0]:
            self.prune(self.small, True)

        if self.large and num == self.large[0]:
            self.prune(self.large, False)

        self.balance()

    def cost(self):
        self.prune(self.small, True)
        self.prune(self.large, False)

        median = -self.small[0]

        return (
            median * self.small_size - self.small_sum
            + self.large_sum - median * self.large_size
        )


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        # Step 1: Calculate all window costs
        dh = DualHeap()

        for i in range(x):
            dh.add(nums[i])

        costs = [dh.cost()]

        for i in range(x, n):
            dh.remove(nums[i - x])
            dh.add(nums[i])
            costs.append(dh.cost())

        # Step 2: Dynamic Programming
        INF = float('inf')
        prev = [0] * (n + 1)

        for count in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element
                curr[i] = curr[i - 1]

                # Select a window ending at i - 1
                if i >= x:
                    start = i - x
                    candidate = prev[start] + costs[start]

                    curr[i] = min(curr[i], candidate)

            prev = curr

        return prev[n]
