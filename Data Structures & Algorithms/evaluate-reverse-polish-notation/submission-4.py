class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for t in tokens:
            if t.isnumeric() or (t[0] == "-" and t[1:].isnumeric()):
                operands.append(int(t))
            else:
                if len(operands) < 2:
                    return None

                right_operand = operands.pop()
                left_operand = operands.pop()
                if t == "+":
                    operands.append(left_operand + right_operand)
                elif t == "-":
                    operands.append(left_operand - right_operand)
                elif t == "*":
                    operands.append(left_operand * right_operand)
                else:
                    operands.append(int(left_operand / right_operand))

        return operands[0]