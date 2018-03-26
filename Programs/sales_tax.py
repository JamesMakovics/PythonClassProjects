# firmatting decimal to print

shirt = 15.00
sales_tax = .06
total = (shirt * sales_tax) + shirt

print("The total of the item is: $%0.2f" % (total))
