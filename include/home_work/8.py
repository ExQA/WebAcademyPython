#x! = n   x! = 1 * … * (x-2) * (x-1) * x
import math

X = int(input('X!= '))
factorial = 1

for i in range(2, X+1):
    factorial *= i

print('X!= ', factorial)

print('Из коробки = ', math.factorial(X))
