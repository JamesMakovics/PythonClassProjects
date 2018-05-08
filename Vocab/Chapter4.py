#function – a set of code that can be called multiple times


#function call – an object that can accept arguments


#def – creates a function reference


#function definition – an executable statement


#block – a piece of code that is executed as a unit


#return – an output that can be interpreted by other statements


#parameter – an input that is acccepted into a function


#argument - parameters that are accepted by an object


#return statement – a statement that can be returned to a method or another object


#none - a null equivalent

'''
Please provide 2 examples of a function and a function call.
One function should take 2 parameters and one should have no parameters.
Write or type the code below:
'''

#F2C
F_temp_list = []
C_temp_list = []
temps_count = 0
def valid_input():
    global temps_count
    while temps_count < 5:
        try:
            user_temp_F = int(input("Enter a temperature in Fahrenheit: "))
            f2c(user_temp_F)
        except ValueError:
            print("Please try again!")
            valid_input();
    organize_list(C_temp_list, F_temp_list)
def f2c(user_temp_F):
    global temps_count
    global F_temp_list
    global C_temp_list
    user_temp_C = (user_temp_F - 32) * 5/9
    user_temp_C = round(user_temp_C,2)
    C_temp_list.append(user_temp_C)
    F_temp_list.append(user_temp_F)
    temps_count += 1

def organize_list(C_temp_list, F_temp_list):
    C_temp_list = sorted(C_temp_list, key=int)
    F_temp_list = sorted(F_temp_list, key=int)
    print_table(C_temp_list,F_temp_list)


def print_table(C_temp_list, F_temp_list):
    count = 0
    print("F        C")
    while count < len(C_temp_list):
        print(F_temp_list[count],"  ",C_temp_list[count])
        count += 1

valid_input()
