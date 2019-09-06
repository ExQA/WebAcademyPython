# def x():
#     print("functional x start call")
#     print("Hello, world!")
#     print("functional x end call")
# x()


def print_number(user_number, break_iteration):
    print('++++++')
    for i in range(user_number):
        if break_iteration == i:
            break
        print(i)
    print('----')

user_input = int(input('>>>>'))
user_i = int(input('i>>>> '))

print_number(user_input, user_i)

#
# def print_number(limit):
#     for i in range(limit):
#         if break_iteration ==i:
#             break
#         print(i)


