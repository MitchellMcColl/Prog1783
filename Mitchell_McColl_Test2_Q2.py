class LargestValue:
    def __init__(self, storenum,largestnum):
        self.largestnum = largestnum
        self.storenum = storenum

    
    def maxValue(self):
        global largestnum, storenum
        largestnum = max(storenum)
        return



storenum = []
largestnum = 0.0
val = LargestValue(storenum, largestnum)

print("Please enter 3 numbers here: ")
for i in range(3):
    x = float(input())
    storenum.append(x)

val.maxValue()

print("The largest number you inputed was: " + str(largestnum))