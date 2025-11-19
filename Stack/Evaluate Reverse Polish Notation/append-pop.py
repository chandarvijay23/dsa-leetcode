class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time Complexity (Best): O(N)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N)
        # Space Complexity (Best): O(N)
        # Space Complexity (Average): O(N)
        # Space Complexity (Worst): O(N)
        
        # Initialize an empty list to serve as a stack for operands.
        stack = []

        # Iterate through each token in the input list.
        for i in tokens:
            # If the token is not an operator, it must be an operand (number).
            if i not in ['+', '-', '*', '/']:
                # Convert the operand string to an integer and push it onto the stack.
                stack.append(int(i))
            else:
                # If the token is an operator, pop the last two operands from the stack.
                # The second operand popped (num2) is the right-hand side,
                # and the first operand popped (num1) is the left-hand side.
                num2 = stack.pop()
                num1 = stack.pop()

                # Perform the operation based on the current operator.
                if i == '+':
                    stack.append(num1 + num2)
                elif i == '-':
                    stack.append(num1 - num2)
                elif i == '*':
                    stack.append(num1 * num2)
                else:
                    # For division, ensure integer division truncating towards zero.
                    # Python's default `/` is float division, `//` is floor division.
                    # `int(num1 / num2)` mimics C++/Java behavior of truncating towards zero.
                    stack.append(int(num1 / num2))
        
        # After processing all tokens, the stack will contain a single element,
        # which is the final result of the RPN expression.
        return stack[0]
