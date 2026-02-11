print("Enter the year :")
year = int(input())

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) :
    print(f"{year} is leap year")
else :
    print("Not a leap year")