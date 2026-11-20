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