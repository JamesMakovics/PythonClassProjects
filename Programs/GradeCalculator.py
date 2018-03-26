#Grade Calculator 2.0

print("Welcome to the Grade Calculator 2.0")

print("This will take your score and turn it into a letter grade")


user_input = float(input("Enter your score: "))

if user_input == 100:

    print("Your grade is an A+")

elif 100 > user_input > 96.5:

    print("Your grade is an A")

elif 96.5 > user_input > 92.5:

    print("Your grade is an A-")

elif 92.5 > user_input > 88.5:

    print("Your grade is an B+")

elif 88.5 > user_input > 84.5:

    print("Your grade is an B")

elif 84.5 > user_input > 80.5:

    print("Your grade is an B-")

elif 80.5 > user_input > 76.5:

    print("Your grade is an C+")

elif 76.5 > user_input > 72.5:

    print("Your grade is an C")

elif 72.5 > user_input > 68.5:

    print("Your grade is an C-")

elif 68.5 > user_input > 64.5:

    print("Your grade is an D+")

elif 64.5 > user_input > 60.5:

    print("Your grade is an D")

elif 60.5 > user_input > 56.5:

    print("Your grade is an D-")

elif 56.5 > user_input > 0:

    print("Your grade is an F")

