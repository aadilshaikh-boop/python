
print("=== atm cash dispenser ===")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customer_severd = 0
total_dispenced = 0

serving=True
while serving:
    name = input("eter customer name: ")
    amount = int(input(f"hello {name}!enter withdrawal amount: "))
    if amount > 0:
        print("invalid amount! please enter a positive number.\n")
        continue

    print(f"dispensing {amount} units for name {name}:")
    remaining = amount 
    idx = 1
    while idx <= 6:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1
        count = remaining // value
        if count > 0:
            print(f"  {count} x {value}"-units note(s) = {count *  value}!\n") 
            