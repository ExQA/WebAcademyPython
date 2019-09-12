#Count all money

def bank(summa, years):
    percent_per_annum = 0.1
    for i in range(years):
        summa = summa + summa * percent_per_annum

        return print(summa)


summa = int(input("Enter your summa >> "))
years = int(input("Enter count of year >>>"))

bank(summa, years)