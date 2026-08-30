print("=== smart school day planner ===")
print("answer 3 quick questions and i will plan your day!\n")

day = input("What day is it? (monday,to sunday): ").strip().capitalize()
weather = input("What is the weather like today? sunny, rainy, snowy, cloudy: ").strip().lower()
homework = input("is your homework done? (yes or no): ").strip().lower()

print()
print(f"===your plan for {day}===")
print("-" * 35)
if day in ("saturday", "sunday"):
    print("day type     : weekend - enjoy your free time ")
elif day  == "monday":
    print("day type     : first day of the week - pack your weekly planner ")
elif day == "friday":
    print("day type     : last day of the school -return your library books today . ")
elif day in ("tuesday", "wednesday", "thursday"):
    print("day type     : regular school day .stay focused!")
else:
    print("day type     :day not recognized - please check your spelling .")

if weather == "sunny" and homework == "yes":
    print("after school: head to the park - great weather and homework is done!")

if weather == "rainy " or weather == "cloudy":
    print("weather tip :pack  your umbrella  - it might get wet today .")

if not (homework == "yes"):
    print("homework not done yet finish it before you go out .")
if weather == "rainy" and not homework == "yes":
    print("after school: stay home and finish your homework then watch your favorite show .")
elif weather == "sunny" and  homework == "yes" and not (day in ("saturday", "sunday")):
    print("best plan :all set for a great school day you are prepared !")
elif day in ("saturday", "sunday") and weather == "sunny":
    print("best plan :enjoy your weekend and go outside to play !")
else:
    print("best plan  : take one step at a time you got this !")

print()
print("plan complete")