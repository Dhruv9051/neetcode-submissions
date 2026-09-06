class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                # If it's not an operator, it must be a number
                stack.append(int(t))
            else:
                # Pop the top two elements. 
                # The first pop is the right operand, the second is the left.
                right = stack.pop()
                left = stack.pop()
                
                if t == '+':
                    stack.append(left + right)
                elif t == '-':
                    stack.append(left - right)
                elif t == '*':
                    stack.append(left * right)
                elif t == '/':
                    # Use int(left / right) to truncate towards zero
                    stack.append(int(left / right))
                    
        return stack[0]