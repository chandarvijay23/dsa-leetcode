class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity (Best): O(1)
        # Time Complexity (Average): O(n)
        # Time Complexity (Worst): O(n)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(n)
        # Space Complexity (Worst): O(n)
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
