num = 0
fac = 0

def factorial(num):
    countdown = num
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        print(countdown)
        countdown -= 1
    return fact
    

num = int(input("Please enter your number here: "))
fac = factorial(num)
print("Your factiorial for the number " + str(num) + " is " + str(fac))


