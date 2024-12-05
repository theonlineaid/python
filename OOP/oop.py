class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # @staticmethod
    def say_hello(self):
        return "Hi"
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(self.say_hello(), self.name , "your avg numer is", sum/3)

 


s1 =  Student("Doglus", [99, 98, 97])

s1.get_avg()
# Student.say_hello()

