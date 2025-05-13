# Nested Lists within a List

A **nested list** is a list that contains other lists as its elements. This allows for hierarchical or grouped data structures.

## Example:

```python
characters = ["red", "blue", ["apple", "grapes"]]
```

Here, we have a list `characters` containing three elements:

1. The string **"red"**
2. The string **"blue"**
3. Another list **["apple", "grapes"]**, making it a nested list.

To access elements inside the nested list, we use indexing:

```python
print(characters[2][0])  # Output: apple
print(characters[2][1])  # Output: grapes
```

### Modifying a Nested List:

#### `Adding an Item`:

To add an item to the nested list:

```python
characters[2].append("cherry")
print(characters)  # Output: ["red", "blue", ["apple", "grapes", "cherry"]]
```

#### `Removing an Item`:

To remove an item from the nested list:

```python
characters[2].remove("grapes")
print(characters)  # Output: ["red", "blue", ["apple", "cherry"]]
```

#### `Other Basic Functions`:

```python
len(characters)  # Returns the number of elements in the outer list.

len(characters[2])  # Returns the number of elements in the nested list.

characters.insert(1, "red")  # Inserts "red" at index 1.

characters.pop(0)  # Removes and returns the first element of the list.
```

### `Explanation:`

```python
characters[2]  # Retrieves the nested list ["fruits"].

characters[2][0]  # Accesses the first element of the nested list

characters[2][1]  # Accesses the second element of the nested list
```

### Use Cases:


> Nested lists are useful for storing grouped data, such as tables or multi-dimensional data.
> They allow structured organization within a single list.

