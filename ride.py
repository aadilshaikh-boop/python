print("============================================")
print("          welcome to ride builder           ")
print("============================================")
print()

print("step 1 : choose your vehicle")
print("1. bike")
print("2. car")
print()

choice = int(input("Enter 1 or 2 : "))
print()
if choice == 1:
    print("pick your bike type")
    print("1. scooty")
    print("2. mountain bike")
    print()

    bike_choice = int(input("Enter 1 or 2 : "))
    print ()

    if bike_choice == 1:
        print("you have selected scooty")
        print("top speed : 80 km/h")
        print ("best for city roads")
    else:
        print("you have selected mountain bike")
        print("top speed : 40 km/h")
        print ("best for off road trails ")

elif choice == 2:
    print("pick your car type")
    print("1. sedan")
    print("2. SUV")
    print()

    car_choice = int(input("Enter 1 or 2 : "))
    print()

    if car_choice == 1:
        print("you have selected sedan")
        print("seating capacity : 5")
        print("best for highway driving")
    else:
        print("you have selected SUV")
        print("seating capacity : 7")
        print("best for off road ")

else:
    print("that is not a valid choice.")
    print("please enter 1 for bike or 2 for car")

print()
print("=============================================")
print("          your custom ride is ready          ")
print ("    enjoy the journey with your new ride!     ")
print("=============================================")