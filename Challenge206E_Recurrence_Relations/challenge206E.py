#!/usr/bin/env python
# Tui Popenoe
# challenge206E.py - Recurrence Relation

import ast
import operator as op
import sys

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

def eval_expr(expr):
    """
    Evaluate the arithmetic expression and return a value
    Args:
        expr: A string representation of an arithmetic expression
    Rets:
        A numeric value as the result of the expression
    """
    return eval_(ast.parse(expr, mode='eval').body)

def eval_(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


def recurrence(n, expr):
    """Return the literal eval of the given expr and n"""
    return eval_expr('%s%s' % (str(n), expr))

def get_nth_term(expr, first_term, n):
    if n == 0:
        return first_term
    else:
        return get_nth_term(expr, recurrence(first_term), n - 1)

def main():
    if len(sys.argv) > 1:
        print(get_nth_term(sys.argv[1], sys.argv[2], sys.argv[3]))
    else:
        print(get_nth_term(stdin.readline(),
                           stdin.readline(),
                           stdin.readline()))

if __name__ == '__main__':
    main()