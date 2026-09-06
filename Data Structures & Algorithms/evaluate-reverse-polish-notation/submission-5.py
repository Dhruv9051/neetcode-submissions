class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def checkNumOrOperand(element):
            try:
                int(element)
                return True
            except ValueError:
                return False
        def eval(ele1, ele2, operand):
            match operand:
                case "+":
                    result = int(ele1) + int(ele2)
                case "/":
                    result = int(int(ele1) / int(ele2))
                case "*":
                    result = int(ele1) * int(ele2)
                case "-":
                    result = int(ele1) - int(ele2)
            return result
        stack = []
        for ele in tokens:
            if checkNumOrOperand(ele) == True:
                stack.append(ele)
            else:
                ele2, ele1 = stack.pop(), stack.pop()
                res = eval(ele1, ele2, ele)
                stack.append(res)

        return int(tokens[0]) if len(tokens) == 1 else stack.pop()