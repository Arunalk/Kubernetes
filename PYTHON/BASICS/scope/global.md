# Global Constants in Python

> In Python, constants are typically defined using **uppercase variable names** and are placed at the top of the script.

## Example of a Global Constant:

```python
PI = 3.14159  # Global constant

def calculate_circle_area(radius):
    return PI * radius * radius

print(calculate_circle_area(5))  # Output: 78.53975
```

## Best Practices for Global Constants:
- Use **uppercase names** (e.g., `MAX_SPEED`, `DATABASE_URL`).
- Define them at the **top** of the file for better readability.
- Though Python does not enforce constants, treating them as **unchangeable** by convention improves code maintainability.

> Understanding global constants is crucial for **avoiding variable conflicts** and ensuring **proper code organization**.
