## `Nested lists within a dictionary`

### **Removing an Element from a List Inside a Dictionary**
To remove an element from a list stored inside a dictionary, you can use different methods:

#### **1. Using `.remove(value)` (Removes by Value)**
```python
# Dictionary with lists as values
data = {
    "fruits": ["apple", "banana", "cherry", "date"]
}

# Remove "banana" from the list
data["fruits"].remove("banana")
print(data["fruits"])  
# Output: ['apple', 'cherry', 'date']

```

#### **2. Using `pop(index)` (Removes by Index)**
```python
# Remove the item at index 1
data["fruits"].pop(1)
print(data["fruits"])  
# Output: ['apple', 'cherry', 'date']
```

#### **3. Using `del` (Deletes by Index)**
```python
# Delete the item at index 2
del data["fruits"][2]
print(data["fruits"])  
# Output: ['apple', 'cherry']
```

#### **4. Removing the Entire Key (`pop` for Dictionaries)**
If you want to remove "fruits" entirely from the dictionary:
```python
# Remove the "fruits" key and its associated list
removed_items = data.pop("fruits")
print(removed_items)  
# Output: ['apple', 'cherry']
```

#### **5. Using List Comprehension – Removes All Occurrences of a Value

This method creates a new list excluding all occurrences of the specified value.

```python3
# Add "banana" back to the list for demonstration
data["fruits"] = ["apple", "banana", "cherry", "banana", "date"]

# Remove all occurrences of "banana"
data["fruits"] = [fruit for fruit in data["fruits"] if fruit != "banana"]
print(data["fruits"])  
# Output: ['apple', 'cherry', 'date']
```

#### 6. Using .clear() – Removes All Elements from the List

This method removes all items from the list, leaving it empty.

```python3
# Clear all items from the list
data["fruits"].clear()
print(data["fruits"])  
# Output: []
```