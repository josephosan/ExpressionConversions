from models.operators import Operators
from models.tree import Node


def postfix_draw(expression):
  stack = []

  for c in expression:
    if c in Operators:
      right = stack.pop()
      left = stack.pop()
      stack.append(Node(c, left, right))
    else:
      stack.append(Node(c))
  root = stack.pop()
  return root


def prefix_draw(expression):
  stack = []

  for c in reversed(expression):
    if c in Operators:
      right = stack.pop()
      left = stack.pop()
      stack.append(Node(c, left, right))
    else:
      stack.append(Node(c))
  root = stack.pop()
  return root


# infix draw :)
