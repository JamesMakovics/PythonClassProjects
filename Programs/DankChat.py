user_name = str(input("What is your name?"))
#input() is a function call and storing value
#into user_name

print("Hi - welcome", user_name)

user_last4Digits = str(input("What is your last four digits of your social security number?"))

print("Wow", user_name, "You're last four digits are", user_last4Digits)

user_csc = str(input("What is the csc on your credit card? P.S. its on the back of your card!"))

user_nameInBinary = str(input("Now, all I need is your name in binary!"))

print("Ok, lets run this through one more time!")

print("Your name is", user_name)

print("The last four digits of your social security are", user_last4Digits)

print("The csc on the back of your card is", user_csc)

print("Finally, your name in binary is", user_nameInBinary)

user_confirm = str(input("Is this correct?"))

if user_confirm == "yes":
    print("Goodbye!")
elif user_confirm != "yes" or "no":
    print("Are you unsure of something fool!?")
else:
    print("Thanks for the fake information")