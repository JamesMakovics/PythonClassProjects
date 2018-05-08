def passwordValid(s):
    correctLength = False #Boolean variables
    upperCaseFound = False
    lowerCaseFound = False
    symbolFound = False
    digitFound = False
    passwordValid = False

    if len(s) >= 6: #is length greater than or equal to 6
        correctLength = True #passes check
    for letters in s: #for loop, that checks every index in s
        if letters.isupper(): #checks if letter is uppercase
            upperCaseFound = True #satifies the condition

        if letters.islower(): #checks for a lowercase letter
            lowerCaseFound = True #this is set to true otherwise its false

        if (ord(letters) > 32 and ord(letters)< 48) or (ord(letters) > 57 and ord(letters) < 65): #Captures all symobls and compares them to the character
            symbolFound = True #if a symbol is found this satifies the condition

        if letters.isdigit(): #checks if the index is an int
            digitFound = True #sets to true if condition is satified

    if correctLength == True and upperCaseFound == True and lowerCaseFound == True and symbolFound == True and digitFound == True:
#checks if all the boolean values have become true
        passwordValid = True # sets to true
    return passwordValid #returns the password

#NEED TO SET WHERE THE PASSWORD FAILED

def whatWentWrong(correctLength,upperCaseFound,lowerCaseFound,symbolFound,digitFound):
    if not correctLength:
        print("Your password is not the correct length")
    if not upperCaseFound:
        print("Your password does contain an uppercase letter")
    if not lowerCaseFound:
        print("Your password does not contain a lowercase letter")
    if not symbolFound:
        print("Your password does not contain a symbol")
    if not digitFound:
        print("Your password does not contain a digit")

if passwordValid("Ha$ters2"):
    print("Password valid")
else:
    print(whatWentWrong(correctLength,upperCaseFound,lowerCaseFound,symbolFound,digitFound))
