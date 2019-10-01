# Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста.

text = input('Enter your text >>> ')

w = text.split()
e = ""
for r in sorted(w):
    e = e+" " +r

print(e)