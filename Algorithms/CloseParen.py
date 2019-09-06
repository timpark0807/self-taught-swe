def close_paren(word):
    stack = []
    for symbol in word:
        if symbol in "({[":
            stack.append(symbol)
        if symbol in ")}]":
            popped = stack.pop()
            if not compare(symbol, popped):
                return False
    return stack == []

def compare(symbol, popped):
    if popped == "(" and symbol == ")":
        return True
    elif popped == "{" and symbol == "}":
        return True
    elif popped == "[" and symbol == "]":
        return True
    else:
        return False

a = "({[]]})"
print(close_paren(a))
