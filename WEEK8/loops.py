# ============================================================
# LOOPS IN PYTHON
# ============================================================
# Loops let you repeat a block of code multiple times,
# instead of writing the same code over and over.
# Python has two main types of loops: for and while.
# ============================================================


# ------------------------------------------------------------
# 1. for LOOP
# ------------------------------------------------------------
# Used to iterate over a sequence (list, string, range, etc.)
# It runs once for each item in the sequence.

fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# mango
# orange


# ------------------------------------------------------------
# 2. for LOOP with range()
# ------------------------------------------------------------
# range(stop)          → 0 up to (but not including) stop
# range(start, stop)   → start up to (but not including) stop
# range(start, stop, step) → with a custom step

# Count from 0 to 4
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

print("---")

# Count from 1 to 5
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

print("---")

# Count in steps of 2
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10

print("---")

# Count backwards
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1


# ------------------------------------------------------------
# 3. for LOOP over a STRING
# ------------------------------------------------------------
# A string is a sequence of characters, so you can loop over it.

name = "Python"

for letter in name:
    print(letter)

# Output: P, y, t, h, o, n (each on its own line)


# ------------------------------------------------------------
# 4. while LOOP
# ------------------------------------------------------------
# Keeps running as long as a condition is True.
# ⚠️ Make sure the condition eventually becomes False, or it
#    will loop forever (infinite loop)!

count = 1

while count <= 5:
    print(f"Count is: {count}")
    count += 1  # IMPORTANT: update the variable to avoid infinite loop

# Output: Count is: 1, Count is: 2, ... Count is: 5


# ------------------------------------------------------------
# 5. break STATEMENT
# ------------------------------------------------------------
# Exits the loop immediately, even if the condition is still True.

for number in range(1, 11):
    if number == 5:
        print("Found 5! Stopping the loop.")
        break
    print(number)

# Output: 1, 2, 3, 4, Found 5! Stopping the loop.


# ------------------------------------------------------------
# 6. continue STATEMENT
# ------------------------------------------------------------
# Skips the current iteration and jumps to the next one.

for number in range(1, 8):
    if number == 4:
        continue  # Skip 4
    print(number)

# Output: 1, 2, 3, 5, 6, 7  (4 is skipped)


# ------------------------------------------------------------
# 7. NESTED LOOPS
# ------------------------------------------------------------
# A loop inside another loop.
# The inner loop completes fully for each iteration of the outer loop.

for i in range(1, 4):          # outer loop: 1, 2, 3
    for j in range(1, 4):      # inner loop: 1, 2, 3
        print(f"{i} x {j} = {i * j}")
    print("---")

# Prints a mini multiplication table


# ------------------------------------------------------------
# 8. else WITH A LOOP
# ------------------------------------------------------------
# The else block runs after the loop finishes normally
# (i.e., it did NOT exit via break).

for i in range(3):
    print(i)
else:
    print("Loop finished without break.")

print("---")

# With break — else does NOT run
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will NOT print because we broke out.")


# ------------------------------------------------------------
# 9. LOOPING OVER A DICTIONARY
# ------------------------------------------------------------

student = {
    "name": "Alice",
    "age": 20,
    "program": "Data Science"
}

# Loop over keys
for key in student:
    print(key)

# Loop over values
for value in student.values():
    print(value)

# Loop over both keys and values
for key, value in student.items():
    print(f"{key}: {value}")


# ------------------------------------------------------------
# 10. PRACTICAL EXAMPLES
# ------------------------------------------------------------

# -- Sum of numbers 1 to 10 --
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of 1 to 10: {total}")  # 55

# -- Print only even numbers from a list --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(num)  # 2, 4, 6, 8, 10

# -- Countdown using while --
countdown = 5
while countdown > 0:
    print(f"Launching in {countdown}...")
    countdown -= 1
print("🚀 Launched!")
