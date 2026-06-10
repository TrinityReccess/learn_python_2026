# 🐍 Learn Python 2026

A beginner Python learning journal — building up from the basics week by week.

---

## 📅 Weekly Progress

| Week | Topics Covered |
|------|----------------|
| [Week 4](#week-4) | First Programs, Naming Conventions, Data Types |
| [Week 5](#week-5) | User Input, Arithmetic Operators, Comparison & Logical Operators |
| [Week 6](#week-6) | Conditional Statements (`if`, `elif`, `else`, nested, `match`) |
| [Week 7](#week-7) | Functions (defining, calling, parameters) |
| [Week 8](#week-8) | Loops (`for`, `while`, `break`, `continue`, nested loops) |

---

## WEEK 4

### 📁 Files
| File | Description |
|------|-------------|
| `first_program.py` | First print statements, variables, naming conventions |
| `data_types.py` | All Python data types with examples |
| `coffee.py` | Practice script |
| `first_guy.py` | Practice script |

---

### ✏️ First Program
Your very first Python program — printing to the screen and using variables.
```python
print("Well in!")

value1 = 70
value2 = 10
sum = value1 + value2
print(sum)  # 80
```

**Naming Conventions:**
| Style | Example | Used For |
|-------|---------|----------|
| `snake_case` | `first_name` | Variables & functions |
| `camelCase` | `firstName` | Less common in Python |
| `MACRO_CASE` | `MAX_SIZE` | Constants |
| `CapsCase` | `MyClass` | Classes |

---

### 🗂️ Data Types

#### String
Text enclosed in quotes.
```python
first_name = 'Jane'
last_name = "Doe"
```

#### Integer
Whole numbers (no decimal point).
```python
age = 80
temperature = -15
```

#### Float
Numbers with a decimal point.
```python
average_height = 5.52
average_weight = 150.75
```

#### Boolean
Only two values: `True` or `False`.
```python
is_student = True
is_teacher = False
```

#### None
Represents the absence of a value.
```python
username = None
password = None
```

#### Complex
Numbers with a real and imaginary part.
```python
complex_number = 2 + 3j
```

#### List
An ordered, **mutable** collection of items.
```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])   # apple
print(len(fruits)) # 3
print(fruits[-1])  # orange (last item)
```

#### Tuple
An ordered, **immutable** collection.
```python
coordinates = (10, 20)
person_info = ("John", 30, "Engineer")
```

#### Set
An **unordered** collection of **unique** elements.
```python
unique_numbers = {1, 2, 3, 4, 5}
```

#### Dictionary
A collection of **key-value pairs**.
```python
student = {
    "name": "Alice",
    "age": 20,
    "program": "Data Science",
    "has_registered": True
}
```

---

## WEEK 5

### 📁 Files
| File | Description |
|------|-------------|
| `input.py` | Getting user input and using `f-strings` |
| `operators.py` | Arithmetic, comparison, and logical operators |
| `conditions.py` | First look at `if`, `elif`, `else` |

---

### ⌨️ User Input
Getting input from the user and using it in your program.
```python
first_name = input("Please enter your first name: ")
print(f"Hello, {first_name}! 👋")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
print(f"The sum of {number1} and {number2} is {number1 + number2}")
```

---

### ➕ Operators

#### Arithmetic Operators
| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 20` | `30` |
| `-` | Subtraction | `10 - 20` | `-10` |
| `*` | Multiplication | `10 * 20` | `200` |
| `/` | Division | `10 / 20` | `0.5` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

#### Comparison Operators
Return `True` or `False`.
```python
print(10 == 20)  # False
print(10 != 20)  # True
print(10 > 20)   # False
print(10 < 20)   # True
print(10 >= 10)  # True
print(10 <= 9)   # False
```

#### Logical Operators
```python
x = True
y = False
print(x and y)  # False — both must be True
print(x or y)   # True  — at least one is True
print(not x)    # False — reverses the value
```

#### Assignment Operators
```python
counter = 0
counter += 1   # counter = 1
counter *= 2   # counter = 2
counter -= 3   # counter = -1
```

#### Membership Operators
```python
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)      # True
print("grape" not in fruits)  # True
```

---

## WEEK 6

### 📁 Files
| File | Description |
|------|-------------|
| `conditional_statments_explained.py` | Full notes and examples on all conditional statement types |
| `nested_if.py` | Focused examples on nested `if` statements |

---

### 🔀 Conditional Statements

#### `if` Statement
Runs code only when a condition is `True`.
```python
age = 20
if age >= 18:
    print("You are an adult.")
```

#### `if...else` Statement
Runs one block if `True`, another if `False`.
```python
if temperature > 25:
    print("It's hot.")
else:
    print("It's not that hot.")
```

#### `if...elif...else` Statement
Checks multiple conditions in order.
```python
mark = float(input("What did you get in Maths? "))

if mark >= 80:
    print("A")
elif mark >= 75:
    print("B")
elif mark >= 65:
    print("C")
elif mark >= 60:
    print("D")
elif mark >= 50:
    print("E")
else:
    print("F")
```

#### Nested `if` Statements
An `if` inside another `if`.
```python
if is_logged_in:
    if is_admin:
        print("Admin access.")
    else:
        print("Standard access.")
else:
    print("Please log in.")
```

#### Shorthand `if` (Ternary)
One-line `if...else`.
```python
result = "Odd" if num % 2 != 0 else "Even"
```

#### Truthy & Falsy Values
| Falsy | Truthy |
|-------|--------|
| `0`, `0.0` | Any non-zero number |
| `""` | Any non-empty string |
| `[]`, `{}`, `()` | Any non-empty collection |
| `None`, `False` | `True` |

```python
name = ""
if name:
    print("Hello,", name)
else:
    print("No name provided.")  # This runs
```

#### `match` Statement *(Python 3.10+)*
Like switch/case in other languages.
```python
match day:
    case "Saturday" | "Sunday":
        print("Weekend!")
    case "Monday":
        print("Start of the work week.")
    case _:
        print("It's a weekday.")
```

---

## ▶️ How to Run Any File

```bash
python WEEK4/first_program.py
python WEEK5/operators.py
python WEEK6/conditional_statments_explained.py
python WEEK7/functions.py
python WEEK8/loops.py
```

---

## WEEK 7

### 📁 Files
| File | Description |
|------|-------------|
| `functions.py` | Defining and calling functions with parameters |

---

### 🔧 Functions
A function is a reusable block of code that only runs when it is called.
You define it once and can call it as many times as you need.

#### Defining and Calling a Function
```python
def greet_user(username):
    print(f"Hello, {username} ☺️")

greet_user("Kenneth")
greet_user("Alice")
```

#### Function with Multiple Parameters
```python
def sum_of_numbers(a, b):
    print(a + b)

sum_of_numbers(2, 6)    # 8
sum_of_numbers(20, 69)  # 89
```

**Key Rules:**
- Use the `def` keyword to define a function
- Give it a descriptive name in `snake_case`
- Parameters go inside the brackets `()`
- The body must be indented

---

## WEEK 8

### 📁 Files
| File | Description |
|------|-------------|
| `loops.py` | Full notes, real-world scenarios, WHY explanations, and a USSD mobile money menu project |

---

### 🔁 Loops

> **Why loops?** Instead of writing the same code 100 times (e.g. printing every student's name), you write the logic **once** and Python repeats it automatically. Loops are used everywhere in real software — sending emails, calculating bills, processing database rows, displaying social media feeds, and more.

---

#### `for` Loop
Goes through each item in a sequence (list, string, range) one by one.

```python
students = ["Alice", "Bob", "Charlie", "Diana"]

for student in students:
    print(f"Good morning, {student}!")
```

🌍 **Real world:** A teacher greeting every student. A system sending a notification to every user. Processing every row in a spreadsheet.

---

#### `for` Loop with `range()`
Use `range()` when you want to repeat something a set number of times or need position numbers.

```python
# range(stop)            → 0 up to (not including) stop
# range(start, stop)     → start up to (not including) stop
# range(start, stop, step) → with a custom step

for i in range(1, 6):      # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 11, 2):  # 0, 2, 4, 6, 8, 10
    print(i)
```

🌍 **Real world:** Generating student ID numbers, printing a times table, looping through pages of results.

---

#### `for` Loop over a String
Strings are sequences of characters, so you can loop letter by letter.

```python
name = "Uganda"
for letter in name:
    print(letter)   # U, g, a, n, d, a
```

🌍 **Real world:** Counting vowels in a name, checking if a password has numbers, validating characters in user input.

---

#### `while` Loop
Keeps running **as long as a condition is True**. Best when you don't know in advance how many times to repeat.

```python
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1   # ⚠️ Always update — or the loop runs forever!
```

🌍 **Real world:** An ATM allowing 3 PIN attempts, a menu that runs until the user chooses to quit, waiting for a sensor reading to reach a target value.

> ⚠️ **Infinite Loop Warning:** If the condition never becomes `False`, the program gets stuck running forever. Always make sure something inside the loop changes the condition.

---

#### `break` — Exit the Loop Early
Stops the loop immediately. Use it when you've found what you need and there's no point continuing.

```python
seats = ["taken", "taken", "available", "available"]

for i, status in enumerate(seats, start=1):
    if status == "available":
        print(f"✅ Seat {i} booked!")
        break
```

🌍 **Real world:** Finding the first available seat in a cinema, finding a product in stock, stopping a search once a match is found.

---

#### `continue` — Skip an Iteration
Skips the current turn and moves to the next one. The loop keeps going — only one iteration is skipped.

```python
users = [
    {"name": "Alice", "suspended": False},
    {"name": "Bob",   "suspended": True},
    {"name": "Carol", "suspended": False},
]

for user in users:
    if user["suspended"]:
        continue   # skip suspended users
    print(f"📧 Email sent to {user['name']}")
```

🌍 **Real world:** Skipping suspended accounts when sending newsletters, skipping blank form entries, skipping items that are out of stock.

---

#### Nested Loops
A loop inside another loop. The **inner loop** runs completely for **each single step** of the outer loop.

```python
# School timetable — for each class, print all subjects
classes = ["S1", "S2", "S3"]
subjects = ["Maths", "English", "Science"]

for cls in classes:
    print(f"Class {cls}:")
    for subject in subjects:
        print(f"   → {subject}")
```

🌍 **Real world:** Building a timetable, labelling cinema seats (row + seat number), generating a multiplication table.

---

#### Looping Over a Dictionary
Read all the information stored in a dictionary using `.keys()`, `.values()`, or `.items()`.

```python
order = {"Rice": 15000, "Sugar": 7000, "Milk": 4500}

total = 0
for item, price in order.items():
    print(f"{item}: UGX {price:,}")
    total += price

print(f"Total: UGX {total:,}")
```

🌍 **Real world:** Printing a shop receipt, displaying a student profile, showing a user's account details.

---

#### `else` with a Loop
The `else` block runs **only if the loop completed without hitting a `break`**. Useful for searches — if nothing is found, the `else` tells you.

```python
registered = ["Alice", "Bob", "Charlie"]
search = "Kenneth"

for name in registered:
    if name == search:
        print(f"✅ {search} is registered.")
        break
else:
    print(f"❌ {search} is NOT in the register.")
```

---

#### Quick Reference — When to Use Which Loop

| Situation | Use |
|-----------|-----|
| Going through a list, string or dictionary | `for` loop |
| Repeating a set number of times | `for` with `range()` |
| Don't know how many times to repeat | `while` loop |
| Stop as soon as you find something | `break` |
| Skip certain items, keep looping | `continue` |
| Loop inside a loop (rows & columns, class & subjects) | Nested loops |

---

*Learning Python one week at a time 🚀*
