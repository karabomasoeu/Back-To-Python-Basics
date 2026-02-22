def largest_number():
    number_list = []

    for i in range (5):
        numbers = int(input("Enter a number: "))
        number_list.append(numbers)

    base_number = number_list[0]

    for number in number_list:
        if number > base_number:
         base_number = number
    return base_number

print(largest_number())
