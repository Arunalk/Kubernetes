# Object State
- The state of an object refers to the values of its attributes (i.e., its data at a specific moment).

**`Each instance can have a different state:`**

```yaml
print(dog1.name)  # Buddy
print(dog2.name)  # Max
```
Both `dog1 and dog2` are instances of the Dog class, but their **states differ** because name is different.

---

## **`Example`**

### <span style="color:#A7C7E7;">🏗️ Class: The Blueprint

- Think of a class like a dog adoption form. It defines what details we care about for every dog — for example, name, breed, age, etc. But the form itself doesn’t represent any one dog — it's just the structure.

    ```yaml
    class Dog:
        def __init__(self, name):
            self.name = name
    ```
- Here, the class Dog is our blueprint. It says every dog object will have a name.

### <span style="color:#A7C7E7;">🐶 Instance: The Real Dog

- An instance is a real dog based on that blueprint. You fill in the form to create an individual dog:

    ```yaml
    dog1 = Dog("Buddy")
    dog2 = Dog("Max")
    ```
- Now:

    - dog1 is an instance of Dog with the name "Buddy"

    - dog2 is another instance of Dog with the name "Max"

- Both were created from the same class, but they are independent objects.

### <span style="color:#A7C7E7;">📦 Object State: The Dog's Current Info

- Each dog (object) has its own state, which is stored in its attributes. The name attribute is part of the object's state:

    ```yaml
    print(dog1.name)  # Output: Buddy
    print(dog2.name)  # Output: Max
    ```
- Now:

    - dog1's state is: name = "Buddy", age = 3, breed = "Labrador"

    - dog2's state is: name = "Max", age = 5, breed = "Beagle"

- Each dog is an instance of the class Dog, and each has a different state.