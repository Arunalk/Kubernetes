# 🧬 Inheritance in Python 

## Overview

- Inheritance allows one class (child) to inherit the properties and methods of another class (parent), promoting code reuse and logical structure.
---

## 🧬 How to Call a Parent Class or Function in Inheritance

- Child class can inherit few functions from parent class.

- When you're working with inheritance, you may want to:

- Call the constructor of the parent class

- Call any other method from the parent class

- You do this using either:

    - super() (recommended)

- Direct class name (less preferred, but valid)

### 1. ✅ 1. Calling the Parent Class Constructor

🔸 Using `super()` (clean and recommended): 

```yaml
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent's __init__
        print("Child constructor")

c = Child()
# Output:
# Parent constructor
# Child constructor
```
🔹 OR Using the class name (not recommended unless needed):
```yaml
Parent.__init__(self)
```

### ✅ 2. Calling a Parent Method
Example:
```yaml
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Calls Parent's greet method
        print("Hello from Child")

c = Child()
c.greet()
# Output:
# Hello from Parent
# Hello from Child
```