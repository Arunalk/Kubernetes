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

#### ✅ **Correct (String Keys)**
```python
fav_characters = {"Acotar": "Rhysand", "HP": "Harry Potter"}
```

#### ❌ **Incorrect (Missing Quotes)**
```python
fav_characters = {Acotar: "Rhysand", HP: "Harry Potter"}  
# NameError: name 'Acotar' is not defined
```

### **Numeric and Boolean Keys Don’t Need Quotes**
- If a key is an integer or boolean, you don’t need quotes.
```python
data = {1: "One", 2: "Two", True: "Yes", False: "No"}
print(data[1])  # Output: "One"
print(data[True])  # Output: "Yes"
```

### **Values Must Be Enclosed in Quotes If They Are Strings**
- If the value is a string, it must be enclosed in quotes.
- If the value is a number, boolean, or another object, quotes are not needed.

#### ✅ **Correct**
```python
fav_characters = {"Acotar": "Rhysand", "HP": 7, "Magic": True}
```

#### ❌ **Incorrect**
```python
fav_characters = {"Acotar": Rhysand}  # NameError: name 'Rhysand' is not defined
```

### **Quotes Help Differentiate String Keys from Variable Names**
Python needs quotes to distinguish between a string key and a variable name.

#### ✅ **Using a String Key**
```python
fav_characters = {"name": "Alice"}
print(fav_characters["name"])  # Output: Alice
```

#### ❌ **Using a Variable as a Key (Without Defining It)**
```python
fav_characters = {name: "Alice"}  
# NameError: name 'name' is not defined
```

### **`Conclusion`**
> - **Strings (keys & values) → Must be wrapped in single `' '` or double `" "` quotes.**
> - **Numbers, Booleans, or other objects → Do not need quotes.**
> - **Quotes prevent Python from misinterpreting a string as a variable name.**

---