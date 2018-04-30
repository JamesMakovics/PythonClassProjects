#Tests methods
import endsWith
import startsWith
import twoCaps
import digits
import zeros
import nameValidation

s = "Hello"
sub = "Hello"
sub2 = "Hello"
test = "GOodbye"
strOfDigits = "1 @ 31 $$2***"
leadingTest = "0000000000123354325234523"

validName1 = 'bDay'
validName2 = 'A0'
validName3 = '_a_1'
validName4 = '_lamt'
validName5 = '__'
validName6 = '_'

nonvalidName1 = '1a'
nonvalidName2 = '#A'
nonvalidName3 = '1_a'
nonvalidName4 = '[a]'
nonvalidName5 = ' ABC'
nonvalidName6 = ''

print("Tests endswith method")
print(endsWith.endsWith(s,sub))
print("Tests startswith")
print(startsWith.startsWith(s,sub2))
print("Tests twoCaps")
print(twoCaps.caps(test))
print("Tests getDigits")
print(digits.getDigits(strOfDigits))
print("Tests removeLeadingZeros")
print(zeros.removeLeadingZeros(leadingTest))

print("Tests valid names")
print(nameValidation.isValidName(validName1))
print(nameValidation.isValidName(validName2))
print(nameValidation.isValidName(validName3))
print(nameValidation.isValidName(validName4))
print(nameValidation.isValidName(validName5))
print(nameValidation.isValidName(validName6))

print("Tests invalid names")
print(nameValidation.isValidName(nonvalidName1))
print(nameValidation.isValidName(nonvalidName2))
print(nameValidation.isValidName(nonvalidName3))
print(nameValidation.isValidName(nonvalidName4))
print(nameValidation.isValidName(nonvalidName5))
print(nameValidation.isValidName(nonvalidName6))
