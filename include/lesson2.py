# coding=utf-8
import math


# z = -2
# pi = 3.13
#
# print (pi)
# print (math.pi)
# print (abs(z))  # модуль числа
# print (pow(z, 2), z ** 2, math.pow(z, 2))  # квадрат числа
#
#
#
# m = 468986645343456567
#
# print (round(m), round(m, 5))  # округляет до пятого символа


PI = math.pi


r = float(input("R = "))
s = (2 * PI * (r ** 2))
l = 2 * PI * r
print(round(s, 3), l)

