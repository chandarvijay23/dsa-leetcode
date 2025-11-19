class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                temperature, index = stack.pop()
                output[index] = i - index
            stack.append((value, i))
        
        return output