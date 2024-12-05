import inspect

class Person:
    
    __name = "secret"

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        return f"{self.name}({self.__age})"
    
    def __say_hi(self):
        print("Say Hi") 
    
    def access_s(self):
        self.__say_hi()
        print(self.__class__.__name)  
        

# Create an instance of the class
p1 = Person("John", 36)
p1.access_s()
print(p1)



