'''
while loop – A control statment that repeats until a condition is met


loop body – Where the method is repeated until the condition is met


iteration – Repeating the same code until a condtion is met


infinite loop – A control statment that repats forever


loop variable – A variable that controls when the loop is broken


counter – A variable that increases with the number of times a loop body is run


break – Gets the loop to stop where the loop condition does not have to be met


Continue – Keeps the program running after a 'if' statement is run

'''
user_number = int(input("Enter a number: ")) #Counts from the number the user had entered to 100

while(user_number < 100):
    if user_number >= 100:
        break
    else:
        user_number += 1

if user_number > 100:
    print("The number ", user_number, " was ", user_number - 100, " Higher than 100")
else:
    print("The number you entered is now ", user_number)
