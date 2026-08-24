temperature = int(input("Enter today's temperature in Celsius: "))

if temperature < 20:
    outfit = "a jacket"
    print("it is cold today", )
    print("you should wear", outfit)
else:
    outfit = "a t-shirt"
    print("it is warm today")
    print(" wear a ", outfit)

is_raining = input("Is it raining today? (yes/no): ")

if is_raining == "yes":
    print("bring an umbrella!")
    wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed > 30:
    needs_windbreaker = "yes"
    print("it is windy today")
    print("you should wear a windbreaker:")
else:
    needs_windbreaker = "no"
    print("it is calm today")
    print("no windbreaker needed over your ", outfit)

has_puddles = input("Are there puddles on the ground? (yes/no): ")

if has_puddles == "yes":
    shoes = "boots"
    print("the ground is wet")
    print("wear",shoes)
else:
    shoes = "sneakers"
    print("the ground is dry")
    print("wear", shoes)

print("")
print("weather check complete")

print("=====weather outfit complete=====")
print("temperature :", temperature)
print("outfit chosen:", outfit)
print("raining:", is_raining)
print("wind speed:", wind_speed)
print("needs windbreaker:", needs_windbreaker)
print("shoes chosen:", shoes)
print("==================================")