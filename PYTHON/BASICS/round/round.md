# <span style="color:#A7C7E7;">Round function</span>

The `round()` function in Python is used to round a floating-point number to a specified number of decimal places. If no decimal places are specified, it rounds to the nearest integer.

## **1. Basic Usage of `round()`**
```python
print(round(3.6))   # Output: 4
print(round(3.4))   # Output: 3
```

## **2. Rounding to a Specific Number of Decimal Places**
```python
print(round(3.14159, 2))  # Output: 3.14
print(round(2.71828, 3))  # Output: 2.718
```

## **3. Rounding Negative Numbers**
```python
print(round(-3.6))   # Output: -4
print(round(-3.4))   # Output: -3
```

## **4. Rounding to the Nearest Multiple of 10**
```python
print(round(125, -1))  # Output: 130
print(round(146, -2))  # Output: 100
```

## **5. Using `round()` with Division Results**
```python
result = 10 / 3
print(round(result, 2))  # Output: 3.33
```

## **6. Rounding in a List Using List Comprehension**
```python
numbers = [1.235, 2.456, 3.678]
rounded_numbers = [round(num, 2) for num in numbers]
print(rounded_numbers)  # Output: [1.24, 2.46, 3.68]
```