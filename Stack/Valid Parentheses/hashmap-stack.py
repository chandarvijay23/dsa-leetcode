class Solution:
    def isValid(self, s: str) -> bool:
        parantheses_stack = []
        d = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in d.values():
                parantheses_stack.append(i)
            else:
                if parantheses_stack and parantheses_stack[-1] == d[i]:
                    parantheses_stack.pop()
                else:
                    return False

        return (len(parantheses_stack) == 0)