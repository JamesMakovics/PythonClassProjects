#Checks if a substring matches the first part of the string

def startsWith(s,sub):
    subLength = len(sub)
    if sub == s[:subLength]:
        return True
    elif s == sub:
        return True
    else:
        return False
