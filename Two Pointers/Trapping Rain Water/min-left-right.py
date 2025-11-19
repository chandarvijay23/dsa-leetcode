class Solution:
    def trap(self, height: List[int]) -> int:
        # Time Complexity (Best): O(N)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(1)
        # Space Complexity (Worst): O(1)
        if not height:
            return 0

        # Initialize two pointers, one at the beginning and one at the end
        l, r = 0, len(height) - 1

        # Initialize max heights encountered from left and right
        lmax = height[l]
        rmax = height[r]
        # Initialize the total trapped water
        result = 0

        # Loop until the pointers meet
        while l < r:
            # If the max height from the left is less than or equal to the max height from the right
            if lmax < rmax:
                # Move the left pointer
                l += 1
                # Update the maximum height encountered from the left
                lmax = max(lmax, height[l])
                # Calculate water trapped at the current position and add to result
                # Water trapped is the difference between the current left max and current bar height
                result += lmax - height[l]
            else:
                # Move the right pointer
                r -= 1
                # Update the maximum height encountered from the right
                rmax = max(rmax, height[r])
                # Calculate water trapped at the current position and add to result
                # Water trapped is the difference between the current right max and current bar height
                result += rmax - height[r]

        return result
