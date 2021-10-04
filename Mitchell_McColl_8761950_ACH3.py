num = 0
x = 1
sum = 0
num = int(input("Please input your number here: "))

while(x <= num):
    if(x % 2 == 0):
        sum += x * x
    x += 1    
print(sum)