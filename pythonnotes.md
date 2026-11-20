# Python Fundamentals — Lessons 1–5

## 1. Variables

Variables store data in Python.

```python
name = "Siddu"
age = 21
balance = 10000
```

A variable can be updated:

```python
balance = 10000
balance = balance + 2500
balance = balance - 1500

print(balance)
```

**Important:** A variable stores its latest assigned value.

---

## 2. Data Types

Python has different data types.

| Data Type | Description | Example |
|---|---|---|
| `int` | Integer numbers | `25`, `100`, `-5` |
| `float` | Decimal numbers | `25.5`, `10.75` |
| `str` | Text | `"Siddu"` |
| `bool` | True or False | `True`, `False` |

Example:

```python
name = "Siddu"
balance = 85
age = 21
amount = 25.10
is_married = False

print(type(name))
print(type(balance))
print(type(age))
print(type(amount))
print(type(is_married))
```

`type()` identifies the data type of a variable.

In a Python script, use `print()` to display the result explicitly.

```python
print(type(name))
```

---

## 3. User Input — `input()`

`input()` collects information from the user.

```python
name = input("Enter your name: ")
print(name)
```

The program waits for the user to enter information.

**Important:** `input()` always returns a string (`str`), even if the user enters a number.

---

## 4. Type Conversion

Type conversion changes data from one type to another.

| Function | Purpose |
|---|---|
| `int()` | Converts into an integer |
| `float()` | Converts into a decimal number |
| `str()` | Converts into a string |

Example:

```python
age = int(input("Enter your age: "))
income = float(input("Enter your income: "))
```

### How it works

```python
age = int(input("Enter your age: "))
```

1. `input()` collects the input.
2. `int()` converts the input into an integer.
3. The converted value is stored in `age`.

---

## 5. The `print()` Function

`print()` displays information in the terminal.

```python
name = "Siddu"
balance = 10000

print(name)
print(balance)
```

You can also combine text and variables:

```python
print("Name:", name)
print("Balance:", balance)
```

---

## 6. Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor division | `10 // 3` |
| `%` | Modulus (remainder) | `10 % 3` |
| `**` | Exponentiation | `2 ** 3` |

Example:

```python
balance = 10000
income = 5000
expenses = 2000

final_balance = balance + income - expenses

print(final_balance)
```

Output:

```text
13000
```

---

## 7. Displaying Labels

Labels make program output easier to understand.

```python
name = "Siddu"
balance = 10000

print("Name:", name)
print("Balance:", balance)
```

Output:

```text
Name: Siddu
Balance: 10000
```

The text inside quotation marks is the label.

---

# Project 1: Personal Finance & Expense Tracker

## Milestone 1 — Financial Calculator

### Objective
Create a program that collects financial information and calculates the final balance.

### Requirements
- Collect the user's name.
- Collect the current balance.
- Collect monthly income.
- Collect monthly expenses.
- Calculate the final balance.
- Display a financial summary.

### Formula

Final Balance = Current Balance + Monthly Income − Monthly Expenses

### Concepts used
- Variables
- Data types
- `input()`
- Type conversion
- `print()`
- Arithmetic operators

**Status: Completed ✅**

---

# Git & GitHub — Important Concept

### VS Code
VS Code contains your local working files.

### Git
Git tracks changes to your files and maintains their history.

### GitHub
GitHub stores your repository remotely online.

| Action | What happens |
|---|---|
| Delete a file in VS Code | Deleted locally, not automatically on GitHub |
| Commit a deletion | Git records the deletion locally |
| Push the commit | GitHub reflects the deletion |
| Delete a file directly on GitHub | The remote file is deleted |

### Remember

**VS Code = Working files**

**Git = Version control and history**

**GitHub = Remote repository**

Git history can help you recover earlier versions of committed files.

---

# My Learning Process

For every concept:

**Learn → Experiment → Build → Test → Debug → Improve → Commit**

My goal is to understand concepts and implement them independently rather than blindly copy code.

---

## Progress

- [x] Variables
- [x] Data Types
- [x] `input()`
- [x] Type Conversion
- [x] `print()`
- [x] Labels
- [x] Arithmetic Operators
- [x] Financial Calculator — Milestone 1
- [x] Git revision basics

## Next Lesson

**Conditional Statements — `if`, `elif`, and `else`**
# Python Notes — Lesson 6: Conditional Statements

## 1. What are Conditional Statements?

