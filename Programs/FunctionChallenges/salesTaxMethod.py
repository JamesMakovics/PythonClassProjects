tax = .06

def salesTax(tax, item):
    print("The item costs: $", item + (item * tax))

item = float(input("Enter how much the item was: "))
salesTax(tax, item)
