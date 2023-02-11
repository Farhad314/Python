def PostfixEval(expr):
    stack= []
    expr=expr.split()
    for token in expr:
        if token.isdigit():
            stack.append(int(token))
        else:
            op2=stack.pop()
            op1=stack.pop()
            if token == "+":
                stack.append(op1 + op2)
            elif token == "-":
                stack.append(op1 - op2)
            elif token == "*":
                stack.append(op1 * op2)
            elif token == "/":
                stack.append(op1 / op2)
    return int(stack.pop())
            
expr="7 8 + 3 2 + /"
print(PostfixEval(expr))