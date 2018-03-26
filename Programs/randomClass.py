#Random class
import random

i = 0
num_count = 0
num_has_appeared = [0,0,0,0,0,0,0,0,0,0]

while i < 100:
    random_number = random.randint(0,9)
    print(random_number)
    while num_count < 9:
        if random_number == num_count:
            num_has_appeared[num_count] += 1
        num_count += 1
    i += 1
    num_count = 0
print("Zero has appeared: ", num_has_appeared[0] / 100, " of the time")
print("One has appeared: ", num_has_appeared[1] / 100, " of the time")
print("Two has appeared: ", num_has_appeared[2] / 100, " of the time")
print("Three has appeared: ", num_has_appeared[3] / 100, " of the time")
print("Four has appeared: ", num_has_appeared[4] / 100, " of the time")
print("Five has appeared: ", num_has_appeared[5] / 100, " of the time")
print("Six has appeared: ", num_has_appeared[6] / 100, " of the time")
print("Seven has appeared: ", num_has_appeared[7] / 100, " of the time")
print("Eight has appeared: ", num_has_appeared[8] / 100, " of the time")
print("Nine has appeared: ", num_has_appeared[9] / 100, " of the time")
