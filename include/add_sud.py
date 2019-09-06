a = float(input('first '))
oper = input('operation ')
b = float(input('second '))



def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def umn(a, b):
    return a * b

def main():
    a = float(input('first '))
    oper = input('operation ')
    b = float(input('second '))
    res = None

    if oper == '+':
        res = add(a, b)
    elif oper == '-':
        res = sub(a, b)
    elif oper == '*':
        res = umn(a, b)
    return res
    print(res)