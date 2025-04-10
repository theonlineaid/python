# import humanize
# number = 10_000_000

# print(humanize.intcomma(number))  # "10,000,000"

# print(humanize.intword(number))   # "10.0 million"


import cProfile
import time

def example_function():
    # time.sleep(10)


    for i in range(1000000):
        print(i)

# Profile the function execution
cProfile.run('example_function()')


# def example_function():
#     # Some code to be timed
#     time.sleep(60)  # Simulate a delay (2 seconds)

# # Start time
# start_time = time.time()

# # Call the function
# example_function()

# # End time
# end_time = time.time()

# # Calculate execution time
# execution_time = end_time - start_time
# print(f"Execution Time: {execution_time} seconds")