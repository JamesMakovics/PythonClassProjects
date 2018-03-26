#Height for ride

user_height = float(input("Enter your height in feet: "))
print()

height_in_inches = user_height * 12

ride_list_NoHeight = ["Raja's Rickshaws", "Bugs Bunny National Park Water Tower", "Bugaboo", "Daffy's Deep Diver", "Safari Off Road Adventure"]

ride_list_36 = ["Bugs Bunny Camp Carousel", "Rock Wall", "Bugs Bunny Ranger Pilots", "Foghorn Leghorn's Stagecoach Express", "Jumpin' Joey", "Wile E. Coyote Canyon Blaster", "Parachute Training Center: Edwards AFB", "Air Safari", "DejaVu", "Safari Tours", "Congo Rapids"]

ride_list_40 = ["Great American Road Race"]

ride_list_41 = ["Harley Quinn Crazy Train"]

ride_list_42 = ["Sky Zooma", "Splash Water Oasis", "Enchanted Teacups", "Tango", "Road Runner Railway", "Daffy's Hot Air Balloons", "Skyway - Frontier Adventures", "Taz's Tornado", "Saw Mill Log Flume", "Dare Devil Dive", "Skyway - Lakefront", "Pepe'Le Pew's Hearts Aweigh", "Buccaneer", "Carousel", "Porky Pig's Camp Wagons", "Bugs Bunny Barnstormer", "Swashbuckler", "Big Wheel", "Justice League: Battle for Metropolis", "Fender Benders", "The Dark Knight Coaster"]

ride_list_44 = ["Soaring Eagle", "Slingshot", "Runaway Mine Train", "SkyScreamer"]

ride_list_48 = ["Skull Mountain", "The Joker", "Houdini's Great Escape", "Air Jumbo", "El Diablo", "Jolly Roger", "Zumanjaro: Drop of Doom"]

ride_list_52 = ["El Toro"]

ride_list_54 = ["Cyborg Cyber Spin", "Green Lantern", "Twister", "Nitro", "Bizarro", "Superman: Ultimate Flight", "Batman The Ride", "Kingda Ka"]


for ride_list_NoHeight in ride_list_NoHeight:
    print(ride_list_NoHeight, (" - No Height Limit"))
    print()

if(height_in_inches >= 36):
    for ride_list_36 in ride_list_36:
        print(ride_list_36, (" - 36 inches"))
        print()

if(height_in_inches >= 40):
    for ride_list_40 in ride_list_40:
        print(ride_list_40, (" - 40 inches"))
        print()

if(height_in_inches >= 41):
    for ride_list_41 in ride_list_41:
        print(ride_list_40, (" - 41 inches"))
        print()

if(height_in_inches >= 42):
    for ride_list_42 in ride_list_42:
        print(ride_list_42, (" - 42 inches"))
        print()

if(height_in_inches >= 44):
    for ride_list_44 in ride_list_44:
        print(ride_list_44, (" - 44 inches"))
        print()

if(height_in_inches >= 48):
    for ride_list_48 in ride_list_48:
        print(ride_list_48, (" - 48 inches"))
        print()

if(height_in_inches >= 52):
    for ride_list_52 in ride_list_52:
        print(ride_list_52, (" - 52 inches"))
        print()

if(height_in_inches >= 54):
    for ride_list_54 in ride_list_54:
        print(ride_list_54, (" - 54 inches"))
        print()
