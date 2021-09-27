txt = input("Enter a character between a/A and z/Z: ")

if txt.isalpha():
    print(txt.swapcase())
else:
    print("Please enter letters only")