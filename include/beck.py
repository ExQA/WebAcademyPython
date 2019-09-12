#
# FIRST_NUMBER = float(input('First number >>> '))
# SECOND_NUMBER = float(input('Second number >>> '))
# OPERATION = input('Enter operation >>>')
#


def add(FIRST_NUMBER, SECOND_NUMBER):
    return FIRST_NUMBER + SECOND_NUMBER
def sub(FIRST_NUMBER, SECOND_NUMBER):
    return FIRST_NUMBER - SECOND_NUMBER
def umn(FIRST_NUMBER, SECOND_NUMBER):
    return FIRST_NUMBER * SECOND_NUMBER
def div(FIRST_NUMBER, SECOND_NUMBER):
    if SECOND_NUMBER != 0:
        return FIRST_NUMBER / SECOND_NUMBER
    else:
        return print('ERROR!!!!')

calc_object = {
    '+': add,
    '-': sub,
    '*': umn,
}

# keys_to_string = ' '.join([key for key in calc_object.keys()])
#
# res = 0
#
# if OPERATION in calc_object.keys():
#     print(calc_object[OPERATION](FIRST_NUMBER, SECOND_NUMBER))

if __name__ == '__main__':
        print('Start testing')
        assert add(5, 5) == 10
        assert sub(5, 5) == 0
        assert umn(5, 5) == 25
        print('END!!!')





