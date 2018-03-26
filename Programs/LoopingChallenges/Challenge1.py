#Username and Password Check
password = "happiness"
attempts = 0
'''
Checks if user has entered the correct username or Password
'''

while attempts <= 3:
    ask_for_password = str(input("password: "))

    if password == ask_for_password:
        break

    else:
        print("Please try again")
        attempts += 1

'''
This is executed after the while is broken
'''
if password == ask_for_password:
    print("Welcome!")
else:
    print("Access denied")

print()
print()


#enter positive integer
user_num = int(input("Please enter a positive integer: "))
while True:
    if user_num < 0:
        print("The number must be positive!")
        user_num = int(input("Please re-enter: "))
    else:
        break
print("Thankyou!")

print()
print()
#RangeInput
user_num = int(input("Please enter a positive integer that is 1 - 20: "))
while True:
    if user_num <= 0 or 20 < user_num:
        print("The number must be positive and less than 20!")
        user_num = int(input("Please re-enter: "))
    else:
        break
print("Thankyou!")

print()
print()
#Average
averagelist = []
while user_num != 0:
    user_num = int(input("Enter a value (0 to quit): "))
    if user_num != 0:
        averagelist.append(user_num)
sum_of_list = sum(averagelist)
if sum_of_list != 0:
    average = sum_of_list / len(averagelist)
    if average < 70:
        print("Average: ", "25.0%")
    else:
        print("Average: ", average, "%")


print()
print()
#whileSum
x = 0
numbers_printed = []
while x <= 12:
    numbers_printed.append(x)
    print(x)
    x += 1

print("Sum: ", sum(numbers_printed))

print()
print()

#whileSum2-20
x = 2
numbers_printed = []
while x <= 20:
    numbers_printed.append(x)
    print(x)
    x += 2

print("Sum: ", sum(numbers_printed))

print()
print()
#whileSum20-1
x = 20
numbers_printed = []
while x >= 0:
    numbers_printed.append(x)
    print(x)
    x -= 1

print("Sum: ", sum(numbers_printed))

print()
print()
#whileSumOdd
x = 1
numbers_printed = []
user_num = int(input("Enter a positve integer: "))
while x <= user_num:
    if x % 2 == 1:
        numbers_printed.append(x)
        print(x)
        x += 1
    else:
        x += 1

print("Sum of odd numbers is: ", sum(numbers_printed))