Conditional statements allow a program to make decisions based on whether a condition is `True` or `False`.

They allow programs to execute different blocks of code depending on the situation.

---

## 2. The `if` Statement

The `if` statement executes a block of code when a condition is `True`.

### Syntax

```python
if condition:
    statement
```

### Example

```python
balance = 15000

if balance > 10000:
    print("Healthy balance")
```

### How it works

1. Python evaluates the condition.
2. If the condition is `True`, the indented code executes.
3. If the condition is `False`, Python skips the block.

---

## 3. Comparison Operators

Comparison operators compare values and produce either `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `5 < 10` |
| `>=` | Greater than or equal to | `10 >= 10` |
| `<=` | Less than or equal to | `5 <= 10` |
| `==` | Equal to | `10 == 10` |
| `!=` | Not equal to | `10 != 5` |

---

## 4. The `else` Statement

`else` executes when the condition associated with `if` is `False`.

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Example

```python
balance = 5000

if balance >= 10000:
    print("Healthy balance")
else:
    print("Low balance")
```

If the balance is below ₹10,000, the `else` block executes.

---

## 5. The `elif` Statement

`elif` means **else if**.

It allows us to check additional conditions when previous conditions are `False`.

### Syntax

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

### Example

```python
balance = 7500

if balance >= 10000:
    print("Healthy balance")
elif balance >= 5000:
    print("Moderate balance")
else:
    print("Low balance")
```

### How Python evaluates it

Python evaluates conditions from top to bottom.

- If the first condition is `True`, its block executes.
- Otherwise, Python checks the next condition.
- If no condition is `True`, the `else` block executes.

Only one block executes in an `if`–`elif`–`else` chain.

---

## 6. Logical Operators

Logical operators allow us to combine or modify conditions.

### `and`

Both conditions must be `True`.

```python
age = 21

if age >= 18 and age <= 25:
    print("Age is between 18 and 25")
```

| Condition 1 | Condition 2 | Result |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### `or`

At least one condition must be `True`.

```python
age = 17

if age < 18 or age > 60:
    print("Outside the standard range")
```

### `not`

`not` reverses a Boolean result.

```python
is_active = False

if not is_active:
    print("Account is inactive")
```

---

## 7. Understanding Conditions from Top to Bottom

Example:

```python
balance = 15000

if balance >= 20000:
    print("Premium balance")
elif balance >= 10000:
    print("Good balance")
elif balance >= 5000:
    print("Moderate balance")
else:
    print("Low balance")
```

Python checks the first condition.

If it is false, it moves to the next.

When a condition is true, Python executes its block and skips the remaining blocks.

### Important Programming Principle

Conditions should be arranged carefully.

In many cases, unnecessary upper-bound conditions can be removed because earlier conditions already eliminate those ranges.

---

# Practice Program — ATM Balance Analyzer

```python
phase 1 revision
# Python — Phase 1: Fundamentals

## 1. Variables

Variables store data.

```python
name = "Siddharth"
age = 20
salary = 25000
```

A variable can be reassigned:

```python
x = 10
x = 20
print(x)
```

Output:
```
20
```

---

## 2. Data Types

Python has different types of data.

| Data Type | Example |
|---|---|
| `int` | `10` |
| `float` | `10.5` |
| `str` | `"Python"` |
| `bool` | `True`, `False` |

To check the type:

```python
x = 10
print(type(x))
```

---

## 3. Input

`input()` allows the user to enter data.

```python
name = input("Enter your name: ")
print(name)
```

**Important:** `input()` returns a string, even when the user enters a number.

---

## 4. Type Conversion

Convert data from one type to another.

```python
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
```

| Function | Purpose |
|---|---|
| `int()` | Converts to integer |
| `float()` | Converts to decimal |
| `str()` | Converts to string |
| `bool()` | Converts to Boolean |

---

## 5. Output — `print()`

Display information.

```python
name = "Siddharth"
salary = 25000

print("Name:", name)
print("Salary:", salary)
```

---

## 6. Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor division | `10 // 3` |
| `%` | Modulo/remainder | `10 % 3` |
| `**` | Exponent | `2 ** 3` |

### Modulo

Modulo returns the remainder.

```python
print(10 % 2)  # 0
print(10 % 3)  # 1
```

Checking even numbers:

```python
if x % 2 == 0:
    print("Even")
```

Checking odd numbers:

```python
if x % 2 == 1:
    print("Odd")
```

