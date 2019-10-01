#Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице;

def zero(number):
    return [0] * number

list = zero(100)
list[0] = 1
list[-1] = 1
print(list)