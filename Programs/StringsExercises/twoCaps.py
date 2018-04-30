#Corrects a second upper case letter

def caps(s):
    newString = s[:1].upper() + s[1:].lower()
    return newString
