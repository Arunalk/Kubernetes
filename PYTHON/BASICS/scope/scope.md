# <span style="color:#A7C7E7;"> Scope in Python</span>

- Scope in Python refers to the **region of a program where a variable is accessible**. There are four types of scopes in Python:

## `Types of Scope:`

1. **`Local Scope`** - Variables declared inside a function are only accessible within that function.
2. **`Enclosing Scope`** - Variables in an outer function are accessible in inner (nested) functions.
3. **`Global Scope`** - Variables declared outside functions are accessible throughout the program.
4. **`Built-in Scope`** - Python’s predefined names, such as `print()` and `len()`.

`Block Scope in Python:`

- Unlike some languages, Python does not have block scope. Variables defined inside if, for, or while blocks remain accessible outside them.

```python
if True:
    a = 10  # This variable is still accessible outside the block

print(a)  # Output: 10
```
> However, inside functions, the scope is local:

```python
def test():
    if True:
        b = 20
    print(b)  # Works because `b` is defined in the function scope

test()
```


## Example Usage:

```python
x = 10  # Global variable

def outer_function():
    y = 20  # Enclosing variable
    
    def inner_function():
        z = 30  # Local variable
        print(f"Local: {z}, Enclosing: {y}, Global: {x}")
    
    inner_function()

outer_function()
```

### `Key Points`:

- `Local variables exist only inside a function` and cannot be accessed outside it.
- `Global variables are accessible throughout the program`, but modifying them inside a function requires the `global` keyword.
- `Enclosing scope applies to nested functions where inner functions` can access outer function variables.
- `Built-in scope consists of Python's reserved keywords` and functions.

## Modifying Global Variables:

```python
global_var = 5

def modify_global():
    global global_var  # Declaring that we want to modify the global variable
    global_var = 10

modify_global()
print(global_var)  # Output: 10
```

### `Does a Global Variable Get Overridden If `global` Is Not Used?`

- No, if `global` is **not used**, the variable inside the function will be treated as a **local variable**, and the global variable **will not be overridden**.

### Example Without `global`:

```python
global_var = 5  # Global variable

def modify_global():
    global_var = 10  # This creates a new local variable inside the function
    print(global_var)  # Output: 10 (local scope)

modify_global()
print(global_var)  # Output: 5 (global scope remains unchanged)
```

- Here, `global_var = 10` inside the function creates a **new local variable** instead of modifying the global one.
- The global `global_var` **remains unchanged**.

### Example With `global`:

```python
global_var = 5

def modify_global():
    global global_var  # Now, we are modifying the global variable
    global_var = 10

modify_global()
print(global_var)  # Output: 10 (global variable updated)
```

- Using `global` ensures that the function modifies the **existing global variable** instead of creating a new local one.

> Understanding scope is crucial for **avoiding variable conflicts** and ensuring **proper code organization**.

