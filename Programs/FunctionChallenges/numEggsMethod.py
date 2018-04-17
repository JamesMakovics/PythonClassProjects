
def numberOfEggs(numEggs):
    if(numEggs % 12 == 0):
        print(int(numEggs / 12), " dozen eggs")
    else:
        remainder = numEggs % 12
        print(numEggs, " eggs is ", int(numEggs / 12), " dozen ", "with a remainder of ", int(remainder), " eggs")

numEggs = float(input("Enter number of eggs: "))
numberOfEggs(numEggs)
