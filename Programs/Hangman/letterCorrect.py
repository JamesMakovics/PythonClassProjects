#Checks if the letter is correct
guessedLetters = []

def is_letter_correct(s):

    import secretWords
    import Hangman
    global guessedLetters
    if s in Hangman.secretWord and s not in guessedLetters:
        guessedLetters.append(s)
        return "correct"
    elif s in Hangman.secretWord and s in guessedLetters:
        return "chosen"
    elif s not in Hangman.secretWord and s in guessedLetters:
        return "chosen"
    elif s not in Hangman.secretWord and s not in guessedLetters:
        guessedLetters.append(s)
        return "incorrect"
