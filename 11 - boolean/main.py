# The following will return False:

def check_truthy(value):
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")

check_truthy(None)       # Falsy
check_truthy(False)      # Falsy
check_truthy(0)          # Falsy
check_truthy("")         # Falsy
check_truthy([])         # Falsy
check_truthy(())         # Falsy
check_truthy({})         # Falsy

check_truthy(1)          # Truthy
check_truthy("Python")   # Truthy
check_truthy([1, 2, 3])  # Truthy
check_truthy({"a": 1})   # Truthy


# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})