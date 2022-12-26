from config.config import States
import transforms as t


def manage(state, expression):
    if state not in States:
        raise Exception("Please Enter a valid infix, postfix or prefix expression!")

    if state == "infix":
        postfix = t.infixToPostfix(expression)
        prefix = t.infixToPrefix(expression)
        return [prefix, expression, postfix]

    elif state == "prefix":
        infix = t.prefixToInfix(expression)
        postfix = t.prefixToPostfix(expression)
        return [expression, infix, postfix]

    elif state == "postfix":
        infix = t.postfixToInfix(expression)
        prefix = t.postfixToInfix(expression)
        return [prefix, infix, expression]

    else:
        raise Exception("The expression does not fit the state!!")
