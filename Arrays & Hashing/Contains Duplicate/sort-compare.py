from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity (Best): O(N log N)
        # Time Complexity (Average): O(N log N)
        # Time Complexity (Worst): O(N log N)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(1)
        # Space Complexity (Worst): O(1)
        
        # Sort the array in-place.
        # Python's list.sort() uses Timsort.
        # Time complexity for Timsort is O(N log N) in all cases (best, average, worst).
        # Auxiliary space complexity for Timsort is typically O(N) in the worst case,
        # but often considered O(1) or O(log N) for primitive types when modifying
        # the input array in-place, focusing on auxiliary space beyond input.
        nums.sort()

        # Iterate through the sorted array to find adjacent duplicates.
        # If the array is sorted, any duplicates must be adjacent.
        # This loop runs in O(N) time in the worst case.
        for i in range(len(nums) - 1):
            # Compare the current element with the next element.
            if nums[i] == nums[i + 1]:
                # If a duplicate is found, return True immediately.
                return True
        
        # If the loop completes without finding any duplicates, return False.
        return False
