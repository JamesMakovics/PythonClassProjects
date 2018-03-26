#price of the T-Shirt
T_shirt = 15.00

#Asks user how much money they have
user_money = float(input("How much money do you have?: $"))

money_leftover = user_money - T_shirt

print("The T-Shirt is $15!")

print("You have: $ %0.2f" % (user_money))

user_wouldLikeAShirt = str(input("Would you like to buy a T-Shirt?: "))

if user_wouldLikeAShirt == "yes" and user_money >= T_shirt:
    print("Your new balance is: $ %0.2f" % (money_leftover))
elif user_wouldLikeAShirt != "yes" or "no" and user_money >= T_shirt:
    print("You did not input 'yes' or 'no' so you bought one anyway")
    print("Your new balance is: $ %0.2f" % (money_leftover))
else:
    print("DUDE BE NICE!")
