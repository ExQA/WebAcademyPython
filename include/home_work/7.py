# a and b = summa from a to b

A = int(input('Enter A >>>>'))
B = int(input('Enter B >>>>'))

def count_number(A, B):
    summa = 0
    if A <= B:
        for i in range(A, B + 1):
            summa += i
    else:
        print(False)
    return summa

#summa = 0
# if A <= B:
#     for i in range(A, B+1):
#         summa += i
#        # print(i)
# else:
#     print(False)

print('Summa = ', count_number(A, B))