import beck

FIRST_NUMBER = float(input('First number >>> '))
SECOND_NUMBER = float(input('Second number >>> '))
OPERATION = input('Enter operation >>>')


keys_to_string = ' '.join([key for key in beck.calc_object.keys()])

res = 0

if OPERATION in beck.calc_object.keys():
    print(beck.calc_object[OPERATION](FIRST_NUMBER, SECOND_NUMBER))
