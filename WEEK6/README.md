# WEEK 6 — Conditional Statements in Python

This week covers how Python makes decisions using **conditional statements**.  
You'll learn how to control the flow of your program based on different conditions.

---

## 📁 Files

| File | Description |
|---|---|
| `conditional_statments_explained.py` | Full notes and examples on conditional statements |
| `nested_if.py` | Examples focused specifically on nested `if` statements |

---

## 📚 Topics Covered

### 1. `if` Statement
Runs a block of code only when a condition is `True`.
```python
if age >= 18:
    print("You are an adult.")
```

### 2. `if...else` Statement
Runs one block if `True`, another if `False`.
```python
if temperature > 25:
    print("It's hot.")
else:
    print("It's not that hot.")
```

### 3. `if...elif...else` Statement
Checks multiple conditions in order.
```python
if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

### 4. Nested `if` Statements
An `if` statement inside another `if` statement.
```python
if is_logged_in:
    if is_admin:
        print("Admin access.")
    else:
        print("Standard access.")
```

### 5. Comparison Operators
Used to compare values inside conditions.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### 6. Logical Operators
Combine multiple conditions together.

| Operator | Meaning |
|---|---|
| `and` | True if **both** conditions are True |
| `or` | True if **at least one** condition is True |
| `not` | Reverses the result |

```python
if has_ticket and has_id:
    print("Entry granted.")
```

### 7. Shorthand `if` (Ternary)
Write a simple `if...else` on a single line.
```python
result = "Odd" if num % 2 != 0 else "Even"
```

### 8. Truthy & Falsy Values
Python treats certain values as `False` automatically.

| Falsy Values | Truthy Values |
|---|---|
| `0`, `0.0` | Any non-zero number |
| `""` (empty string) | Any non-empty string |
| `[]`, `{}` (empty collections) | Any non-empty collection |
| `None`, `False` | `True` |

### 9. Membership with `in`
Check if a value exists inside a list or string.
```python
if "banana" in fruits:
    print("Banana is available.")
```

### 10. `match` Statement *(Python 3.10+)*
A cleaner way to handle multiple specific values (like switch/case).
```python
match day:
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Weekday.")
```

---

## ▶️ How to Run

```bash
python conditional_statments_explained.py
```

---

## 🗓️ Week Overview

| Week | Topics |
|---|---|
| Week 4 | Data types, first programs |
| Week 5 | Operators, conditions intro, user input |
| **Week 6** | **Conditional statements (if, elif, else, nested, match)** |
