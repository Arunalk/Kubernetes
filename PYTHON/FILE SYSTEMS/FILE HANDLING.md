# 📂 Python File Handling

Python provides several ways to interact with files. A intro to reading, writing, and managing files safely.

---

## 📖 Opening a File

```python
file = open("filename.txt", "mode")
```

When opening a file in Python, you can specify the **mode** — which determines how the file will be accessed.

## 🔑 Mode

- `"mode"`: the file access mode.
- Default is `'r'` (read).

## 📋 Common Modes

| Mode | Description                              |
|------|------------------------------------------|
| `r`  | Read (default, file must exist)          |
| `w`  | Write (creates or overwrites file)       |
| `a`  | Append (adds to end of file)             |
| `x`  | Create (fails if file already exists)    |
| `b`  | Binary mode (e.g., `'rb'`, `'wb'`)       |
| `+`  | Read and write mode (e.g., `'r+'`)       |


## 🧾 Reading a File

```python3
file = open("file.txt", "r")
contents = file.read()
file.close()
```
- Always call file.close() to free system resources.

- Think of open files like browser tabs — too many open can slow down performance.

## ✅ Using with to Manage Files (Recommended)

```python3
with open("file.txt", "r") as file:
    contents = file.read()
```

## ✍ Writing to a File

Overwrite with 'w' Mode:

```python3
with open("file.txt", "w") as file:
    file.write("Hello, world!")
```
- If the file exists, it will be overwritten.

## Append with 'a' Mode:

```python3
with open("file.txt", "a") as file:
    file.write("\nMore text")
```
- Adds text to the end of the file without deleting existing content.

For example if you go to ../INTERMEDIATE/OOP/snake-game/scoreboard.py and see how we are mainting high score data.
