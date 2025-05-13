# 📄 Reading CSV Files in Python

## 📘 Using `readlines()`

The `readlines()` function reads all lines from a file and returns them as a list. While simple, handling CSV data this way can be cumbersome, especially for extracting specific rows or columns.:contentReference[oaicite:2]{index=2}

```python
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
```

## 📗 Using the csv Module

Python's built-in csv module provides functionality to read and write CSV files more efficiently.

```python
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temp = []
    for row in data:
        if row[2] != "temperature":
            temp.append(int(row[2]))
    print(temp)
```

## 📙 Using pandas

The pandas library offers powerful data structures and functions for data analysis, making it easier to handle CSV files.

```python
import pandas

data = pandas.read_csv("weather_data.csv")
print(data['temperature'])
```

With pandas, you can easily perform operations like selecting specific columns, filtering rows, and computing statistics without manually opening or parsing the file.