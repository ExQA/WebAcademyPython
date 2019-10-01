#Найти наибольший элемент списка и вывести его на экран;


list = [12, 23, 33, 44, 1, 11]
print(max(list))




list1 = [] # create empty list
# mow many elements will be put in List1
num = int(input("Enter number of elements in list: "))
# iterating till num to append elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

# print maximum element
print("Max element is:", max(list1))


a = [1, 2, 3, 4, 6, 7, 99, 88, 999]
def max_value(a):
    max = 0
    for i in a:
        if i > max:
            max = i
    return max

print(max_value(a))