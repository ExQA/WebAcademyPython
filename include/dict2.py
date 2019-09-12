

# phonebook = {
# #     'Jack': '0123-123',
# #     'Guid': '666-333',
# #     'Mary': '4343-123'
# #
# # }
# #
# # print(phonebook['Jack'])


# def calc(**n):
#     print(n)
#     summa = 0
#     for i in n.values():
#         summa += i
#
#
#
#     return summa
#
# print(calc(apple=123, pear=34, orange=55))


# def print_info(**human_object):
#     for key in human_object:
#         print(key, human_object[key] , set=' - ')
#     print('-------')
#
# print_info(name='Vasia', surename='Bobo', age='15', job='QA')


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

keys_to_string = ' '.join([key for key in calc_object.keys()])

FIRST_NUMBER = float(input('First number >>> '))
SECOND_NUMBER = float(input('Second number >>> '))
OPERATION = input( keys_to_string)


if OPERATION in calc_object:
    res = calc_object(OPERATION)(FIRST_NUMBER, SECOND_NUMBER)
    print(res)