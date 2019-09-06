

YEAR_PYTHON = 1991
DELTA = 16

year_user = float(input('Год создания python: '))

delta_user = abs (year_user - YEAR_PYTHON)

if delta_user ==0:
    print('good!!!')

elif delta_user <= DELTA:
    print("go to wiki")

else:
    print("Вообще не попал!!")



