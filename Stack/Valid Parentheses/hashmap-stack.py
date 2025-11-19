class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity (Best): O(n)
        # Time Complexity (Average): O(n)
        # Time Complexity (Worst): O(n)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(n)
        # Space Complexity (Worst): O(n)
        parantheses_stack = []
        d = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in d.values():  # Check if it's an opening parenthesis
                parantheses_stack.append(i)
            else:  # It's a closing parenthesis
                # If stack is empty or top of stack doesn't match the expected opening parenthesis
                if not parantheses_stack or parantheses_stack[-1] != d[i]:
                    return False
                # If it matches, pop the opening parenthesis from the stack
                parantheses_stack.pop()

        # After iterating through all characters, the stack should be empty for a valid string
        return len(parantheses_stack) == 0
