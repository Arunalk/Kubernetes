# Nested Lists within a List

A **nested list** is a list that contains other lists as its elements. This allows for hierarchical or grouped data structures.

## Example:

```python
characters = ["lance", "blue", ["rhys", "azriel"]]
```

Here, we have a list `characters` containing three elements:

1. The string **"lance"**
2. The string **"blue"**
3. Another list **["rhys", "azriel"]**, making it a nested list.

To access elements inside the nested list, we use indexing:

```python
print(characters[2][0])  # Output: rhys
print(characters[2][1])  # Output: azriel
```

### Modifying a Nested List:

#### `Adding an Item`:

To add an item to the nested list:

```python
characters[2].append("cassian")
print(characters)  # Output: ['lance', 'blue', ['rhys', 'azriel', 'cassian']]
```

#### `Removing an Item`:

To remove an item from the nested list:

```python
characters[2].remove("azriel")
print(characters)  # Output: ['lance', 'blue', ['rhys', 'cassian']]
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
characters[2]  # Retrieves the nested list ["rhys", "azriel"].

characters[2][0]  # Accesses the first element of the nested list, "rhys".

characters[2][1]  # Accesses the second element of the nested list, "azriel".
```

### Use Cases:


> Nested lists are useful for storing grouped data, such as tables or multi-dimensional data.
> They allow structured organization within a single list.

