first = float(input('first number >>> '))
operation = input('operation >>> ')
second = float(input('second number >>> '))

pattern_output = '{} {} {} = {}'
res = None

if operation == '+':
    res = first + second
elif operation == '-':
    res = first - second
elif operation == '*':
    res = first - second
else:
    print('invalide operation')

if res is not None:
    print(pattern_output.format(first, operation, second, res))