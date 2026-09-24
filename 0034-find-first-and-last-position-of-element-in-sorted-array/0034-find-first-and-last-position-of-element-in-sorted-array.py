class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            left, right = 0, len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    answer = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return answer

        def find_last():
            left, right = 0, len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    answer = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return answer

        return [find_first(), find_last()]