#!/usr/bin/python3

import sys


def help():
    print('Usage:')
    print('calc.py func op1 op2')
    print('Possible functions: suma resta multi div')

N_ARGS = 4

if len(sys.argv) != N_ARGS:
    help()
    sys.exit()

_, func, op1, op2 = sys.argv

try:
    op1 = float(op1)
    op2 = float(op2)
except ValueError:
    help()
    sys.exit("Introduced not numeric arguments")

if func == 'suma':
    print(op1 + op2)
elif func == 'resta':
    print(op1 - op2)
elif func == 'multi':
    print(op1 * op2)
elif func == 'div':
    try:
        print(op1 / op2)
    except ZeroDivisionError:
        print("Cannot divide by 0")
else:
    help()
