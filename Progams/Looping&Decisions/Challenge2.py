#CDWorth
deposit = 2500
years = 0
while deposit < 5000:
    deposit += deposit * .75
    years += 1
print("After ", years, " years. your deposit is worth: ", deposit)

print()
print()

#F2C
F_temp_list = []
C_temp_list = []
temps_count = 0
def valid_input():
    global temps_count
    while temps_count < 5:
        try:
            user_temp_F = int(input("Enter a temperature in Fahrenheit: "))
            f2c(user_temp_F)
        except ValueError:
            print("Please try again!")
            valid_input();
    organize_list(C_temp_list, F_temp_list)
def f2c(user_temp_F):
    global temps_count
    global F_temp_list
    global C_temp_list
    user_temp_C = (user_temp_F - 32) * 5/9
    user_temp_C = round(user_temp_C,2)
    C_temp_list.append(user_temp_C)
    F_temp_list.append(user_temp_F)
    temps_count += 1

def organize_list(C_temp_list, F_temp_list):
    C_temp_list = sorted(C_temp_list, key=int)
    F_temp_list = sorted(F_temp_list, key=int)
    print_table(C_temp_list,F_temp_list)


def print_table(C_temp_list, F_temp_list):
    count = 0
    print("F        C")
    while count < len(C_temp_list):
        print(F_temp_list[count],"  ",C_temp_list[count])
        count += 1

valid_input()

print()
print()

printCheckerBoard = 0 #Amount of spaces and * is 16
printRows = 0 #Amount of rows in the board is 8
def printOddRow():
    global printCheckerBoard
    printCheckerBoard = 0
    while printCheckerBoard < 8: #This needs to be halfed because the space and astrik are printed together
        print("*", end='')
        print(" ", end='')
        printCheckerBoard += 1

def printEvenRow():
    global printCheckerBoard
    printCheckerBoard = 0
    while printCheckerBoard < 8: #This needs to be halfed because the space and astrik are printed together
        print(" ", end='')
        print("*", end='')
        printCheckerBoard += 1

while printRows < 4: #This needs to be halfed because the even and odd rows are printed together
    printOddRow()
    print()
    printEvenRow()
    print()
    printRows += 1

print()
print()

#n!
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

user_factorial = int(input("Please enter a number to be set to a factorial: "))
n = user_factorial
print("The factorial of ", user_factorial, " is: ", factorial(n))

print()
print()

#EstimateE

factorialList = []
totalFactorials = 0

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def addToListOfFactorials():
    global stopAt
    if factorial(n) == 1:
        factorialList.append(factorial(n))
    else:
        factorialList.append(1/factorial(n))

user_factorial = int(input("Please enter a number to be set to guess e: "))
stopAt = 0
while stopAt < user_factorial:
    n = stopAt
    addToListOfFactorials()
    stopAt += 1
print("e is: ", round(sum(factorialList),2))

print()
print()
#ParseNums

user_strNums = str(input("Enter a set of numbers: "))
print("The string of numbers is: ")
i = 0
numList = [int (numList) for numList in str(user_strNums)]
while i < len(numList):
    print(numList[i])
    i += 1

print()
print()
#SumDigits
user_strNums = int(input("Enter a set of numbers: "))
print("The sum of the string of numbers is: ", sum(map(int,str(user_strNums))))

print()
print()
