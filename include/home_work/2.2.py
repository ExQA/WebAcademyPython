#Сформировать возрастающий список из чётных чисел (количество элементов 45);

def list(n):
    a = [i for i in range(0,n,2)]
    return a


print(list(45))
