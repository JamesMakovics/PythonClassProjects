#Boolean Values - Video Game Skyrim
health = 75
dragonrend = False

item = int(input("You find dragonrend shout, Do you want to pick it up?\n Press 1 - to pick it up \n Press 2 - to not pick it up \n"))
if item == 1:
    print("You picked up dragonrend")
    dragonrend = True
elif item == 2:
    print("You keep walking")
    dragonrend = False
else:
    print("That is not an option")
print("You are walking in the woods and you come across")
print("You call a mysterious horse")
print("The dragon atacks you!")

if dragonrend == True and health > 50:
    print("You attack and beat the dragon")
else:
    print("The dragon toasts you and you become his dinner") #OOOOOOOOOOOOOOOOOOOF #MEGA OOOOOOOOOOOOOOOOOOOF
