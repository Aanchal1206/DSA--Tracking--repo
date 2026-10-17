
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(num):
            return sum(int(digit) for digit in str(num))

        n = len(nums)

        # Sort by digit sum, then by numerical value
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its target index
        target = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        # Count cycles in the permutation
        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                j = target[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
