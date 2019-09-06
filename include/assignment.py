# my_list = [1, 2, 3, 55, 11]
# print(my_list)
#
# my_list[0] = 10
# print(my_list)
# print(my_list[0:4])  #с первого элемента по четвертый, диапазон
#

# def sort_even(some_list):
#    print(some_list)
#    new_list = []
#    for number in some_list:
#        if number % 2 == 0:
#            new_list.append(number)
#            print(number)
#    return new_list
#
#
# x = sort_even([1, 2, 3, 5, 6, 9, 7, 4])
# print(x)


# def custom_len(list_n):
#     count = 0
#     for _ in list_n:
#         count = count + 1
#         return count
#
#
# print(custom_len('qwerty'))

# def is_str(string, char):
#     return char in string
#
# def count_char(text, char_1):
#     count = 0
#     if is_str(string=text, char=char_1):
#         for elem in text:
#             if elem == char_1:
#                 count += 1
#     return count
#
#
# print(count_char(text=';kfdddskfjgs', char_1='s'))


def check_password(password):
    for element in password:
        element = ord(element)
        if ord('A') <= element <= ord('Z'):
            return True

    return False


print(check_password('qwErty'))

