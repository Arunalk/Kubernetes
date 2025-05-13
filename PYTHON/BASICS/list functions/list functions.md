# <span style="color:#A7C7E7;">List Functions in Python</span>

Python provides various built-in functions to manipulate lists efficiently.

#### **1. `append()` - Add an Element to the End of the List**
```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]
```

#### **2. `extend()` - Extend the List with Another List**
```python
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
```

#### **3. `insert()` - Insert an Element at a Specific Index**
```python
numbers = [1, 2, 4]
numbers.insert(2, 3)  # Inserts 3 at index 2
print(numbers)  # Output: [1, 2, 3, 4]
```

### **4. `remove()` - Remove the First Occurrence of a Value**
Cannot provide index here
```python
numbers = [1, 2, 3, 2]
numbers.remove(2)  # Removes the first occurrence of 2
print(numbers)  # Output: [1, 3, 2]
```

### **5. `pop()` - Remove and Return an Element by Index**
```python
numbers = [1, 2, 3]
removed_element = numbers.pop(1)  # Removes element at index 1
print(numbers)  # Output: [1, 3]
print(removed_element)  # Output: 2
```

### **6. `index()` - Find the Index of the First Occurrence of a Value**
```python
numbers = [10, 20, 30, 40]
print(numbers.index(30))  # Output: 2
```

### **7. `count()` - Count the Occurrences of a Value**
```python
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.count(2))  # Output: 3
```

### **8. `sort()` - Sort the List in Ascending Order**
```python
numbers = [4, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 4, 9]
```

#### **Sorting in Descending Order**
```python
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 4, 2, 1]
```

### **9. `sorted()` - Return a New Sorted List Without Modifying the Original**
```python
numbers = [4, 2, 9, 1]
new_numbers = sorted(numbers)
print(new_numbers)  # Output: [1, 2, 4, 9]
print(numbers)  # Output: [4, 2, 9, 1] (original list remains unchanged)
```

### **10. `reverse()` - Reverse the Order of the List**
```python
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)  # Output: [4, 3, 2, 1]
```

### **11. `copy()` - Create a Copy of the List**
```python
numbers = [1, 2, 3]
new_numbers = numbers.copy()
print(new_numbers)  # Output: [1, 2, 3]
```

### **12. `clear()` - Remove All Elements from the List**
```python
numbers = [1, 2, 3]
numbers.clear()
print(numbers)  # Output: []
```

