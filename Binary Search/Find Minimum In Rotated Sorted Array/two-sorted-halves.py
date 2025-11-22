class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]
        while l <= r:
            middle = (l + r) // 2
            result = min(nums[middle], result)
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle - 1
        return result