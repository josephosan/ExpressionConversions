from models.operators import Operators
from models.priorities import Priorities

# 1.


def infixToPostfix(expression):
    stack = []  # defining a stack
    output = ""

    for character in expression:  # looping the characters
        if character not in Operators:
            output += character
        elif character == '(':
            stack.append(character)
        # when we reach this point, means we need pop from stack till we reach the '(' character.
        elif character == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # pop the '(' character itself!
        else:  # here, we check if we can add the operator to the stack or not!
            # if they have same Priorities, you should also pop them.
            while stack and stack[-1] != '(' and Priorities[character] <= Priorities[stack[-1]]:
                output += stack.pop()
            stack.append(character)

    while stack:  # then we empty the stack.
        output += stack.pop()

    return output

# 2.


def infixToPrefix(expression):
    output = ""
    stack = []
    expression = expression[::-1]

    for character in expression:
        if character not in Operators:
            output += character
        elif character == ')':
            stack.append(character)
        elif character == '(':
            while stack and stack[-1] != ')':
                output += stack.pop()
            stack.pop()
        else:
            if stack and character == stack[-1] and character == '^':
                output += stack.pop()

            while stack and stack[-1] != ')' and Priorities[character] < Priorities[stack[-1]]:
                output += stack.pop()
            stack.append(character)

    while stack:
        output += stack.pop()

    return output[::-1]


# 3.
def postfixToInfix(expression):
    holder1 = ""
    holder2 = ""
    stack = []

    for character in expression:
        if character not in Operators:
            stack.append(character)
        else:
            holder2 += stack.pop()
            holder1 += stack.pop()
            holder1 += character
            stack.append("(" + holder1+holder2 + ")")
            holder1 = ""
            holder2 = ""

    return stack[0]


# 4.
def prefixToInfix(expression):
    holder1 = ""
    holder2 = ""
    stack = []

    expression = expression[::-1]

    for character in expression:
        if character not in Operators:
            stack.append(character)
        else:
            holder1 = stack.pop()
            holder2 = stack.pop()
            holder2 += character
            stack.append(")" + holder2+holder1 + "(")
            holder1 = ""
            holder2 = ""

    return stack[0][::-1]


# 5.
def postfixToPrefix(expression):
    holder1 = ""
    holder2 = ""
    stack = []

    for character in expression:
        if character not in Operators:
            stack.append(character)
        else:
            holder2 = stack.pop()
            holder1 = stack.pop()
            holder1 = character+holder1
            stack.append(holder1+holder2)
            holder1 = ""
            holder2 = ""

    return stack[0]

# 6.


def prefixToPostfix(expression):
    holder1 = ""
    holder2 = ""
    stack = []

    expression = expression[::-1]

    for character in expression:
        if character not in Operators:
            stack.append(character)
        else:
            holder1 = stack.pop()
            holder2 = stack.pop()
            holder2 = holder2+character
            stack.append(holder1+holder2)
            holder1 = ""
            holder2 = ""

    return stack[0]
