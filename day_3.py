# UNDERSCORES IN PYTHON
universe_age = 14_000_000_000
print(universe_age) # answer: 14000000000
# CONCLUSION: Underscores can be used in numeric literals for better readability.
# They are ignored by the Python interpreter and do not affect the value.

# Multiple Assignments
x, y, z = 0, 18, 7
print(x) # answer: 0
print(y) # answer: 18
print(z) # answer: 7
# CONCLUSION: In Python, you can assign values to multiple variables in a single line.

# Constants in Python
MAX_CONNECTIONS = 100
print(MAX_CONNECTIONS) # answer: 100
# CONSTANTS are typically defined using uppercase letters.
# They are meant to be immutable (unchangeable) throughout the program. 

# TRY IT YOURSELF
print(4 * 2)
print(16 / 2) # NOTE: In Python 3, the division operator (/) always returns a float.
print(5 + 3)
print(10 - 2)
print(2 ** 3)
# ANSWER = 8 [In all cases, the answer is 8]

# COMMENTS
# This is a comment. Comments are ignored by Python.
# You can use comments to explain your code.
print('Hello, World!') # This is a comment at the end of a line of code.
# answer = Hello, World!

# The Zen of Python
import this
# The Zen of Python is a collection of guiding principles for writing programs.
# It was written by Tim Peters and is included as an Easter egg.

print(0.1 + 0.2) # always get a float
print(0.2 * 3)
print(10 ** 6)
print(14 / 7)    # always get a float
# ANSWERS:
# 0.30000000000000004
# 0.6000000000000001
# 1000000
# 2.0

# CHAPTER ENDING PRACTICE CODE
my_first_name = "xyz"
my_last_name = "abcdef"
my_age = 14      # Support the hustle! Starting at 14 is impressive. 🤣🤣😂
i_love = " python programmingN"

# Using title(), f-string, math in brackets, lstrip(), and removesuffix()
print(f'I am {my_first_name.title()} {my_last_name.title()}:\n\tI am only {my_age+1} and I love {i_love.lstrip().removesuffix("N")}.\n\t Please help me grow my love for programming.')

# ANSWER:
# I am Xyz Abcdef:
# 	I am only 15 and I love python programming.
# 	 Please help me grow my love for programming.
