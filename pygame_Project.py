import time

def simpleProblemSolver(x, y):
    operationType = input("Choose an Operation Type(+,-,/,*)")
    if operationType == '+':
        print(x + y)
    elif operationType == '-':
        print(x - y)
    elif operationType == '/':
        print(x / y)
    elif operationType == '/':
        print(x * y)
simpleProblemSolver(2,4)
time.sleep(3000)