# <span style="color:teal;">✂️ Slicing in Python</span>

**Slicing** is a technique used to extract a portion (subsequence) from sequences like lists, strings, or tuples using a specific syntax.

---

## ✅ Slicing in Lists

- Lists are mutable sequences. You can slice them to get a new sublist:

### 🔹 Syntax

```python
sequence[start:stop:step]
```
`start`: index to begin slicing (inclusive)  
`stop`: index to end slicing (exclusive)  
`step`: interval between elements (optional)  

## ✅ Examples
```yaml  
my_list[1:4] → elements at index 1, 2, 3  
my_string[:5] → first 5 characters  
numbers[::2] → every second element  
items[::-1] → reversed list  
```
---

## ✅ Slicing in Tuples

- Tuples are immutable sequences. You can slice them the same way, but you can't modify the result.

## ✅ Examples
```yaml 
my_tuple = (1, 2, 3, 4, 5)
my_tuple[1:4]      # (2, 3, 4)
my_tuple[::-1]     # (5, 4, 3, 2, 1)
```

## 🧠 Notes  
- Negative indices count from the end.  
- Omitting start or stop uses the beginning or end by default.  
- The original sequence is not modified; slicing returns a new object.  

## 📌 Common Use Cases  
- Extract substrings  
- Reverse sequences  
- Select every Nth item  
- Trim lists or strings  