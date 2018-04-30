#Checks if the name of a class or method is valid in python

def isValidName(s):
    str = s
    try:
        if(s[0].isdigit() == True or str.startswith('#') == True or str.startswith(" ") == True or str.startswith("[") == True or str == ""):
            return False
        else:
            return True
    except:
        return False
