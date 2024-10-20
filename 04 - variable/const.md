In Python, there is no built-in constant type like in some other programming languages (e.g., `const` in C++ or `final` in Java). However, you can simulate constants using a few common practices:

1. **Naming Conventions**: By convention, you can use uppercase letters for variable names to indicate that they should be treated as constants. For example:

   ```python
   PI = 3.14159
   MAX_USERS = 100
   ```

2. **Using Classes**: You can create a class that only contains class attributes and prevent instantiation to act as a container for constants:

   ```python
   class Constants:
       PI = 3.14159
       MAX_USERS = 100

   print(Constants.PI)  # Accessing the constant
   ```

3. **Using Enums**: The `enum` module can be used to create enumerations, which can be helpful for defining a set of named constants:

   ```python
   from enum import Enum

   class Status(Enum):
       PENDING = 1
       COMPLETED = 2
       FAILED = 3

   print(Status.PENDING)  # Accessing the constant
   ```

4. **Using a Module**: You can create a separate module (e.g., `constants.py`) and define constants there. You can then import them into your main module:

   ```python
   # constants.py
   PI = 3.14159
   MAX_USERS = 100
   ```

   ```python
   # main.py
   from constants import PI, MAX_USERS

   print(PI)
   ```

While Python does not enforce immutability for these constants, using these practices helps communicate intent and maintain code clarity.