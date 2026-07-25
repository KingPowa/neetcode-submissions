class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        if len(tokens) == 2: raise ValueError()

        operands = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                if len(operands) >= 2:
                    operand_2 = operands.pop()
                    operand_1 = operands.pop()
                    if token == "+": res = operand_1 + operand_2
                    elif token == "-": res = operand_1 - operand_2
                    elif token == "*": res = operand_1 * operand_2
                    else: res = int(operand_1 / operand_2)
                    operands.append(res)
                else:
                    raise ValueError()
            else:
                operands.append(int(token))
        return operands[-1]