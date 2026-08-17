from turtle import speed


name = input("enter your real name ,agent : ")
gadget = input("enter your favorite gadget : ")

agent_number = 8
speed_rate=9.5
misson_count =13
height_m = 1.67
is_active = True

print ("name:", name, " type:", type(name))
print ("gadget :", gadget, " type:", type(gadget))
print ("agent number:", agent_number, " type :", type(agent_number))
print ("speed rate:", speed_rate, "type:", type (speed_rate))
print ("mission count:", misson_count, "type:", type(misson_count))
print ("height in meters:", height_m, "type:", type(height_m))
print ("is active:", is_active, "type:", type(is_active))


agent_number_text = str(agent_number)
mission_count_text = str(misson_count)
speed_rate_text = str(speed_rate)
status_text = str(is_active)

print("agent number:", agent_number_text, " type:", type(agent_number_text))
print("mission count:", mission_count_text, " type:", type(mission_count_text))
print("speed rate:", speed_rate_text, " type:", type(speed_rate_text))
print("status:", status_text, " type:", type(status_text))


first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("first three letters of your name:", first_three)
print("last letter of your name:", last_letter)
print("secret code name:", code_name)


reversed_gadget = gadget[::-1]
print("reversed gadget name:", reversed_gadget)


badge_line_1 = "Agent " + code_name.upper()
badge_line_2 = "id: " + agent_number_text + " missions: " + mission_count_text
badge_line_3 = "speed: " + speed_rate_text + " active: " + status_text
badge_line_4 = "secret gadget code: " + reversed_gadget.upper()


print("")
print("===== secret agent badge =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("===================================")