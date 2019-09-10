# + - *  / ^ sin cos tan
import math

FIRST_NUMBER = float(input('First number >>> '))
SECOND_NUMBER = float(input('Second number >>> '))
OPERATION = input('Enter operation >>>')
res = None

def add(FIRST_NUMBER, SECOND_NUMBER):
    return FIRST_NUMBER + SECOND_NUMBER
def sub(FIRST_NUMBER, SECOND_NUMBER):
    return FIRST_NUMBER - SECOND_NUMBER
def umn(FIRST_NUMBER, SECOND_NUMBER):
    return FIRST_NUMBER * SECOND_NUMBER
def div(FIRST_NUMBER, SECOND_NUMBER):
    return FIRST_NUMBER / SECOND_NUMBER
def step(FIRST_NUMBER, SECOND_NUMBER):
    return FIRST_NUMBER ** SECOND_NUMBER

def sin(FIRST_NUMBER, SECOND_NUMBER):
    return math.sin(FIRST_NUMBER)
def cos(FIRST_NUMBER, SECOND_NUMBER):
    return math.cos(FIRST_NUMBER)
def tan(FIRST_NUMBER, SECOND_NUMBER):
    return math.tan(FIRST_NUMBER)


def main():
    if OPERATION == '+':
        res = add(FIRST_NUMBER, SECOND_NUMBER)
    elif OPERATION == '-':
        res = sub(FIRST_NUMBER, SECOND_NUMBER)
    elif OPERATION == '*':
        res = umn(FIRST_NUMBER, SECOND_NUMBER)
    elif OPERATION == '/':
        res = div(FIRST_NUMBER, SECOND_NUMBER)
    elif OPERATION == 'ˆ':
        res = step(FIRST_NUMBER, SECOND_NUMBER)

    elif OPERATION == 'sin':
        res = sin(FIRST_NUMBER, SECOND_NUMBER)
    elif OPERATION == 'cos':
        res = sin(FIRST_NUMBER, SECOND_NUMBER)
    elif OPERATION == 'tan':
        res = sin(FIRST_NUMBER, SECOND_NUMBER)
    elif OPERATION == 'tan':
        res = sin(FIRST_NUMBER, SECOND_NUMBER)
    else:
        print(False)

    return print(res)
main()