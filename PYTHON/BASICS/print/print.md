## <span style="color:#A7C7E7;">Print</span>

The print() function is used to display output to the console

### `Printing Different Data Types in Python`

#### 1. `Printing Strings`
```python
print("Hello, World!")
print('Python is fun!')
```
- String manipulation: 
    - Can print multiple statements using a single print statement using "\n" 

- String Concatenation 
    - Concatenate the string print("string1" + "string2") -> without space 
    - If we wanted space print("string1" + "" + "string2") 

#### 2. `Printing Integers`
```python
age = 25
print(age)
print("My age is", age)
```

#### 3. `Printing Floats (Decimal Numbers)`
```python
pi = 3.14159
print(pi)
print("The value of pi is", pi)
```

#### 4. `Printing Boolean Values`
```python
is_python_fun = True
print(is_python_fun)
print("Is Python fun?", is_python_fun)
```

#### 5. `Printing Lists`
```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits)
print("My favorite fruits are:", fruits)
```

#### 6. `Printing Tuples`
```python
coordinates = (10, 20)
print(coordinates)
print("X and Y coordinates:", coordinates)
```

#### 7. `Printing Dictionaries`
```python
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)
print("Person details:", person)
print("Person details:", person['name']) # To fetch the value of 'name'
```

#### 8. `Printing Sets`
```python
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
print("Unique numbers:", unique_numbers)
```

#### 9. `Printing Multiple Values in One `print()` Statement`
```python
name = "Bob"
age = 30
height = 5.9
print("Name:", name, "| Age:", age, "| Height:", height)
```

#### 10. `Using `f-strings` for Better Formatting`
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

#### 11. `To join list of strings`

```python
display = ['H', 'e', 'l', 'l', 'o']
print(''.join(display))
```