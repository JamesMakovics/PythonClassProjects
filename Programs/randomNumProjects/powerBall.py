#powerball
import random
powerballJackpotNums = []
powerballNum = 0
import time

powerballJackpotNums.append(random.randint(1,69))
powerballJackpotNums.append(random.randint(1,69))
powerballJackpotNums.append(random.randint(1,69))
powerballJackpotNums.append(random.randint(1,69))
powerballJackpotNums.append(random.randint(1,69))

powerballNum = random.randint(1,26)

for x in range (0,5):
    b = "Loading your Jackpot numbers" + "." * x
    print (b, end="\r")
    time.sleep(1)
print()
print ("Your powerball numbers are: ", powerballJackpotNums)

for x in range (0,5):
    b = "Loading your powerball number" + "." * x
    print (b, end="\r")
    time.sleep(1)
print()
print(powerballNum)
