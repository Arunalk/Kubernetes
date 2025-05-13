## <span style="color:#A7C7E7;">Title function</span>

The title() function in Python is a string method that capitalizes the first letter of each word in a string while converting the rest of the letters to lowercase.

```python
string.title()
Example Usage:
text = "hello world! python is awesome."
title_case = text.title()
print(title_case)  
# Output: "Hello World! Python Is Awesome."
```
`Limitations:`</br>
- It capitalizes the first letter after spaces and punctuation, but does not handle exceptions like "iPhone" or "eBay" properly.
    ```python
    text = "welcome to mcDonald's"
    print(text.title())  
    # Output: "Welcome To Mcdonald'S" (Incorrect capitalization)
    ```
