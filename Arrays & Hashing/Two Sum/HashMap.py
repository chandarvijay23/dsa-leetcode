class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity (Best): O(1)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(N)
        # Space Complexity (Worst): O(N)
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [i, d[target - num]]
            d[num] = i
