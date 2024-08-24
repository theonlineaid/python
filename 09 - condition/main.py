age =  int(input("Please select your age :"))

if age <= 18:
    print("Access denied")
else:
    print("Access granted")

v = 4
if v > 5:
    print("v is greater than 5")
else:
    print("v is not greater than 5")


x =  8
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but not greater than 10")
else:
    print("x is 5 or less")


try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful:", result)



try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always run, even if an error occurs.")


try:
    result = int(input('Select number : '))
except:
    print("An error occurred")




try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number.")
else:
    print("You entered a valid number!")
finally:
    print("This block always runs.")
