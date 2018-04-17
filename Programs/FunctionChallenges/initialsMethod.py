def initials(first, middle, last):
    print(first + " " + middle + " " + last)
    print(first + " " + last + " " + middle)

first = str(input("Enter your first initial: "))
middle = str(input("Enter your middle initial: "))
last = str(input("Enter your last initial: "))
initials(first, middle, last)
