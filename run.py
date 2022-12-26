from models.draw import postfix_draw
from models import tree
from manage.manage import manage
from utils.utils import find_state, is_brackets_valid, is_space_valid

while True:
    expression = input("Expression: ")

    state = find_state(expression)

    # main expression validation:
    space_valid = is_space_valid(expression)
    # brackets validation:
    brackets_valid = is_brackets_valid(expression)

    if not brackets_valid or not space_valid:
        print("An Error Accrued: Please enter an expression with valid brackets and without space!")
        continue

    result = manage(state, expression)

    print("-----------------------------------\n")
    print("Prefix expression = " + result[0])
    print("Infix expression = " + result[1])
    print("Postfix expression = " + result[2])
    print("\n")
    print("Expression tree:")
    tree.print_tree(postfix_draw(result[2]))
    print("-----------------------------------\n")


# Giant Prefix = ++++++++/*A+BCD/*A+BCD/*A+BCD/*A+BCD/*A+BCD/*A+BCD/*A+BCD/*A+BCD/*A+BCD
# Giant Infix = A*(B+C)/D+A*(B+C)/D+A*(B+C)/D+A*(B+C)/D+A*(B+C)/D+A*(B+C)/D+A*(B+C)/D+A*(B+C)/D+A*(B+C)/D
# Giant Postfix = ABC+*D/ABC+*D/+ABC+*D/+ABC+*D/+ABC+*D/+ABC+*D/+ABC+*D/+ABC+*D/+ABC+*D/+
