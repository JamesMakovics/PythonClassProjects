#Dog years

user_humanYears = float(input("Enter your dogs age: "))

if user_humanYears == 1:
    print("Your dog is 14 years old!")

elif user_humanYears == 2:
    print("Your dog is 22 years old!")

elif user_humanYears > 2:
    dog_age = 22 + ((user_humanYears - 2) * 5)
    print("Your dogs age is ", dog_age, " years old!")

else:
    print("Not a valid number!")
