import re
import datetime

def replace(search, write):
    with open("C:\PROG1783 Final Exam\PROG1783File2.txt", "r+") as f1:

        

        t = datetime.datetime.now()
        time = t.strftime("%m-%d-%Y, %Hh:%Mm:%Ss")

        file = f1.read()
        file = re.sub(search, write, file)

        f1.write(file)
        f1.write(time)






search = "Mitchell McColl 8761950"
write = "********"

replace(search, write)

file1 = open("C:\PROG1783 Final Exam\PROG1783File2.txt", "r")
print(file1.read())