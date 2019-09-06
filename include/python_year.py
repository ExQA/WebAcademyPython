YEAR_PYTHON = 1991
DELTA = 10

year_user = float(input(">>>>>> "))
delta_usr = abs(year_user - YEAR_PYTHON)

if delta_usr ==0:
    print("Goood!!!")
elif delta_usr <= DELTA:
    print("Almost win!!")
else:
    print("no win")