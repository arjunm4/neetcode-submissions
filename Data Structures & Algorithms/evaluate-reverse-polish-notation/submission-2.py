class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        stack = []
        operators = {"/", "-", "+", "*"}

        for token in tokens:
            if token in operators:
                stack.append(self.operation(token, stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        
        return stack[0]

    def operation(self, op, num1, num2):
        match op:
            case "*":
                return num1 * num2
            case "+":
                return num1 + num2
            case "-":
                return num2 - num1
            case "/":
                return math.trunc(num2 / num1)
        