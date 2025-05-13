# <span style="color:lightblue;"> IMPORTING A MODULE </span>

### `Basic import:`

```
import <module-name>
object = <module-name>.<class-name>()
```

### `from import:`

```
from <module-name> import <class-name>
object = <class-name>()
```

`Avoid writing * as it is difficult  to track where the method is coming from`
```
from <module-name> import *  
method_name()
```
---

# <span style="color:lightblue;"> Aliasing a module </span>

```
import <module-name> as t
object = t.<class-name>()
```

----
# <span style="color:lightblue;"> Installing a module </span>

- 📌 **`Why Do Some Modules Need to Be Installed While Others Can Be Imported Directly?`**

    - Some modules come `pre-installed with Python` because they are part of the Python Standard Library. You can import them directly without installing anything. 
    - While some modules are `not included` in Python by default. These are developed by third parties and must be installed separately using `pip`.

---

# <span style="color:lightblue;"> 📌 Virtual Environments in Python</span>

- A virtual environment in Python is an isolated workspace where you can install packages without affecting the global Python installation. </br>
This allows you to manage dependencies separately for different projects.