t = '{} {} {} = {}'

first_number = float(input('Enter first number: '))
second_number = float(input('Enter second number: '))
operaton = input('operation: ')
res = None

if operaton == "+":
    res = first_number + second_number
elif operaton == "-":
    res = first_number - second_number
elif operaton == "*":
    res = first_number * second_number
else:
    print("Invalid operation")

if res is not None:
    print(t.format(first_number, operaton, second_number, res))
