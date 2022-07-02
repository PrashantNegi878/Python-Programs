def ispar(self, x):
    stack = []
    stack.append("A")
    for i in x:
        if i == "}" and stack[-1] == "{":
            stack.pop(-1)
        elif i == "]" and stack[-1] == "[":
            stack.pop(-1)
        elif i == ")" and stack[-1] == "(":
            stack.pop(-1)
        else:
            stack.append(i)
    stack.remove("A")
    if len(stack) > 0:
        return False
    else:
        return True