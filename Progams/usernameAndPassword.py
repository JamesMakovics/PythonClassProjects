#Username and Password Check


username = "James"

password = "happiness"

attempts = 0

has_user_name = False


'''
Checks if user has entered the correct username or Password
'''

while attempts <= 3:
    if has_user_name == False:
        ask_for_username = str(input("user: "))
    ask_for_password = str(input("password: "))

    if username == ask_for_username and password == ask_for_password:
        break

    elif username == ask_for_username and password != ask_for_password:
        print("Incorrect password")
        has_user_name = True
        attempts += 1

    else:
        print("Please try again")
        attempts += 1

'''
This is executed after the while is broken
'''
if username == ask_for_username and password == ask_for_password:
    print("Welcome!")
else:
    print("Access denied")




#
