year = int(input("enter the number :  "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("year {0} is a leap year")
        else:
            print("year {0} is a leap year")
    else:
        print("year {0} is a leap year")
else:
    print("year {0} is not a leap year")





