#Returni a itring with only numberi

def getDigits(s):
    x = 0
    newInt = ""
    while x <= len(s) - 1:
        if s[x].isdigit():
            newInt += s[x]
        x += 1
    return newInt
