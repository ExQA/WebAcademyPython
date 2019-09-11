#365 366
year = int(input("Enter Year >>> "))

def intercalary_year(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print("usual year")
        return False
    else:
        print("intercalary year")
        return True

print(intercalary_year(year))