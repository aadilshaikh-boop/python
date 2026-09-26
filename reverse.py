string = input("please enter your own string: ")

string2 =('')

for i in string:
    string2 = i + string2

    print("\nthe original string is: ",string)
    print("\nthe reverse string is: ",string2)