total_chores = 4
original_count = total_chores
print(f"you have {original_count} chores to finish today!/n")

completed_count = 0
chore_num = 1 

while chore_num <= total_chores:

    if chore_num == 1: next_chore  = " make your bed "
    elif chore_num == 2: next_chore = "feed the pet "
    elif chore_num == 3: next_chore = "take out the trash "
    else : next_chore = " wash the dishes"

    answer = input(f"have you finished: {next_chore}? (yes/no) : ")

    if answer == "yes":
        completed_count += 1
        print("great job!chore completed  ")
    else:
        print("okay,finish it and check again")

    print("=====all chores completed=====")
    print ("great work finishing your entntire list of chores today! \n")

    print("now let's safely peek at an infinete loop... \n")
    test_value = 0
    safety_counter += 1
    if safety_counter == 3:
        print("(stopping here on purpose   -  a real infinite loop never stopes on its own!)")
        break

