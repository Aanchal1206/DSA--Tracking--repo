class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n + 1)

        for num in nums:
            count[num] += 1

        duplicate = 0
        missing = 0

        for num in range(1, n + 1):
            if count[num] == 2:
                duplicate = num
            elif count[num] == 0:
                missing = num

        return [duplicate, missing]