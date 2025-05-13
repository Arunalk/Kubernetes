# <span style="color:lightblue;"> TUPLE </span>

- Similar to lists, but surrounded by `()`.  
- It is **ordered** and **immutable** (cannot be changed after creation).  

### **📌 `Difference Between Lists and Tuples in Python`**  

| Feature          | List (`list`)        | Tuple (`tuple`)        |
|-----------------|---------------------|-----------------------|
| **`Mutability`**  | ✅ Mutable (Can be changed) | ❌ Immutable (Cannot be changed) |
| **`Syntax`**      | `[]` (Square brackets) | `()` (Parentheses) |
| **`Memory Usage`** | ❌ More memory (because it's dynamic) | ✅ Less memory (optimized) |

#### **`Mutability Example`**
```python
# List (Mutable)
my_list = [1, 2, 3]
my_list[0] = 10  # ✅ Allowed
print(my_list)  # Output: [10, 2, 3]

# Tuple (Immutable)
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # ❌ TypeError: 'tuple' object does not support item assignment
```