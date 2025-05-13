# <span style="color:#A7C7E7;">Input function</span>

- The `input()` function in Python is used to take user input from the keyboard. It always returns the input as a string.

### 1. `Using `input()` for User Input`

### `Basic Usage`
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

### **`Taking Numeric Input`**
Since `input()` returns a string, you need to convert it to an integer or float when dealing with numbers.

#### **Example: Taking Integer Input**
```python
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
```

#### **Example: Taking Float Input**
```python
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")
```

### **`Taking Multiple Inputs`**
You can use `split()` to take multiple inputs at once.

#### **Example: Taking Two Numbers as Input**
```python
num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
print(f"Sum: {num1 + num2}")
```
> split method splits the string into a list based on spaces
> map is used for conevrting them to integers.



