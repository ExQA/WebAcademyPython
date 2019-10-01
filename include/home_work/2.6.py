#Определите, есть ли в списке повторяющиеся элементы, если да, то сделать из них новый список без повторений;


massiv = [1, 3, 5, 3, 1, 6, 6, 6, 6, 555]

# masivv2 = []
# for i in massiv:
#     if massiv.count(i) >= 2:
#         masivv2.append(i)
#
# print(masivv2)


def uniq(massiv):
  output = []
  for x in massiv:
    if x not in output and massiv.count(x) >= 2:
      output.append(x)
  return output


print(uniq(massiv))