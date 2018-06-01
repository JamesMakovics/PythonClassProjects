
number = "2157717072"
def formatTelephone(str):
    #will return, Sample: xxx-xxx-xxxx
    newNumber = ""
    count = 1
    finalDigits = 10
    for numbers in str:
        if numbers.isdigit() and count != 3:
            newNumber += numbers
            count += 1
            finalDigits += -1
        elif numbers.isdigit() and count == 3 and finalDigits > 4:
            newNumber += numbers + "-"
            count = 1
            finalDigits += -1

        elif numbers.isdigit() and finalDigits <= 4:
            newNumber += numbers

    return newNumber

print(formatTelephone(number))
