class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False


# Time complexity o(n)
# Space Complexity O(n) (worst case)
# Space Complexity O(1) (best case)
