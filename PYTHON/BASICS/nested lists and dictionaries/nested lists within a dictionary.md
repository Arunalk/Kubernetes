## `Nested lists within a dictionary`

### **Removing an Element from a List Inside a Dictionary**
To remove an element from a list stored inside a dictionary, you can use different methods:

#### **1. Using `.remove(value)` (Removes by Value)**
```python
fav_characters = {
    "Acotar": ["Rhys", "Azriel", "Cassian", "Feyre", "Suriel"]
}

fav_characters["Acotar"].remove("Suriel")  # Removes "Suriel" from the list
print(fav_characters["Acotar"])  
# Output: ['Rhys', 'Azriel', 'Cassian', 'Feyre']
```

#### **2. Using `pop(index)` (Removes by Index)**
```python
fav_characters["Acotar"].pop(4)  # Removes the element at index 4 ("Suriel")
print(fav_characters["Acotar"])  
# Output: ['Rhys', 'Azriel', 'Cassian', 'Feyre']
```

#### **3. Using `del` (Deletes by Index)**
```python
del fav_characters["Acotar"][4]  # Deletes "Suriel" at index 4
print(fav_characters["Acotar"])  
# Output: ['Rhys', 'Azriel', 'Cassian', 'Feyre']
```

#### **4. Removing the Entire Key (`pop` for Dictionaries)**
If you want to remove "Acotar" entirely from the dictionary:
```python
fav_characters.pop("Acotar")  
print(fav_characters)  
# "Acotar" key is removed from the dictionary
```