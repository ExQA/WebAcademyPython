# axˆ2+bx+c=0
# discr = bˆ2 - 4ac

a = float(input('Enter A >>>'))
b = float(input('Enter B >>>'))
c = float(input('Enter C >>>'))

discr = b ** 2 - 4 * a * c

if discr > 0:
    x1 = (-b + discr ** 0.5) / 2 * a
    x2 = (-b - discr ** 0.5) / 2 * a

    print('X1 = {} X2 ={}'.format(x1, x2))

elif discr == 0:
    x = -b / (2 * a)

    print('X = ', x)
else:
    print('D < 0')
