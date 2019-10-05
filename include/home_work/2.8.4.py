#Даны две строки. Выведите на экран символы, которые есть в обоих строках.

def common_values(first_line, second_line):
    a = set(first_line)
    b = set(second_line)

    result = (a & b)
    return result

A = input(">>>>> ")
B = input(">>>> ")

print(common_values(A, B))