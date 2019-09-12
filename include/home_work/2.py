# a b x; if x betwen a and b

a = int(input('Enter A >>>'))
b = int(input('Enter B >>>'))
x = int(input('Enter X >>>'))

if a < x and b > x:
    print(True)
elif a == x or b == x:
    print("такого не было в требованиях")
else:
    print(False)