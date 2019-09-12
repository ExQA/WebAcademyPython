#Ввести два слова и разделить все знаки запятой

first_word = input('Enter the first word >>> ')
secod_word = input('Enter the second word >>> ')

result = first_word + secod_word

print(list(result))
print(','.join(result))