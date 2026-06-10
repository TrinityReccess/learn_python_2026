# ================================================================
# WEEK 8 — LOOPS IN PYTHON
# ================================================================
#
# WHY DO WE NEED LOOPS?
# ---------------------------------------------------------------
# Imagine you are a teacher and you want to print the name of
# every student in your class of 100 students.
#
# Without a loop, you would have to write:
#   print("Alice")
#   print("Bob")
#   print("Charlie")
#   ... (97 more lines!)
#
# That is repetitive, time-consuming, and hard to maintain.
# If a student joins or leaves, you have to rewrite everything.
#
# With a loop, you write the logic ONCE and Python repeats it
# for every student automatically.
#
# Loops are used EVERYWHERE in real software:
#   ✅ Sending emails to all users on a platform
#   ✅ Calculating the total bill for items in a shopping cart
#   ✅ Checking every photo uploaded for inappropriate content
#   ✅ Displaying all posts in a social media feed
#   ✅ Processing every row in a spreadsheet or database
#
# Python has TWO main types of loops:
#   1. for loop  — when you know what to loop over (a list, range, etc.)
#   2. while loop — when you loop until a condition becomes False
#
# ================================================================


# ----------------------------------------------------------------
# 1. THE for LOOP
# ----------------------------------------------------------------
# The for loop goes through each item in a sequence one by one.
# A "sequence" can be a list, a string, a range of numbers, etc.
#
# SYNTAX:
#   for variable in sequence:
#       # code to run for each item
#
# The variable (e.g. "fruit") takes the value of each item
# in the sequence one at a time. You can name it anything,
# but give it a meaningful name so your code is easy to read.
# ----------------------------------------------------------------

# SIMPLE EXAMPLE — Loop over a list of fruits
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# mango
# orange

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 1: Printing a class register
# ---------------------------------------------------------------
# A teacher wants to greet every student by name at the
# start of class. Instead of writing a print statement for
# each student, we loop through the list.

students = ["Alice", "Bob", "Charlie", "Diana", "Emmanuel"]

print("\n--- Class Register ---")
for student in students:
    print(f"Good morning, {student}! Please take your seat.")

# Output:
# Good morning, Alice! Please take your seat.
# Good morning, Bob! Please take your seat.
# ... and so on for every student

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 2: Calculating a shopping bill
# ---------------------------------------------------------------
# A cashier has a list of item prices and needs to calculate
# the total cost of a customer's shopping.

item_prices = [5000, 12000, 3500, 8000, 1500]
total_bill = 0

for price in item_prices:
    total_bill += price  # add each price to the running total

print(f"\nYour total bill is: UGX {total_bill:,}")
# Output: Your total bill is: UGX 30,000


# ----------------------------------------------------------------
# 2. THE for LOOP WITH range()
# ----------------------------------------------------------------
# range() generates a sequence of numbers for you to loop over.
# It is useful when you want to repeat something a set number
# of times, or when you need the index (position) of each item.
#
# FORMS OF range():
#   range(stop)               → from 0 up to (not including) stop
#   range(start, stop)        → from start up to (not including) stop
#   range(start, stop, step)  → with a custom step/jump
#
# NOTE: range() does NOT include the last number.
#   range(5) gives: 0, 1, 2, 3, 4  — NOT 5
#   range(1, 6) gives: 1, 2, 3, 4, 5  — NOT 6
# ----------------------------------------------------------------

print("\n--- range(5): 0 to 4 ---")
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

print("\n--- range(1, 6): 1 to 5 ---")
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

print("\n--- range(0, 11, 2): even numbers ---")
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10

print("\n--- range(5, 0, -1): counting down ---")
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 3: Generating student ID numbers
# ---------------------------------------------------------------
# A school wants to assign ID numbers to 5 new students
# starting from ID 1001.

print("\n--- New Student IDs ---")
for student_id in range(1001, 1006):
    print(f"Assigned Student ID: {student_id}")

