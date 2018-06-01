#Creates a snack vending machine

snackNums = [5,5,5,5,5,5,5,5,5,5]
itemNames = ["FruitSnack","PotatoChips","Brownies","Twinkies","Gabe","Iced Tea","TV","Football","Taco","Java"]
itemDescription = ["Classic Welches", "A bag of air", "Fudge snack", "A fried snack with a cream filling", "He needs a home and maybe a girlfriend", "Goes perfect with Gabe", "For the yearly Yule Log, but don't leave Gabe in front of it too long", "Eagles are #1", "A festive mexican treat", "Dark roast 100% Columbian"]
itemCost = [1.50,1.50,1.50,1.50,1.50,1.50,1.50,1.50,1.50,1.50]
itemAvalible = [True,True,True,True,True,True,True,True,True,True]
moneyInMachine = 0.00

def itemSelection(snackNums, itemNames, itemDescription, itemCost, itemAvalible):
    displayNum = 0

    while displayNum <= 9:
        print("Press ", displayNum + 1, " for ", itemNames[displayNum] + ":\n", itemDescription[displayNum] + "\n", "Cost: ", "$" + itemCost[displayNum], "\n", "Snacks left: ", snackNums[displayNum], "\n", itemAvalible[displayNum])
        displayNum += 1

    print("\nPress 0 for main menu")


def mainMenu():
    print("Press 1 for itemSelection\nPress 2 for Restock items\nPress 3 for counting money\n Press 4 to remove money")

def emptyMoney():
    global moneyInMachine
    moneyInMachine = 0.00

def showMoney():
    global moneyInMachine
    print(moneyInMachine)
