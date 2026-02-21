# reversed_string = "".join(reversed(input("Enter a word: ")))
# print(reversed_string)

def reverse_string():
    string = input("Enter a word: ")
    reversed_string = ""

    for i in range(len(string) -1, -1, -1):
        reversed_string += string [i]
    print(reversed_string)

reverse_string()


