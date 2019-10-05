from calc_operations import calc_object
import re


print(calc_object.keys())


try:
    while True:
        first = input('Enter the first number>>> ').strip()
        second = input('Enter the second number>>> ').strip()

        if not re.match("^\d+(\.\d+)?$", first) or not re.match("^\d+(\.\d+)?$", second):
            print("Error! Make sure you only use float data")
        else:
            first_num = float(first)
            second_num = float(second)
            operation = input('Select an operation').strip()
            result = calc_object[operation](first_num, second_num)
            break
    print('{} {} {} = {}'.format(first_num, operation, second_num, result))

except (ZeroDivisionError, ValueError, RecursionError ) as e:
    print(e)