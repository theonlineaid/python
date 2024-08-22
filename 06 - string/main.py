# Define a variable 

lol = "Hello python world!"


# Print the variable

print(lol[0])
print(lol[-1])
print(lol[len(lol) - 1])
print(len(lol))


# Search for a variable check is it existed
txt = "The best things in life are free!"
user_input = input("search : ")
print(user_input in txt)


# With logic
if user_input in txt:
  print(f"Yes, {user_input} is present.")
else :
  print(f"No, {user_input} is not present.")


# You can slice  string 
print(lol[2:5])
print(lol[:5])
print(lol[2:])
print(lol.upper())
print(lol.lower())
print(lol)

# The strip() method removes any whitespace from the beginning or the end:
print(lol.strip())
print(lol.split(" "))


# Get all string methods
string_methods = dir(str)

# Print string methods
print("String methods in Python:")
for method in string_methods:
    if not method.startswith('__'):
        print(method)