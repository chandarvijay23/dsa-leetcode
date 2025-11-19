class MinStack:

    # Time Complexity (Best): O(1)
    # Time Complexity (Average): O(1)
    # Time Complexity (Worst): O(1)
    # Space Complexity (Best): O(1)
    # Space Complexity (Average): O(1)
    # Space Complexity (Worst): O(1)
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # Time Complexity (Best): O(1)
    # Time Complexity (Average): O(1)
    # Time Complexity (Worst): O(1)
    # Space Complexity (Best): O(1)
    # Space Complexity (Average): O(1)
    # Space Complexity (Worst): O(1)
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    # Time Complexity (Best): O(1)
    # Time Complexity (Average): O(1)
    # Time Complexity (Worst): O(1)
    # Space Complexity (Best): O(1)
    # Space Complexity (Average): O(1)
    # Space Complexity (Worst): O(1)
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    # Time Complexity (Best): O(1)
    # Time Complexity (Average): O(1)
    # Time Complexity (Worst): O(1)
    # Space Complexity (Best): O(1)
    # Space Complexity (Average): O(1)
    # Space Complexity (Worst): O(1)
    def top(self) -> int:
        return self.stack[-1]

    # Time Complexity (Best): O(1)
    # Time Complexity (Average): O(1)
    # Time Complexity (Worst): O(1)
    # Space Complexity (Best): O(1)
    # Space Complexity (Average): O(1)
    # Space Complexity (Worst): O(1)
    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
