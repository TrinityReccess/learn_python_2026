# String
# A string is a sequence of characters enclosed in quotes.
# It can be used to represent text, such as names, addresses,
# or any other type of information that can be expressed in words.

first_name = 'Jane'
last_name = "Doe"

single_letter = 'A'


# Integer
# An integer is a whole number without a decimal point. 
# It can be positive, negative, or zero. Integers are commonly used for counting, indexing,
# and performing mathematical operations.

age = 80
number_of_students_in_class = 30
mark = 0
temperature = -15

# float
# A float, short for "floating-point number," is a number that can have a decimal
# point. It is used to represent real numbers, such as measurements, prices, 
# or any value that requires precision.

average_height_of_students = 5.52
average_weight_of_students = 150.75

# Boolean
# A boolean is a data type that can have one of two values: True or False.
# It is often used to represent the truth value of a statement or condition.

is_student = True
is_teacher = False

is_raining = True
has_passbook = False


# None
# None is a special data type in Python that represents the absence of a value or 
# the lack of a specific value. It is often used to indicate that a variable 
# has no value or that a function does not return anything.


username = None
password = None

is_logged_in = None
is_shining = None

number_of_students = None
# print("Before assigning a value to number_of_students:", number_of_students)

# number_of_students =  number_of_students_in_class

# print("After assigning a value to number_of_students:", number_of_students)


# Complex
# A complex number is a number that consists of a real part and an imaginary part.
# It is represented in the form a + bj, where a is the real part and b
# is the imaginary part. Complex numbers are used in various fields, including engineering,
# physics, and mathematics, to represent quantities that have both magnitude and direction.

complex_number1 = 2 + 3j
complex_number2 = 4 - 5j

# Sequence Types
# Sequence types are data types that can hold multiple values(collections) in a specific order.
# They include lists, tuples, and strings.

# Lists
# A list is a mutable sequence type that can hold a collection of items.
# Lists are defined using square brackets [] and can contain elements of different data types.
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5, 5]
ages_of_students = [20, 22, 19, 21]

print(fruits)
print(fruits[0])  # Accessing the first element of the list
print(fruits[1])  # Accessing the second element of the list

print(len(fruits))  # Getting the length of the list
print(fruits[-1])  # Accessing the last element of the list


# tuples
# A tuple is an immutable sequence type that can hold a collection of items.
# Tuples are defined using parentheses () and can contain elements of different data types.
coordinates = (10, 20)
person_info = ("John", 30, "Engineer", 30)


# Strings
# A string is a sequence of characters enclosed in quotes. It can be used to represent text
greeting = "Hello, World!"
name = "Alice"

# set
# A set is an unordered collection of unique elements.
# Sets are defined using curly braces {} and can contain elements of different data types. 
# Sets are commonly used for operations like union, intersection, and difference.
unique_numbers = {1, 2, 3, 4, 5}
unique_fruits = {"apple", "banana", "orange"}

# dictionary
# A dictionary is a collection of key-value pairs. It is defined using curly braces {} and
# each key is separated from its value by a colon (:). Dictionaries are mutable and can contain
# elements of different data types. They are commonly used for storing and retrieving data based on keys.

student = {
    "name": "Alice",
    "age": 20,
    "program": "Data Science",
    "has_registered": True,
    "country": "UGANDA"
    }

employee ={
    "name": "Jane Doe",
    "sex" :"Female",
    "position": "Teacher",
    "salary": 50000,
}


# Operators
# Arithmetic Operators
# +, -, *, /, %, **
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation



# Comparison Operators
# ==, !=, <, >, <=, >=
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a < b)   # Less than
print(a > b)   # Greater than
print(a <= b)  # Less than or equal to
print(a >= b)  # Greater than or equal to

# Logical Operators
# and, or, not
x = True
y = False
print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT




