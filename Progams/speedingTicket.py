stock_ticket = 20.00

speed_limit = float(input("What is the speed limit?: "))

user_speed = float(input("How fast are you going?: "))

over_limit = user_speed - speed_limit

if user_speed <= speed_limit:
    print("You will not recieve a ticket!")

else:
    ticket = (over_limit * 5) + stock_ticket
    print("FINE------------------: $%0.2f" % (ticket))
