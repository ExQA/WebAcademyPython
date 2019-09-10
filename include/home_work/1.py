first_word = input('Enter the first word >>> ')
secod_word = input('Enter the second word >>> ')

result = first_word + secod_word

for i in range(len(result)):
    print(result[i])

print(list(result))
print(','.join(result))