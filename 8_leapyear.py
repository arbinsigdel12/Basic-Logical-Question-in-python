# Find if the given year is leap or  not

num=int(input("Enter a date: "))

if num%4==0 or num%100==0 or num%400==0:
    print("The year is leap year")
else:
    print("The year is not leap year")
