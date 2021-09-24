txt = input("Please enter your input here: ")


if txt.isalpha():
    print("A letter was entered")
elif txt.isdigit():
        print("A digit was entered")
elif txt.isspace():
    print("A space was entered")
else:
    print("ERROR")