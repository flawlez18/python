year = int(input("please enter the year to check: "))

if year % 4 == 0:
    condition_b = year % 100
    if condition_b != 0:
        print("leap year")
    else:
        condition_c = year % 400
        if condition_c == 0:
            print("Leap year")
        else:
            print("Not leap year")

    # else:
    #     print("Leap year")

else:
    print("Not leap year")