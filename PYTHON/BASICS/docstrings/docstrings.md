# Docstrings in Python

A **docstring** is a special kind of string used to document a function, class, or module. It provides **helpful information** about what the function does, its parameters, and its return value.

## Syntax:

```python
def function_name():
    """This is a docstring that describes the function."""
    return value
```

## Example Usage:

```python
def add(a, b):
    """Returns the sum of two numbers.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of a and b.
    """
    return a + b

print(help(add))  # Displays the docstring for the function
```

### Key Points:

- Docstrings are enclosed in `"""triple quotes"""`.
- They **describe the function’s purpose, parameters, and return values**.
- The `help(function_name)` command prints the function’s docstring.
- Docstrings are useful for **documentation and readability**.

Using docstrings makes your code **more understandable and maintainable** by providing built-in documentation.

