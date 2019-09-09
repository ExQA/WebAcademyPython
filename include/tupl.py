some_str = 'sjdkhfjsdhf8736457jsdhfjkdsf9893'

u = []
for char in some_str:
    if '0' <= char <= '9':
        u.append(int(char))

print(u)

z = (1, 3, 4, 5, 6, 7)

def f(some_list):
    list_odd = []
    list_event = []
    for number in some_list:
        if number % 2 == 0:
            list_event.append(number)
        else:
            list_odd.append(number)
    return list_odd, list_event

def f1(some_list):
    return  [elem for elem in some_list if elem % 2 == 0], [elem for elem in some_list if elem % 2 == 1]

print(f(range(2, 56)))

print(f1(range(2, 56)))


def left_finde(string, char):
    if char in string:
        for index , element in enumerate(string):
            if element == char:
                return index
    else:
        return '"{}" in "{}" not found!'.format(char, string)

print(left_finde('some', 'e'))
print(left_finde('qqqqqqq', 'q'))
