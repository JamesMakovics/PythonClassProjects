#Checks if the substring matches the end of the string

def endsWith(s,sub):
    subLength = len(sub) - 1
    if s[subLength:] == sub:
        return True
    elif s == sub:
        return True
    else:
        return False
