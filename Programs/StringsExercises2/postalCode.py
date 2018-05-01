#Checks if the input is a valid Canadian Postal code

def code(s):
    i = 0
    postalCode = s.strip()
    postalCode = postalCode.upper()
    #Postal code format "ADA DAD" A is a letter and D is a digit
    for intergers in postalCode:
        if i == 0 or i == 2 or i == 4:
            if intergers[i].isalpha():
                pass
            else:
                postalCode = "Invalid"
                return postalCode
        if i == 1 or i == 3 or i == 5:
            if intergers[i].isdigit():
                pass
            else:
                postalCode = "Invalid"
                return postalCode
        i = i + 1
    return postalCode
