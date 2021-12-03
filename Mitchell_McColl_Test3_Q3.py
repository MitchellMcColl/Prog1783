n = int(input("Enter the ending number: "))
#changed sum initialization from 5 to 0
sum = 0
#removed unessesary m variable
#removed the ,2 from the range
for num in range(1, n + 1):
#changed sum = sum + num to sum += num
    sum += num
print("The sum of the first", n, "numbers is: ", sum)
#changed: sum / (n + 1) to just: sum / n
average = sum / n
#changed m variable to n variable
print("The average of the first", n, "numbers is: ", average)