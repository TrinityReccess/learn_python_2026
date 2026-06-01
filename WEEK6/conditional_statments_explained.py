# ============================================================
# CONDITIONAL STATEMENTS IN PYTHON
# ============================================================
# Conditional statements allow your program to make decisions
# and execute different blocks of code based on conditions.
# ============================================================


# ------------------------------------------------------------
# 1. if STATEMENT
# ------------------------------------------------------------
# Runs a block of code ONLY if the condition is True.

age = 20

if age >= 18:
    print("You are an adult.")  # This will print

# ------------------------------------------------------------
# 2. if...else STATEMENT
# ------------------------------------------------------------
# Runs one block if True, another block if False.

temperature = 15

if temperature > 25:
    print("It's hot outside.")
else:
    print("It's not that hot outside.")  # This will print


# ------------------------------------------------------------
# 3. if...elif...else STATEMENT
# ------------------------------------------------------------
# Checks multiple conditions one by one.
# elif = "else if" — only checked if previous conditions are False.

score = 72

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")  # This will print
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# ------------------------------------------------------------
# 4. NESTED if STATEMENTS
# ------------------------------------------------------------
# An if statement inside another if statement.

is_logged_in = True
is_admin = False

if is_logged_in:
    print("Welcome back!")
    if is_admin:
        print("You have admin access.")
    else:
        print("You have standard access.")  # This will print
else:
    print("Please log in first.")


# ------------------------------------------------------------
# 5. COMPARISON OPERATORS (used in conditions)
# ------------------------------------------------------------
# ==   equal to
# !=   not equal to
# >    greater than
# <    less than
# >=   greater than or equal to
# <=   less than or equal to

x = 10
print(x == 10)   # True
print(x != 5)    # True
print(x > 3)     # True
print(x < 3)     # False
print(x >= 10)   # True
print(x <= 9)    # False


# ------------------------------------------------------------
# 6. LOGICAL OPERATORS (combine multiple conditions)
# ------------------------------------------------------------
# and  → True only if BOTH conditions are True
# or   → True if AT LEAST ONE condition is True
# not  → Reverses the result (True becomes False, False becomes True)

has_ticket = True
has_id = True

# and
if has_ticket and has_id:
    print("Entry granted.")  # This will print

# or
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")  # This will print

# not
is_raining = False

if not is_raining:
    print("Let's go for a walk!")  # This will print


# ------------------------------------------------------------
# 7. SHORTHAND if (Ternary / One-liner)
# ------------------------------------------------------------
# A concise way to write a simple if...else on one line.
# Syntax: value_if_true  if  condition  else  value_if_false

num = 7
result = "Odd" if num % 2 != 0 else "Even"
print(result)  # Odd


# ------------------------------------------------------------
# 8. TRUTHY and FALSY VALUES
# ------------------------------------------------------------
# Python treats certain values as False even without == False:
#   Falsy: 0, 0.0, "", [], {}, None, False
#   Truthy: anything else

name = ""

if name:
    print("Hello,", name)
else:
    print("No name provided.")  # This will print (empty string is Falsy)

items = [1, 2, 3]

if items:
    print("List has items.")  # This will print (non-empty list is Truthy)


# ------------------------------------------------------------
# 9. CHECKING MEMBERSHIP with 'in'
# ------------------------------------------------------------
# Use 'in' to check if a value exists in a list, string, etc.

fruits = ["apple", "banana", "mango"]

if "banana" in fruits:
    print("Banana is available.")  # This will print

if "grape" not in fruits:
    print("Grape is not in the list.")  # This will print


# ------------------------------------------------------------
# 10. MATCH STATEMENT (Python 3.10+)
# ------------------------------------------------------------
# Similar to switch/case in other languages.

day = "Monday"

match day:
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case "Monday":
        print("Start of the work week.")  # This will print
    case _:
        print("It's a weekday.")  # _ is the default case




day = input("Enter a day of the week: ").lower()