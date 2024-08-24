# all_errors.py

# 1. SyntaxError
def syntax_error():
    if True
        print("This will cause a SyntaxError because of the missing colon")


# 2. IndentationError
def indentation_error():
    print("This line is indented correctly")
print("This line will cause an IndentationError because it is not indented")


# 3. TypeError
def type_error():
    result = 'Hello' + 5  # This will cause a TypeError because you can't add a string and an integer


# 4. NameError
def name_error():
    print(undeclared_variable)  # This will cause a NameError because the variable is not defined


# 5. IndexError
def index_error():
    my_list = [1, 2, 3]
    print(my_list[5])  # This will cause an IndexError because index 5 is out of range


# 6. KeyError
def key_error():
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])  # This will cause a KeyError because 'c' is not a valid key in the dictionary


# 7. AttributeError
def attribute_error():
    my_string = "Hello"
    my_string.append(' World')  # This will cause an AttributeError because strings don't have an append method


# 8. ZeroDivisionError
def zero_division_error():
    result = 10 / 0  # This will cause a ZeroDivisionError because division by zero is not allowed


# 9. FileNotFoundError
def file_not_found_error():
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()  # This will cause a FileNotFoundError because the file doesn't exist


# 10. ValueError
def value_error():
    result = int('abc')  # This will cause a ValueError because 'abc' cannot be converted to an integer


# 11. ImportError
def import_error():
    import non_existent_module  # This will cause an ImportError because the module does not exist


# 12. OverflowError
def overflow_error():
    import math
    result = math.exp(1000)  # This will likely cause an OverflowError due to the large exponential result


# 13. RuntimeError
def runtime_error():
    raise RuntimeError("This is a manually raised runtime error")


# 14. MemoryError
def memory_error():
    # Try to create a list with a huge number of elements to cause a MemoryError
    huge_list = [1] * (10**10)


# 15. AssertionError
def assertion_error():
    assert 1 == 2, "This will cause an AssertionError because the assertion is false"


# 16. FloatingPointError
def floating_point_error():
    import sys
    sys.float_info.epsilon = 0.0  # This will likely cause a FloatingPointError


# 17. EOFError
def eof_error():
    input("Enter something (or just trigger an EOF): ")  # Press Ctrl+D (or Ctrl+Z on Windows) to trigger an EOFError


# 18. UnicodeError
def unicode_error():
    byte_string = b'\x80\x81\x82'
    text = byte_string.decode('utf-8')  # This will cause a UnicodeDecodeError


# 19. NotImplementedError
def not_implemented_error():
    raise NotImplementedError("This function is not implemented yet")


# 20. OSError
def os_error():
    open('/root/secret_file.txt', 'r')  # This will likely cause an OSError due to permission issues


# 21. RecursionError
def recursion_error():
    def infinite_recursion():
        return infinite_recursion()
    infinite_recursion()  # This will cause a RecursionError


# 22. StopIteration
def stop_iteration_error():
    iterator = iter([1, 2, 3])
    next(iterator)
    next(iterator)
    next(iterator)
    next(iterator)  # This will cause a StopIteration error


# Uncomment the functions below one by one to see the corresponding errors.

# syntax_error()
# indentation_error()
# type_error()
# name_error()
# index_error()
# key_error()
# attribute_error()
# zero_division_error()
# file_not_found_error()
# value_error()
# import_error()
# overflow_error()
# runtime_error()
# memory_error()
# assertion_error()
# floating_point_error()
# eof_error()
# unicode_error()
# not_implemented_error()
# os_error()
# recursion_error()
# stop_iteration_error()