# Output:
# Assigned Student ID: 1001
# Assigned Student ID: 1002
# ...up to 1005

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 4: Times tables
# ---------------------------------------------------------------
# A student wants to print the 3 times table.

number = 3
print(f"\n--- {number} Times Table ---")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# ----------------------------------------------------------------
# 3. THE for LOOP OVER A STRING
# ----------------------------------------------------------------
# A string is just a sequence of characters, so Python can loop
# over it letter by letter. This is useful for checking
# individual characters in a word or sentence.
# ----------------------------------------------------------------

word = "Uganda"

print("\n--- Letters in 'Uganda' ---")
for letter in word:
    print(letter)

# Output: U, g, a, n, d, a (each on its own line)

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 5: Counting vowels in a word
# ---------------------------------------------------------------
# An app wants to count how many vowels are in a given name.

name = "Emmanuel"
vowels = "aeiouAEIOU"
vowel_count = 0

for letter in name:
    if letter in vowels:
        vowel_count += 1

print(f"\nThe name '{name}' has {vowel_count} vowel(s).")
# Output: The name 'Emmanuel' has 4 vowel(s).


# ----------------------------------------------------------------
# 4. THE while LOOP
# ----------------------------------------------------------------
# The while loop keeps running a block of code AS LONG AS
# a condition is True. It is best used when you do NOT know
# in advance how many times you will need to loop.
#
# SYNTAX:
#   while condition:
#       # code to run
#       # update something so the condition eventually becomes False
#
# ⚠️ VERY IMPORTANT WARNING — INFINITE LOOPS:
#   If you forget to update the variable inside the loop,
#   the condition will NEVER become False and your program
#   will get stuck running forever. Always make sure the
#   condition can eventually become False!
# ----------------------------------------------------------------

# SIMPLE EXAMPLE
count = 1

while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Without this line, the loop would never stop!

# Output:
# Count is: 1
# Count is: 2
# Count is: 3
# Count is: 4
# Count is: 5

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 6: ATM PIN attempts
# ---------------------------------------------------------------
# An ATM allows a user 3 attempts to enter the correct PIN.
# After 3 wrong tries, the card is blocked. We don't know
# in advance how many attempts the user will take, so a
# while loop is perfect here.

correct_pin = "1234"
attempts = 0
max_attempts = 3

print("\n--- ATM Login ---")
while attempts < max_attempts:
    entered_pin = input("Enter your PIN: ")
    attempts += 1

    if entered_pin == correct_pin:
        print("✅ Access granted. Welcome!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ Wrong PIN. You have {remaining} attempt(s) left.")
        else:
            print("🚫 Card blocked. Too many wrong attempts.")

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 7: A simple shop menu
# ---------------------------------------------------------------
# A shop system keeps showing a menu until the user chooses
# to exit. We loop until they say "quit".

print("\n--- Shop Menu (type 'quit' to exit) ---")
while True:  # This loop runs forever UNTIL we hit a break
    choice = input("Enter item to buy (or 'quit' to exit): ")
    if choice == "quit":
        print("Thank you for shopping with us! Goodbye 👋")
        break
    else:
        print(f"✅ Added '{choice}' to your cart.")


# ----------------------------------------------------------------
# 5. THE break STATEMENT
# ----------------------------------------------------------------
# break immediately EXITS the loop, even if there are still
# items left to go through or the while condition is still True.
#
# Think of it as an emergency exit door — you use it when
# you have found what you need and there is no point continuing.
# ----------------------------------------------------------------

# SIMPLE EXAMPLE
print("\n--- Searching for number 5 ---")
for number in range(1, 11):
    if number == 5:
        print(f"Found it! Stopping at {number}.")
        break
    print(number)

# Output: 1, 2, 3, 4, Found it! Stopping at 5.
# Numbers 6-10 are never printed because we broke out at 5.

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 8: Searching for an available seat
# ---------------------------------------------------------------
# A cinema system checks seats one by one and stops as soon
# as it finds the first available seat. No need to check
# the rest once we've found one.

