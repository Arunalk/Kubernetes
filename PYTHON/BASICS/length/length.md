# <span style="color:#A7C7E7;">Length function</span>
- The `len()` function is used to determine the length (number of elements) of various data structures such as strings, lists, tuples, dictionaries, and sets.
---

### `Using `len()` Function in Python`

### **1. Using `len()` with Strings**
Counts the number of characters in a string, including spaces.

```python
text = "Hello, World!"
print(len(text))  # Output: 13
```

### **2. Using `len()` with Lists**
Counts the number of elements in a list.

```python
fruits = ["Apple", "Banana", "Cherry"]
print(len(fruits))  # Output: 3
```

### **3. Using `len()` with Tuples**
Works the same way as lists.

```python
coordinates = (10, 20, 30)
print(len(coordinates))  # Output: 3
```

### **4. Using `len()` with Dictionaries**
Counts the number of key-value pairs.

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
print(len(person))  # Output: 3
```

### **5. Using `len()` with Sets**
Counts the number of unique elements.

```python
unique_numbers = {1, 2, 3, 4, 5}
print(len(unique_numbers))  # Output: 5
```

### **6. Using `len()` with Nested Structures**

```python
nested_list = [[1, 2], [3, 4], [5, 6]]
print(len(nested_list))  # Output: 3 (counts the sublists, not individual elements)
```

---
`Subscripting` – To fetch one character from a string print("Hello"[0]) 
- Can use a negative indices starting from –1 to print last characters 