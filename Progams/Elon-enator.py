#Chatbot
user_wants_vegan = False

user_wants_dairy = False

user_wants_meal_warm = False

meal_list = ["yogurt", "CheeseSteak", "Vegan Chili", "A singular peice of Brocoli"]

elon_age = 46

user_name = str(input("Whats your name?: "))

print("Hello, ", user_name, " welcome to the Elon-enator")

print("Let's see what decisions you would make as Elon Musk")


user_age = int(input("First I need to know your age!: "))

if user_age < elon_age:
    age_difference = elon_age - user_age
    print("Wow what an achievement you are ", age_difference, " years younger than Elon.")
    print("Pretty impressive for only being", user_age, " years old")
else:
    age_difference = user_age - elon_age
    print("Well your only ", age_difference, " years late")


print("We have a new experimental program for calculating a persons' weight in stone")

user_choice = str(input("Would you like to try the experimental program?: "))

if user_choice.lower() == "yes":

    print("Well lets get to it")
    user_weight_LB = float(input("How much do you weigh?: "))

    weight_stone = float((user_weight_LB * 2.2))

    print("Your weight in stone is: %0.2f" % (weight_stone), end=' Stones')

else:
    print("Too bad!")


print("Lets move on to another program you need to test Elon!")

print("For this test you need to enter your food perferences")

user_preference = str(input("Do you like meat?: "))
if user_preference.lower() == 'yes':
        user_wants_vegan = False
else:
    user_wants_vegan = True

user_preference = str(input("Do you like dairy?: "))
if user_preference.lower() == 'yes':
    user_wants_dairy = True
else:
    user_wants_dairy = False

user_preference = str(input("Do you like meal warm?: "))

if user_preference.lower() == 'yes':
    user_wants_meal_warm = True
else:
    user_wants_meal_warm = False

print("Here is the item of choice for you")

if user_wants_vegan == False and user_wants_dairy == True and user_wants_meal_warm == False:
    print(meal_list[1])
if user_wants_vegan == False and user_wants_dairy == True and user_wants_meal_warm == True:
    print(meal_list[2])
if user_wants_vegan == True and user_wants_dairy == False and user_wants_meal_warm == True:
    print(meal_list[3])
if user_wants_vegan == True and user_wants_dairy == False and user_wants_meal_warm == False:
    print(meal_list[4])
else:
    print("Just Starve!")
