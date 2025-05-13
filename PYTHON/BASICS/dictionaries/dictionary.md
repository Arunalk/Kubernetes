# <span style="color:#A7C7E7;">Dictionaries in Python</span>

Dictionaries in Python are used to store data in key-value pairs. They are mutable, unordered collections that allow for fast data retrieval.

## **1. Creating a Dictionary**
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

## **2. Accessing Values**
### **Using Keys**
```python
print(person["name"])  # Output: Alice
```

### **Using `get()` Method**
```python
print(person.get("age"))  # Output: 25
```

## **3. Adding and Updating Entries**
```python
person["job"] = "Engineer"  # Adds a new key-value pair
person["age"] = 26  # Updates the existing key
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}
```

## **4. Removing Entries**
### **Using `del` Statement**
```python
del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 26, 'job': 'Engineer'}
```

### **Using `pop()` Method**
```python
age = person.pop("age")  # Removes 'age' and returns its value
print(age)  # Output: 26
```

## **5. Looping Through a Dictionary**
### **Loop Through Keys**
```python
for key in person:
    print(key)
```

### **Loop Through Values**
```python
for value in person.values():
    print(value)
```

### **Loop Through Key-Value Pairs**
```python
for key, value in person.items():
    print(f"{key}: {value}")
```

## **6. Checking if a Key Exists**
```python
if "name" in person:
    print("Name exists!")
```

## **7. Dictionary Length**
```python
print(len(person))  # Output: Number of key-value pairs
```

## **8. Nested Dictionaries**
```python
students = {
    "student1": {"name": "Alice", "age": 25},
    "student2": {"name": "Bob", "age": 22}
}
print(students["student1"]["name"])  # Output: Alice
```

## **9. Dictionary Methods**
### **`keys()` - Get All Keys**
```python
print(person.keys())  # Output: dict_keys(['name', 'job'])
```

### **`values()` - Get All Values**
```python
print(person.values())  # Output: dict_values(['Alice', 'Engineer'])
```

### **`items()` - Get All Key-Value Pairs**
```python
print(person.items())  # Output: dict_items([('name', 'Alice'), ('job', 'Engineer')])
```

### **`clear()` - Remove All Items**
```python
person.clear()
print(person)  # Output: {}
```
---

## **2. Why Are Quotes Necessary for Keys and String Values?**

### **Keys Must Be Valid Identifiers or Strings**
- String keys must be enclosed in quotes to differentiate them from variable names.
- Without quotes, Python will interpret the key as a variable name, causing an error if it is undefined.
