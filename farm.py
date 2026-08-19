field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110



total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total of all fields:", total, "kg")
print("Average per field:", average, "kg")

price_per_kg = 15
earning = total * price_per_kg
print("total earning :rs", earning)

bags = total //25
leftover = total % 25

print("full bags packed:", bags)
print("leftover kg:", leftover, "kg")


last_year = 500
print("better than last year:", total > last_year)
print("same as last year:", total == last_year)
print("at least good :", total >= last_year)
total += 30 
print("after bonus crop total:", total, "kg")

total -= 15 
print("after seed reserve:", total, "kg")

bags = total // 25
print("final bags packed   :", bags)