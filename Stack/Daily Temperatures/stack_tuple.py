class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time Complexity (Best): O(n)
        # Time Complexity (Average): O(n)
        # Time Complexity (Worst): O(n)
        # Space Complexity (Best): O(n)
        # Space Complexity (Average): O(n)
        # Space Complexity (Worst): O(n)
        
        # Initialize an output array with zeros, of the same length as temperatures.
        # This array will store the number of days one has to wait for a warmer temperature.
        output = [0] * len(temperatures)
        
        # Initialize an empty stack. Each element in the stack will be a tuple: (temperature, index).
        # The stack will maintain a decreasing order of temperatures.
        stack = []

        # Iterate through the temperatures list with both index (i) and value.
        for i, value in enumerate(temperatures):
            # While the stack is not empty and the current temperature (value) is warmer
            # than the temperature at the top of the stack:
            while stack and value > stack[-1][0]:
                # Pop the (temperature, index) pair from the top of the stack.
                # This signifies that 'temperature' has found its next warmer day.
                temperature, index = stack.pop()
                
                # Calculate the number of days to wait and store it in the output array.
                # The waiting period is the current day's index minus the popped day's index.
                output[index] = i - index
            
            # Push the current (temperature, index) onto the stack.
            # This temperature is now waiting for a warmer day in the future.
            stack.append((value, i))
        
        # Return the final output array.
        return output
