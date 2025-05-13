## <span style="color:#A7C7E7;">Try and Except in Python</span>

The `try` and `except` blocks in Python are used for **handling errors** gracefully, preventing programs from crashing due to unexpected issues.

## `Syntax`:

```python
try:
    # Code that may raise an exception
    risky_operation()
except ExceptionType:
    # Handle the error
    print("An error occurred")
```

##  Example Usage`:

```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
```

### `How It Works`:
- The **`try` block** contains code that may raise an exception.
- If an exception occurs, the **`except` block** handles it instead of stopping the program.

## `Handling Multiple Exceptions`:

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

### `Using a Generic Exception:`
If you don’t know the exact error type, you can catch all exceptions:

```python
try:
    risky_code()
except Exception as e:
    print(f"An error occurred: {e}")
```

> Using `try-except` ensures programs **handle errors smoothly** and **continue execution** instead of abruptly stopping.