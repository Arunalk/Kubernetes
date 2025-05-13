# <span style="color:#A7C7E7;">Random Module</span>

The `random` module in Python provides functions to generate random numbers and make random selections from sequences like lists, tuples, and strings. It is useful for simulations, games, cryptography, and other applications requiring randomness.

### **1. Importing the `random` Module**
Before using any random functions, you need to import the module:
```python
import random
```
---

## `Using `random` Module in Python`

### **2. Generating Random Numbers**

#### **`(a) Random Integer (`randint()`)`**
Generates a random integer between the specified range (inclusive).
```python
print(random.randint(1, 10))  # Generates a random number between 1 and 10
```

#### **`(b) Random Float (`random()`)`**
Generates a random floating-point number between `0` and `1`.
```python
print(random.random())  # Example output: 0.6789
```

#### **`(c) Random Float in a Range (`uniform()`)`**
Generates a random floating-point number between a given range.
```python
print(random.uniform(1.5, 5.5))  # Example output: 3.789
```

### **3. Random Selection from a List**

#### **(a) `Select One Random Element (`choice()`)`**
Chooses a single random element from a sequence (list, tuple, or string).
```python
fruits = ["Apple", "Banana", "Cherry"]
print(random.choice(fruits))  # Example output: "Banana"
```

#### **`(b) Select Multiple Random Elements (`sample()`)`**
Selects `n` unique random elements from a list.
```python
print(random.sample(fruits, 2))  # Example output: ["Apple", "Cherry"]
```

#### **`(c) Shuffle a List (`shuffle()`)`**
Randomly shuffles the elements in a list (modifies the list in place).
```python
random.shuffle(fruits)
print(fruits)  # Example output: ['Cherry', 'Banana', 'Apple']
```

### **4. Random Boolean Values**
Simulates a coin flip by randomly choosing `True` or `False`.
```python
print(random.choice([True, False]))  # Example output: True
```

