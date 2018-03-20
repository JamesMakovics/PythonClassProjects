feeling = str(input("How are you today?: "))
#printing line,taking an input, casting to
#a string and storing it into a variable
#feeling
feeling = feeling.lower()

if feeling == 'good': #if statement
    print("That's great!")
    print("Have a good day!")
elif feeling == 'bad': #else-if statement
    print("Oh, no!")
    print("Hope that you don't fail this class")
elif feeling == 'great': #else-if statement
    print("Is that it?")
else:
    print("ok")


print(feeling)
