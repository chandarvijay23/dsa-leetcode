class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                index = stack.pop()
                height = heights[index]
                width = (i - (stack[-1] + 1)) if stack else i
                maxarea = max(maxarea, height * width)
            stack.append(i)
        return maxarea
