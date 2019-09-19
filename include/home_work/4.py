# S = pi * R ˆ2
import math
import re


while True:
    R = input('Enter radius >>> ').strip()

    if not re.match("(?<=>)\d+.\d+|\d+", R):
        print ("Error! Make sure you only use float data")
    else:
        radius = float(R)
        s = math.pi * radius ** 2
        print('S = ', s)
        break