seats = ["taken", "taken", "taken", "available", "available", "taken"]

print("\n--- Finding First Available Seat ---")
for seat_number, status in enumerate(seats, start=1):
    if status == "available":
        print(f"✅ Seat {seat_number} is available. Booking it now!")
        break
    else:
        print(f"Seat {seat_number} is taken.")

# Output:
# Seat 1 is taken.
# Seat 2 is taken.
# Seat 3 is taken.
# ✅ Seat 4 is available. Booking it now!


# ----------------------------------------------------------------
# 6. THE continue STATEMENT
# ----------------------------------------------------------------
# continue SKIPS the rest of the code for the current iteration
# and jumps straight to the next one.
#
# Unlike break (which exits the whole loop), continue just
# skips one turn and keeps the loop going.
# ----------------------------------------------------------------

# SIMPLE EXAMPLE — skip the number 4
print("\n--- Skipping number 4 ---")
for number in range(1, 8):
    if number == 4:
        continue  # skip this iteration
    print(number)

# Output: 1, 2, 3, 5, 6, 7  (4 is skipped)

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 9: Skipping suspended accounts
# ---------------------------------------------------------------
# A system is sending a newsletter to all users, but should
# skip any accounts that have been suspended.

users = [
    {"name": "Alice", "suspended": False},
    {"name": "Bob",   "suspended": True},
    {"name": "Carol", "suspended": False},
    {"name": "Dan",   "suspended": True},
    {"name": "Eve",   "suspended": False},
]

print("\n--- Sending Newsletter ---")
for user in users:
    if user["suspended"]:
        print(f"⏭️  Skipping {user['name']} (account suspended)")
        continue
    print(f"📧 Newsletter sent to {user['name']}")

# Output:
# 📧 Newsletter sent to Alice
# ⏭️  Skipping Bob (account suspended)
# 📧 Newsletter sent to Carol
# ⏭️  Skipping Dan (account suspended)
# 📧 Newsletter sent to Eve

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 10: Skipping empty form entries
# ---------------------------------------------------------------
# A form was submitted with some fields left blank.
# We skip blank entries when processing the responses.

responses = ["Alice", "", "Charlie", "", "Eve", "Frank"]

print("\n--- Processing Form Responses ---")
for response in responses:
    if response == "":
        continue  # skip blank entries
    print(f"Processing response from: {response}")


# ----------------------------------------------------------------
# 7. NESTED LOOPS
# ----------------------------------------------------------------
# A nested loop is a loop inside another loop.
# The INNER loop runs completely from start to finish for
# EACH single iteration of the OUTER loop.
#
# Think of it like this:
#   Outer loop = each class in a school
#   Inner loop = each student in that class
#   → For every class, we go through every student.
# ----------------------------------------------------------------

# SIMPLE EXAMPLE — Multiplication table
print("\n--- Multiplication Table (1 to 3) ---")
for i in range(1, 4):           # outer loop: rows
    for j in range(1, 4):       # inner loop: columns
        print(f"{i} x {j} = {i * j}")
    print("---")                # prints after each row

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 11: School timetable
# ---------------------------------------------------------------
# A school has 3 classes and each class has 3 subjects.
# Print each class and its subjects.

classes = ["S1", "S2", "S3"]
subjects = ["Maths", "English", "Science"]

print("\n--- School Timetable ---")
for cls in classes:
    print(f"\nClass {cls}:")
    for subject in subjects:
        print(f"   → {subject}")

# Output:
# Class S1:
#    → Maths
#    → English
#    → Science
# Class S2:
#    → Maths
# ... and so on

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 12: Seating chart
# ---------------------------------------------------------------
# A cinema has 3 rows and 4 seats per row.
# Label each seat (e.g. Row 1, Seat 1).

print("\n--- Cinema Seating Chart ---")
for row in range(1, 4):
    for seat in range(1, 5):
        print(f"Row {row}, Seat {seat}")
    print()  # blank line between rows


