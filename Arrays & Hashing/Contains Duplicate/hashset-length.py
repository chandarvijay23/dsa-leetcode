class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity (Best): O(N)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(N)
        # Space Complexity (Worst): O(N)
        return len(set(nums)) != len(nums)
