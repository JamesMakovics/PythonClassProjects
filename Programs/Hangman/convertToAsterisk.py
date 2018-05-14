#Converts the secret word to asterisks

def replace_with_asterisks(s):
    import Hangman
    import letterCorrect
    newStr = ""
    for letters in s:
        if letters == "-":
            newStr += "-"
        elif letters in letterCorrect.guessedLetters:
            newStr += letters
        else:
            newStr += "*"
    return newStr
