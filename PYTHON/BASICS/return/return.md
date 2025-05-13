## <span style="color:#A7C7E7;">Return Statements</span>

- The `return` statement in Python is used inside a function to **send a value back to the caller**. It allows a function to produce an output that can be used elsewhere in the program.

### `Syntax:`

```python
def function_name():
    return value
```

### `Example Usage:`

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

### `Key Points:`

- A function **stops execution** when it reaches a `return` statement.
- If no `return` is provided, the function returns `None` by default.
- `return` can send multiple values as a tuple.

    ```python
    def operations(a, b):
        return a + b, a - b, a * b, a / b

    results = operations(10, 5)
    print(results)  # Output: (15, 5, 50, 2.0)
    ```

### Using `return` to Exit a Loop

The `return` statement can also be used to exit a loop early when a specific condition is met:

```python
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num  # Exits the loop and function immediately
    return None  # If no even number is found

nums = [1, 3, 7, 8, 9]
result = find_first_even(nums)
print(result)  # Output: 8
```

In this example, the function returns the first even number it encounters, **immediately exiting the loop** when a match is found.

> Using `return` makes functions **reusable and modular**, improving code efficiency.

