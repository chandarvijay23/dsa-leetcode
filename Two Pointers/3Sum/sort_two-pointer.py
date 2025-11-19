```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity (Best): O(N^2)
        # Time Complexity (Average): O(N^2)
        # Time Complexity (Worst): O(N^2)
        # Space Complexity (Best): O(N)
        # Space Complexity (Average): O(N)
        # Space Complexity (Worst): O(N)
        
        result = []
        # Sort the array to efficiently use the two-pointer approach and handle duplicates.
        nums.sort()

        # Iterate through the array, fixing the first element of the triplet.
        for i, value in enumerate(nums):
            # Skip duplicate values for the first element to avoid duplicate triplets.
            if i > 0 and value == nums[i-1]:
                continue
            
            # Initialize two pointers for the remaining sub-array.
            # 'l' starts just after 'i', 'r' starts at the end of the array.
            l = i + 1
            r = len(nums) - 1
            
            # Use a two-pointer approach to find the other two elements.
            while l < r:
                current_sum = value + nums[l] + nums[r]
                
                if current_sum < 0:
                    # Sum is too small, move the left pointer to increase the sum.
                    l += 1
                elif current_sum > 0:
                    # Sum is too large, move the right pointer to decrease the sum.
                    r -= 1
                else:
                    # Found a triplet that sums to zero.
                    result.append([value, nums[l], nums[r]])
                    
                    # Move the left pointer to find new distinct elements.
                    l += 1
                    # Skip duplicate values for the left pointer to avoid duplicate triplets.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return result
```
