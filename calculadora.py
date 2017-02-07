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

if sys.argv[1] == 'suma':
    print(int(sys.argv[2]) + int(sys.argv[3]))
elif sys.argv[1] == 'resta':
    print(int(sys.argv[2]) - int(sys.argv[3]))
elif sys.argv[1] == 'multi':
    print(int(sys.argv[2]) * int(sys.argv[3]))
elif sys.argv[1] == 'div':
    try:
        print(int(sys.argv[2]) / int(sys.argv[3]))
    except ZeroDivisionError:
        print("Cannot divide by 0")
else:
    help()