---

## 7. Financial Calculator

### Formula

Final Balance = Current Balance + Income − Expenses

```python
current_balance = float(input("Enter current balance: "))
income = float(input("Enter income: "))
expenses = float(input("Enter expenses: "))

final_balance = current_balance + income - expenses

print("Final balance:", final_balance)
```

### Project Milestone

Built a financial calculator that:
- Accepts user information.
- Accepts current balance.
- Accepts income.
- Accepts expenses.
- Calculates final balance.
- Displays a financial summary.

---

## 8. Comparison Operators

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |

Example:

```python
x = 10

print(x > 5)
print(x == 10)
```

---

## 9. Logical Operators

### AND

Both conditions must be true.

```python
if age >= 18 and age <= 30:
    print("Eligible")
```

### OR

At least one condition must be true.

```python
if age < 18 or age > 60:
    print("Special category")
```

### NOT

Reverses a Boolean result.

```python
x = True
print(not x)
```

---

## 10. Conditional Statements

### if

```python
if condition:
    print("True")
```

### if-else

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### if-elif-else

```python
balance = 12000

if balance >= 20000:
    print("Premium balance")
elif balance >= 10000:
    print("Good balance")
elif balance >= 5000:
    print("Moderate balance")
else:
    print("Low balance")
```

Python checks conditions from top to bottom.

Once a matching condition is found, the remaining conditions in that chain are skipped.

---

## 11. While Loop

A `while` loop runs as long as its condition is True.

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

### Important

You must update the variable appropriately to prevent an infinite loop.

### Countdown

```python
count = 10

while count > 0:
    print(count)
    count = count - 1
```

---

## 12. For Loop

A `for` loop iterates through a sequence or range.

```python
for i in range(1, 11):
    print(i)
```

Output: 1 through 10.

### range()

| Syntax | Result |
|---|---|
| `range(5)` | 0–4 |
| `range(1, 5)` | 1–4 |
| `range(1, 11)` | 1–10 |
| `range(2, 11, 2)` | 2, 4, 6, 8, 10 |

The stop value is excluded.

---

## 13. Counters

A counter tracks how many times something happens.

```python
count = 0

while count < 5:
    print(count)
    count = count + 1
```

---

## 14. Accumulators

An accumulator stores and progressively updates a total.

```python
total = 0

for i in range(1, 6):
    total = total + i

print(total)
```

The accumulator is useful for:
- Total expenses.
- Total income.
- Total sales.
- Total marks.

---

## 15. Calculating Averages

Formula:

Average = Total / Number of Values

```python
total = 1000
average = total / 5

print(average)
```

---

## 16. Expense Calculator

```python
total_expense = 0

for count in range(1, 6):
    expense = int(input("Enter expense: "))
    total_expense = total_expense + expense

print("Total expenses:", total_expense)

average_expense = total_expense / 5

print("Average expense:", average_expense)
```

This program:
- Accepts five expenses.
- Calculates the total.
- Calculates the average.

---

# 17. Phase 1 Revision Project — Monthly Budget Analyzer

```python
name = input("Enter your name: ")
monthly_income = int(input("Enter your monthly income: "))

expense = 0
total_expense = 0

for i in range(1, 6):
    expense = int(input("Enter expense: "))
    total_expense = total_expense + expense

average_expense = total_expense / 5
remaining_bal = monthly_income - total_expense

if remaining_bal > 10000:
    assessment = "Excellent savings!"
elif remaining_bal > 5000:
    assessment = "Good savings!"
elif remaining_bal > 0:
    assessment = "Low savings!"
else:
    assessment = "You are overspending!"

print("Name:", name)
print("Income:", monthly_income)
print("Total expenses:", total_expense)
print("Average expense:", average_expense)
print("Remaining balance:", remaining_bal)
print("Assessment:", assessment)
```

## Concepts used

- Variables
- Data types
- Input
- Type conversion
- Arithmetic
- Conditions
- `if`, `elif`, `else`
- `for`
- `range()`
- Accumulators
- Average calculation

---

# Phase 1 Completion

**Completed: Python Fundamentals**

### Learning workflow

Learn → Experiment → Build → Test → Debug → Improve → Commit to GitHub.

### Phase 2

Python Data Structures:

- Lists
- List operations
- Iteration over lists
- List methods
- Dictionaries
- Storing transactions

**Project direction:** Personal Finance & Expense Tracker.