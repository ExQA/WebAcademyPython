x = [-2, 34.5, 6, 0, -11]

def invers_list(some_list):
    new_list = list()
    for number in some_list:
        if number > 0:
            new_list.append(1)
        elif number < 0:
            new_list.append(-1)
        else:
            new_list.append(0)
    return  new_list
print(invers_list(x))

result = invers_list(x)


def custom_sum(some_list):
    new_list = sum(some_list)
    return new_list

print(custom_sum(result))
