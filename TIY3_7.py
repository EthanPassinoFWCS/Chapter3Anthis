guest_list = ["John", "Alex", "Mason", "Jacob", "Isaac", "Mathew"]

print("I can only have two people over for dinner now.")

name1 = guest_list.pop(0)
name2 = guest_list.pop(0)
name3 = guest_list.pop(0)
name4 = guest_list.pop(0)
print(f"Sorry, {name1}. I can only have two people over for dinner no so you can no longer come. Sorry!")
print(f"Sorry, {name2}. I can only have two people over for dinner no so you can no longer come. Sorry!")
print(f"Sorry, {name3}. I can only have two people over for dinner no so you can no longer come. Sorry!")
print(f"Sorry, {name4}. I can only have two people over for dinner no so you can no longer come. Sorry!")


for name in guest_list:
    print(f"You are still invited to the party, {name}! Can't wait to see you there!")

del guest_list[0]
del guest_list[0]

print(guest_list)