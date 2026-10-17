member_name = input("Enter member name: ")
club_name = input("Enter club name: ")

member_number = 8
points = 9.5
is_active = True

print("Member number:", member_number, type(member_number))
print("Points:", points, type(points))
print("Active:", is_active, type(is_active))

badge_code = member_name[:3] + club_name[-1] + str(member_number)
print("Badge code:", badge_code)

print("===== CLUB BADGE =====")
print("Member: " + member_name)
print("Club: " + club_name)
print("Code: " + badge_code)
print("Points: " + str(points) + " | Active: " + str(is_active))
