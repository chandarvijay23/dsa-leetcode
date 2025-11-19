class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time Complexity (Best): O(N)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(1)
        # Space Complexity (Worst): O(1)
        l, r = 0, len(height) - 1
        maximum = 0

        while l < r:
            # Calculate the area with the current left and right pointers.
            # The height is limited by the shorter of the two lines.
            # The width is the distance between the two lines.
            area = min(height[l], height[r]) * (r - l)
            # Update the maximum area found so far.
            maximum = max(maximum, area)

            # Move the pointer of the shorter line inward.
            # This is because moving the taller line inward will definitely
            # result in a smaller or equal height (due to the min operation)
            # and a smaller width, thus a smaller or equal area.
            # Moving the shorter line, however, might lead to a taller line
            # on that side, potentially increasing the area.
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return maximum
