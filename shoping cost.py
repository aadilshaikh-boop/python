print("=== GROCERY COST COMPARISON TOOL ===")

rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4

basket_cost_per_person = (
    (rice_price + milk_price + fruit_price) * number_of_baskets
) / family_members

print("Basket cost per person:", basket_cost_per_person)

total_items = int(input("Enter total items: "))
people = int(input("Enter number of people: "))

if people == 0:
  print("You cannot share between 0 people.")
else:
  remainder = total_items % people
  if remainder == 0:
    print(
        "They divide equally. Each person gets"
        f" {total_items // people} items."
    )
  else:
    print(
        "They do not divide equally. There is a remainder of"
        f" {remainder} items."
    )

recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80

total_cost = recorded_average * total_weeks
total_cost = total_cost - wrong_week_cost + correct_week_cost
corrected_average = total_cost / total_weeks

print("Recorded average:", recorded_average)
print("Total cost after correction:", total_cost)
print("Corrected average:", corrected_average)

store_a_average = 70
store_b_average = 75
store_c_average = 80

verdict = (
    store_a_average < corrected_average
    and store_b_average < corrected_average
    and store_c_average < corrected_average
)

print("\n--- SUMMARY ---")
print("Basket cost per person:", basket_cost_per_person)
print("Corrected average:", corrected_average)
print("Verdict (Are all store averages lower than our corrected average?):", verdict)