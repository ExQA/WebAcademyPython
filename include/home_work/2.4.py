#Найдите сумму и произведение элементов списка. Результаты вывести на экран;


def product_list(p):
    total = 1  # critical step works for all list
    summa = 1
    for i in p:
        total = total * i  # тут умножаем
        summa = summa + i  # тут сумируем
        answer = ('Произведение = {} \nСумма = {}').format(total, summa)
    return answer

list = [2, 3, 4, 2]

print (product_list(list))  # should print 48