# ----------------------------------------------------------------
# 8. LOOPING OVER A DICTIONARY
# ----------------------------------------------------------------
# A dictionary stores data as key-value pairs (like a form or
# a profile card). Looping over a dictionary lets you read or
# display all the information stored inside it.
#
# There are three ways to loop over a dictionary:
#   .keys()   → loop over the keys only
#   .values() → loop over the values only
#   .items()  → loop over both key and value at the same time
# ----------------------------------------------------------------

student_profile = {
    "name": "Alice",
    "age": 20,
    "program": "Data Science",
    "university": "Makerere University",
    "year": 2
}

print("\n--- Student Profile (keys only) ---")
for key in student_profile:
    print(key)

print("\n--- Student Profile (values only) ---")
for value in student_profile.values():
    print(value)

print("\n--- Student Profile (full details) ---")
for key, value in student_profile.items():
    print(f"{key}: {value}")

# ---------------------------------------------------------------
# 🌍 REAL-WORLD SCENARIO 13: Printing a shop receipt
# ---------------------------------------------------------------
# A customer's order is stored as a dictionary where the
# keys are item names and the values are prices.
# We loop to print a formatted receipt.

order = {
    "Rice (5kg)":     15000,
    "Cooking Oil":    12000,
    "Sugar (2kg)":     7000,
    "Tomatoes":        3500,
    "Milk (1L)":       4500,
}

print("\n=============================")
print("       SHOP RECEIPT")
print("=============================")

receipt_total = 0
for item, price in order.items():
    print(f"{item:<20} UGX {price:>7,}")
    receipt_total += price

print("-----------------------------")
print(f"{'TOTAL':<20} UGX {receipt_total:>7,}")
print("=============================")
print("    Thank you, come again!")


# ----------------------------------------------------------------
# 9. else WITH A LOOP
# ----------------------------------------------------------------
# Python allows an else block after a loop.
# The else block runs ONLY if the loop completed normally,
# meaning it was NOT exited by a break statement.
#
# This is useful for searching — if you search a whole list
# and never find what you're looking for, the else block
# lets you know the search is complete and nothing was found.
# ----------------------------------------------------------------

# EXAMPLE — Search for a student in the register
registered_students = ["Alice", "Bob", "Charlie", "Diana"]
search_name = "Kenneth"

print(f"\n--- Searching for '{search_name}' ---")
for name in registered_students:
    if name == search_name:
        print(f"✅ {search_name} is registered.")
        break
else:
    # This only runs if the loop finished without finding the name
    print(f"❌ {search_name} is NOT found in the register.")

# Output: ❌ Kenneth is NOT found in the register.


# ----------------------------------------------------------------
# 10. SUMMARY — WHEN TO USE WHICH LOOP
# ----------------------------------------------------------------
#
#  ┌─────────────────────────────────────────────────────────────┐
#  │  USE A for LOOP WHEN:                                       │
#  │  • You are going through a list, string, or dictionary      │
#  │  • You know exactly how many times to repeat                │
#  │  • Example: process every student, every item in a cart     │
#  ├─────────────────────────────────────────────────────────────┤
#  │  USE A while LOOP WHEN:                                     │
#  │  • You don't know how many times you'll need to repeat      │
#  │  • You are waiting for something to happen (user input,     │
#  │    a condition to change, etc.)                             │
#  │  • Example: ATM PIN retry, menu that runs until user quits  │
#  ├─────────────────────────────────────────────────────────────┤
#  │  USE break WHEN:                                            │
#  │  • You found what you were looking for — stop early         │
#  │  • Example: found available seat, found a user in a list    │
#  ├─────────────────────────────────────────────────────────────┤
#  │  USE continue WHEN:                                         │
#  │  • You want to skip certain items but keep looping          │
#  │  • Example: skip suspended users, skip blank form entries   │
#  └─────────────────────────────────────────────────────────────┘
