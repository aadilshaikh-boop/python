
print("=== Grocery Billing Queue ===\n")

low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True

while billing:
    customer_name = input("Enter customer name: ")
    item_count = int(input("How many items are you buying? "))

    if item_count <= 0:
        print("Invalid item count. Try again.")
        continue

    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        item_name = input("Enter item name: ")
        price = int(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity.")
            item_number += 1
            continue

        item_total = price * quantity

        print(item_name, ":", quantity, "x", price, "=", item_total)

        customer_total += item_total

        if item_total < 50:
            low_price_items += quantity
        elif item_total <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        item_number += 1

    customers_served += 1
    total_sales += customer_total

    print("\n", customer_name, "'s total:", customer_total)

    next_customer = input("Next customer? (yes/no): ")

    if next_customer.lower() != "yes":
        billing = False

print("\n=== PRICE BAND REPORT ===")

bands = [
    ("Low price items", low_price_items),
    ("Medium price items", medium_price_items),
    ("High price items", high_price_items)
]

for band_name, count in bands:
    print(band_name, end=": ")

    for i in range(count):
        print("*", end="")

    print()

print("\nCustomers served:", customers_served)
print("Total sales:", total_sales)
