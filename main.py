def process_flow(var):
    def start():
        print("Starting...")

    def middle():
        print("Middle function")

    def end():
        print("End function")

    def defaultFn():
        print("Default function")

   
    functions = {
        1: start,
        2: middle,
        3: end
    }
    
    
    return functions.get(var, defaultFn)

result = process_flow(0)

result()



# class ProcessFlow:
#     def start(self):
#         print("Starting...")

#     def middle(self):
#         print("Middle function")

#     def end(self):
#         print("End function")

#     def defaultFn(self):
#         print("Default function")

#     def run(self, var):
#         methods = {
#             1: self.start,
#             2: self.middle,
#             3: self.end
#         }
#         methods.get(var, self.defaultFn)()

# flow = ProcessFlow()
# flow.run(0)



#  Mapping variable values to functions
# functions = {
#     1: start,
#     2: middle,
#     3: end
# }

# var = 2


# if(var == 1):
#     start()
# elif(var == 2):
#     middle()
# elif(var == 3):
#     end()
# else:
#     defaultFn()


# Call the function based on the value of var, or default to defaultFn
# functions.get(var, defaultFn())