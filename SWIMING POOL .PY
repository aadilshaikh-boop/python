print("=== Swimming Pool Entry Checker ===")
print("Answer 3 questions and I will tell you which pool you can use.\n")

age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes / no): ").lower()
adult_here = input("Is an adult with you? (yes / no): ").lower()

print()
print("=== Entry Decision ===")
print("*" * 32)

if age < 4:
    age_group = "Toddler"
elif age < 12:
    age_group = "Child"
elif age < 18:
    age_group = "Teen"
else:
    age_group = "Adult"

print("Age group:", age_group)

if can_swim != "yes" and can_swim != "no":
    print("Error: Please answer yes or no.")
    swim_known = False
else:
    swim_known = True

if adult_here != "yes" and adult_here != "no":
    print("Error: Please answer yes or no.")
    adult_known = False
else:
    adult_known = True

if swim_known and adult_known:
    deep_pool = can_swim == "yes" and adult_here == "yes"
    shallow_warning = age < 12 or can_swim == "no"
    lifeguard_reminder = not (adult_here == "yes") and adult_known

    print("Deep pool allowed:", deep_pool)

    if shallow_warning:
        print("Warning: Use caution in the shallow end.")

    if lifeguard_reminder:
        print("Reminder: Make sure a lifeguard is present.")

    if age < 4:
        print("Final verdict: Splash pool only, with an adult.")
    elif age < 12:
        if adult_here == "yes":
            print("Final verdict: Main pool with an adult.")
        else:
            print("Final verdict: An adult is required.")
    elif age < 18:
        if can_swim == "yes":
            print("Final verdict: Main pool alone.")
        else:
            print("Final verdict: Main pool only with appropriate supervision.")
    else:
        print("Final verdict: All pools open to you, subject to pool rules.")
else:
    print("Final verdict: Cannot decide. Please enter valid answers.")

print()
print("Have a safe swim!")