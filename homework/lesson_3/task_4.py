input_year = input("Input the year please")

current_year = int(input_year)

min_year = 1900
max_year = 1000000

if min_year < current_year < max_year:
    if current_year % 4 == 0 and current_year % 100 != 0:
        print(current_year, ": is a leap year")
    elif current_year % 400 == 0:
        print(current_year, ": is a leap year")
    else:
        print(current_year, ": is not leap year")
else:
    print("Year out of range")
