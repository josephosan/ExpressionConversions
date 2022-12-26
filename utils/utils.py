from models.operators import Operators_except_brackets, Open_brackets, Close_brackets


def find_state(expression):
    if expression[0] in Operators_except_brackets:
        return "prefix"

    elif expression[-1] in Operators_except_brackets:
        return "postfix"

    else:
        return "infix"


def is_brackets_valid(expression):
    stack = []

    for char in expression:
        if char in Open_brackets:
            stack.append(char)
        elif stack and char in Close_brackets:
            stack.pop()

    if stack:
        return False
    else:
        return True


def is_space_valid(expression):
    if " " in expression:
        return False
    return True
