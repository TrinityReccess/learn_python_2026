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
#
# ✅ WHY USE A for LOOP?
# ---------------------------------------------------------------
# Use a for loop when:
#   • You already HAVE a collection (list, string, dictionary)
#     and you want to do something with each item inside it.
#   • You know EXACTLY how many times to repeat (e.g. 10 students,
#     5 items in a cart, 26 letters of the alphabet).
#   • You want clean, readable code that clearly says
#     "for each item, do this".
#
# DON'T use a for loop when:
#   • You don't know when to stop (use while instead).
#   • You are waiting for something to happen (e.g. user input,
#     a sensor reading — use while instead).
#
# REAL-WORLD EXAMPLES OF WHEN TO USE for:
#   → Send an SMS to every contact in a phone book
#   → Calculate the average mark of every student in a class
#   → Display every product on an e-commerce website
#   → Check every uploaded image for a virus
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
#
# ✅ WHY USE range()?
# ---------------------------------------------------------------
# Use range() when:
#   • You want to repeat something exactly N times
#     (e.g. "do this 10 times").
#   • You need a counter — a number that goes up or down
#     with each step (e.g. numbering students 1, 2, 3...).
#   • You want to count in steps (e.g. every 2nd seat, every
#     5th row, going backwards from 10 to 1).
#   • You don't have a list to loop over — you just need
#     a sequence of numbers.
#
# REAL-WORLD EXAMPLES:
#   → Generate 50 student ID numbers automatically
#   → Print a times table (1x1 to 12x12)
#   → Count down before a rocket launches
#   → Number each line in a printed report
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
# ✅ WHY USE A while LOOP?
# ---------------------------------------------------------------
# Use a while loop when:
#   • You do NOT know how many times the loop will run.
#     The loop runs for as long as something is True.
#   • You are WAITING for something to happen:
#     → Waiting for the user to enter the correct PIN
#     → Waiting for a sensor to detect movement
#     → Waiting for a server to respond
#   • You are building a MENU that should keep showing
#     until the user chooses to exit.
#   • You are building a GAME that keeps running until
#     the player loses or wins.
#
# DON'T use a while loop when:
#   • You already have a list, string, or dictionary to
#     loop over — use for instead.
#   • You know exactly how many times to repeat — use for
#     with range() instead.
#
# REAL-WORLD EXAMPLES:
#   → A USSD mobile money menu (*165#) — keeps showing
#     until you press 0 to exit
#   → An ATM that lets you try your PIN up to 3 times
#   → A game loop that runs until the player's health = 0
#   → A chat app waiting for new messages to arrive
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
#
# ✅ WHY USE break?
# ---------------------------------------------------------------
# Use break when:
#   • You are SEARCHING for something — once you find it,
#     stop. There is no reason to keep checking the rest.
#   • Continuing to loop after finding the answer would
#     WASTE time and slow your program down.
#   • You want to EXIT a while True menu when the user
#     chooses the "Exit" option.
#
# THINK OF IT LIKE THIS:
#   Imagine you are looking for your friend in a crowd of
#   1000 people. The moment you spot them, you stop looking.
#   You do NOT keep walking through the remaining 999 people
#   just because you started.
#
# REAL-WORLD EXAMPLES:
#   → Stop searching a database once the matching record is found
#   → Exit a menu when the user presses 0
#   → Stop checking seats once the first available one is found
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
#
# ✅ WHY USE continue?
# ---------------------------------------------------------------
# Use continue when:
#   • You have a list but only SOME items should be processed.
#     Instead of wrapping everything in a big if-else block,
#     you skip the ones you don't need early with continue.
#   • It makes your code CLEANER and easier to read.
#
# THINK OF IT LIKE THIS:
#   Imagine a teacher marking attendance. When she sees a name
#   of a student who is on sick leave, she calls "skip" and
#   moves to the next name — she does not stop taking attendance
#   entirely, she just skips that one student.
#
# REAL-WORLD EXAMPLES:
#   → Skip suspended accounts when sending a newsletter
#   → Skip blank/empty entries in a submitted form
#   → Skip out-of-stock items when printing a product list
#   → Skip weekends when generating a work schedule
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


