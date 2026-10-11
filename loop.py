
print("===atm cash dispenser===\n")
total_100=total_50=total_20=total_10=total_5=total_1=0
customers_sesved =0
total_dispensed =0

serving = true
while serving:
    name = input("enter customer name:  ")
    amount =int(input(f"hello {name}! enter withdrawal amount: "))
    if amount <= 0:
        print("invalid amount. pleas enter a positive number.\n")
        continue

    print
