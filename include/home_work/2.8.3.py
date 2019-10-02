# Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста.

text = input('Enter your text >>> ').split()

print(text)
e = ""
for i in sorted(text):
    e = e +" " + i

print(e)