# ================================================================
# 11. REAL-WORLD PROJECT — USSD MOBILE MONEY MENU
# ================================================================
#
# Have you ever dialed *165# or *185# on your phone?
# That is a USSD menu — a simple text-based menu that lets
# you send money, buy airtime, check your balance, and more.
#
# WHY while loop here?
# → Because we do NOT know how many options the user will
#   select before they exit. The menu must keep showing
#   after every action until the user consciously chooses
#   to leave (presses 0). That is exactly what while True does.
#
# WHY break?
# → When the user selects 0 (Exit), there is nothing more
#   to do. We use break to exit the while True loop cleanly.
#
# WHY if/elif/else inside the loop?
# → Each number the user presses is a different action.
#   We check what they pressed and run the matching code.
#   If they press something invalid, we tell them and show
#   the menu again — the while loop handles that automatically.
#
# This example uses concepts from multiple weeks:
#   ✅ Variables (Week 4)
#   ✅ input() and f-strings (Week 5)
#   ✅ if / elif / else (Week 6)
#   ✅ while loop + break (Week 8)  ← YOU ARE HERE
# ================================================================

balance = 50000  # The user's starting mobile money balance in UGX

print("\n" + "=" * 38)
print("     WELCOME TO MOBILE MONEY")
print("=" * 38)

