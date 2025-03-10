def check_number(num):
    input("Check number if its Even Number or Odd Number")
    num = int(input("Number:"))
    if num % 2 == 0:
        print(num, "is an Even Number")
    else:
        print(num, "is an Odd Number")
check_number(num)