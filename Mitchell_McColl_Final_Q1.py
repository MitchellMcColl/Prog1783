

characters = 100

f1 = open ("C:\Conestoga\PROG1783File1Before.txt", "r")
f2 = open ("C:\Conestoga\PROG1783File1After.txt", "a")

f2.write(f1.read(characters))

f1.close()
f2.close()
