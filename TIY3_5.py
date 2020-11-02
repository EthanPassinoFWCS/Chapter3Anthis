guest_list = ["John", "Alex", "Mason", "Jacob", "Isaac", "Mathew"]

for name in guest_list:
  print(f"Would you like to come over for a dinner, {name}? A few others will be there and we are having steak!")
print("Jacob cannot make it.")
guest_list.remove("Jacob")
guest_list.append("James")
for name in guest_list:
  print(f"Would you like to come over for a dinner, {name}? A few others will be there and we are having steak! Jacob sadly could not make it.")

  
