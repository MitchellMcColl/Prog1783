num = []

def largestNumber(num):
    print("The largest number you entered was: ", max(num))

for i in range(5):
    x = int(input("Please enter your number: "))
    num.append(x)

largestNumber(num)

