#Bad Tips

user_totalBill = float(input("Total Bill:$ "))
user_tip = float(input("Tip:$ "))

percentage_tip = user_tip / user_totalBill

if percentage_tip < .10:
    print("terrible")

if .10 < percentage_tip < .20:
    print("fair")

if .20 == percentage_tip:
    print("good")

if .20 < percentage_tip:
    print("great")

else:
    print("Invalid Entry")
