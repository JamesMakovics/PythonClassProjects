#Converts the secret word to asterisks

def replace_with_asterisks(s):
    for letters in s:
        if letters == "-":
            pass
        else:
            letters = "*"
    return s
