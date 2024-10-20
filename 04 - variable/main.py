# Right naming conventions

_var = "John"          # Leading underscore is acceptable (often indicates a "protected" variable in class contexts)
__var = "John"         # Double leading underscore (used for name mangling in classes)
var_ = "John"          # Trailing underscore is acceptable (often used to avoid conflict with Python keywords)
Var = "John"           # Capitalized first letter (PascalCase, common for class names)
__var__ = "John"       # Double leading and trailing underscores (reserved for system-defined names like __init__)
var123 = "John"        # Including numbers, but not at the beginning
_Var = "John"          # Capitalized with leading underscore (often indicates a "protected" or special-use variable)
VAR123 = "John"        # Uppercase letters with numbers (often used for constants)

# Wrong naming conventions

# var@ = "John"          # Special characters like @ are not allowed
# my#var = "John"        # Special characters like # are not allowed
# !myvar = "John"        # Special characters like ! are not allowed
# my*var = "John"        # Special characters like * are not allowed
# my%var = "John"        # Special characters like % are not allowed
# my+var = "John"        # Special characters like + are not allowed
# my.var = "John"        # Dot notation is not allowed for variable names (reserved for attribute access)
# None = "John"          # Using Python keywords as variable names is not allowed
# True = "John"          # Using Python keywords as variable names is not allowed
# class = "John"         # Using Python keywords as variable names is not allowed
# return = "John"        # Using Python keywords as variable names is not allowed
# my var = "John"        # Spaces are not allowed in variable names
# 123var = "John"        # Variable names cannot start with numbers
