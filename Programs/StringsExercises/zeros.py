#Removes the leading zeros before the first non-zero digit

def removeLeadingZeros(s):
    zeroNum = 0
    while s[zeroNum] == "0":
        zeroNum += 1
    return s[zeroNum:]
