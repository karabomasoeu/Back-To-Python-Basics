def PositiveOrNegative():
number = int(input("Enter any number: "))

if number > 0:
        print(f"{number} is positive!")
    elif number < 0:
        print(f"{number} is negative!")
    else:
        print(f"{number} is zero!")

PositiveOrNegative()
