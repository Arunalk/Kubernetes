## 📊 pandas: DataFrame and Series

### 🧱 DataFrame

- **DataFrame** is a two-dimensional, tabular data structure.
- It consists of rows and columns, where each column can hold data of different types (e.g., integers, strings).
- Think of it as the entire dataset you're working with.

### 🔢 Series

- **Series** is a one-dimensional labeled array capable of holding any data type.
- It represents a single column of data.
- You can think of it as a single column in a spreadsheet or a single list of values.

## 🔄 Conversions and Operations

- **DataFrame to Dictionary**: You can convert a DataFrame into a dictionary using the `to_dict()` method, which is useful for data manipulation.
- **Series to List**: A Series can be converted into a list using the `tolist()` method, making it easy to work with standard Python lists.
- **Type Checking**: You can check the type of data structures using Python's built-in `type()` function.

## 📈 Common Functions

Both DataFrames and Series support various functions to analyze data:

- **Mean**: Calculates the average of the data.
- **Median**: Finds the middle value in the data.
- **Sum**: Adds up all the values.

These functions help in summarizing and understanding your data effectively.

## 🧠 Summary

- **DataFrame**: Two-dimensional, can hold multiple columns of different types.
- **Series**: One-dimensional, represents a single column of data.
- **Conversions**: Easily convert between DataFrame and dictionary, Series and list.
- **Operations**: Perform statistical operations like mean, median, and sum on both DataFrames and Series.

Understanding these structures is fundamental for data manipulation and analysis in pandas.
