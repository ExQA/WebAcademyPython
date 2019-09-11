x = input('x = ') #124234
y = input('y = ')

y_list = [int(y) for y in str(y)]

def custom_sum(x):
    new_list = 0
    for i in x:
        new_list += int(i)

    return new_list



def custom_sum2(y_list):
    #new_list = list(y)

    new_list2 = sum(y_list)
    return new_list2

print('x = ', custom_sum(x))

print('y = ', custom_sum2(y_list))