while True:
    # ── Show the main menu every time the loop runs ──
    print("\n" + "-" * 38)
    print("  MAIN MENU")
    print("-" * 38)
    print("  1. Send Money")
    print("  2. Withdraw Cash")
    print("  3. Check Balance")
    print("  4. Buy Airtime")
    print("  5. Pay Bills")
    print("  0. Exit")
    print("-" * 38)

    choice = input("  Enter choice: ").strip()

    # ── OPTION 1: Send Money ──────────────────────────
    if choice == "1":
        print("\n  --- SEND MONEY ---")
        recipient = input("  Enter recipient number: ")
        amount_input = input("  Enter amount (UGX): ")

        # Make sure the user typed a valid number
        if not amount_input.isdigit():
            print("  ❌ Invalid amount. Please enter numbers only.")
        else:
            amount = int(amount_input)
            if amount <= 0:
                print("  ❌ Amount must be greater than 0.")
            elif amount > balance:
                print(f"  ❌ Insufficient balance. Your balance is UGX {balance:,}")
            else:
                balance -= amount
                print(f"  ✅ UGX {amount:,} sent to {recipient} successfully.")
                print(f"     New balance: UGX {balance:,}")

    # ── OPTION 2: Withdraw Cash ───────────────────────
    elif choice == "2":
        print("\n  --- WITHDRAW CASH ---")
        agent = input("  Enter agent number: ")
        amount_input = input("  Enter amount to withdraw (UGX): ")

        if not amount_input.isdigit():
            print("  ❌ Invalid amount. Please enter numbers only.")
        else:
            amount = int(amount_input)
            if amount <= 0:
                print("  ❌ Amount must be greater than 0.")
            elif amount > balance:
                print(f"  ❌ Insufficient balance. Your balance is UGX {balance:,}")
            else:
                balance -= amount
                print(f"  ✅ Cash withdrawal of UGX {amount:,} from agent {agent} successful.")
                print(f"     New balance: UGX {balance:,}")

    # ── OPTION 3: Check Balance ───────────────────────
    elif choice == "3":
        print("\n  --- ACCOUNT BALANCE ---")
        print(f"  Your current balance is: UGX {balance:,}")

    # ── OPTION 4: Buy Airtime ─────────────────────────
    elif choice == "4":
        print("\n  --- BUY AIRTIME ---")
        # A sub-menu inside the main menu — this is a NESTED menu!
        print("  Select network:")
        print("    1. MTN")
        print("    2. Airtel")
        print("    3. Africell")
        print("    9. Back to Main Menu")

        network_choice = input("  Enter choice: ").strip()

        if network_choice == "9":
            print("  ↩️  Returning to main menu...")
        else:
            networks = {"1": "MTN", "2": "Airtel", "3": "Africell"}

            if network_choice not in networks:
                print("  ❌ Invalid network selected.")
            else:
                network_name = networks[network_choice]
                amount_input = input(f"  Enter airtime amount for {network_name} (UGX): ")

                if not amount_input.isdigit():
                    print("  ❌ Invalid amount. Please enter numbers only.")
                else:
                    amount = int(amount_input)
                    if amount <= 0:
                        print("  ❌ Amount must be greater than 0.")
                    elif amount > balance:
                        print(f"  ❌ Insufficient balance. Your balance is UGX {balance:,}")
                    else:
                        balance -= amount
                        print(f"  ✅ UGX {amount:,} airtime loaded on {network_name} successfully.")
                        print(f"     New balance: UGX {balance:,}")

    # ── OPTION 5: Pay Bills ───────────────────────────
    elif choice == "5":
        print("\n  --- PAY BILLS ---")
        # Another sub-menu
        print("  Select biller:")
        print("    1. UMEME (Electricity)")
        print("    2. NWSC (Water)")
        print("    3. URA (Tax)")
        print("    9. Back to Main Menu")

        bill_choice = input("  Enter choice: ").strip()

        if bill_choice == "9":
            print("  ↩️  Returning to main menu...")
        else:
            billers = {
                "1": "UMEME (Electricity)",
                "2": "NWSC (Water)",
                "3": "URA (Tax)"
            }

            if bill_choice not in billers:
                print("  ❌ Invalid biller selected.")
            else:
                biller_name = billers[bill_choice]
                ref = input(f"  Enter your {biller_name} reference number: ")
                amount_input = input(f"  Enter amount to pay (UGX): ")

                if not amount_input.isdigit():
                    print("  ❌ Invalid amount. Please enter numbers only.")
                else:
                    amount = int(amount_input)
                    if amount <= 0:
                        print("  ❌ Amount must be greater than 0.")
                    elif amount > balance:
                        print(f"  ❌ Insufficient balance. Your balance is UGX {balance:,}")
                    else:
                        balance -= amount
                        print(f"  ✅ UGX {amount:,} paid to {biller_name} (Ref: {ref}) successfully.")
                        print(f"     New balance: UGX {balance:,}")

    # ── OPTION 0: Exit ────────────────────────────────
    elif choice == "0":
        print("\n  Thank you for using Mobile Money.")
        print("  Your final balance: UGX {:,}".format(balance))
        print("  Goodbye! 👋")
        print("=" * 38)
        break  # ← EXIT the while True loop — the program ends here

    # ── INVALID INPUT ─────────────────────────────────
    else:
        print("  ❌ Invalid choice. Please enter a number from the menu.")
        # The while loop automatically goes back to the top
        # and shows the menu again — no extra code needed!

# ================================================================
# WHAT THIS MENU DEMONSTRATES:
# ================================================================
#   ✅ while True       — keeps the menu running indefinitely
#   ✅ break            — cleanly exits when user chooses 0
#   ✅ if/elif/else     — handles each menu option differently
#   ✅ Nested menus     — sub-menus inside the main menu
#   ✅ Input validation — checks the user typed a valid number
#   ✅ Running total    — balance updates after every transaction
#
# This is how REAL mobile money systems work at their core.
# The actual MTN MoMo or Airtel Money system is much larger,
# but the fundamental logic is exactly this — a loop that
# shows a menu, reads input, runs an action, and repeats.
# ================================================================
