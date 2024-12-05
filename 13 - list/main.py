thislist = ["apple", "banana", "cherry", "apple", "cherry"]

# Initialize an empty list to store unique items
unique_list = []

# Iterate through the original list
for item in thislist:
    # Add the item to the unique list if it isn't already there
    if item not in unique_list:
        unique_list.append(item)

# print(unique_list)
unique_list[0] = "orrange"

print(unique_list[0])
print(unique_list[1])
print(unique_list[2])
unique_list.append("barry")
unique_list.insert(0, "banana")
# // index error
unique_list.remove("banana")
print(len(unique_list)) 


list_methods = dir(list)
print(list_methods)