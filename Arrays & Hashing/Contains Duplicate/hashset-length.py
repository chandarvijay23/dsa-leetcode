class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


# Time complexity o(n)
# Space Complexity O(n)
