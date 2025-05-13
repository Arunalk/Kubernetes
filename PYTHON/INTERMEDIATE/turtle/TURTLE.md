# 🐢 Turtle Graphics module

The `turtle module` in Python is used for drawing `graphics`, `creating animations`, and `visualizing algorithms`. It provides a simple way to control a turtle (a pen) that moves on the screen.

## 📌 Turtle Class
The turtle.Turtle() class creates and controls the turtle, which acts as a pen for drawing on the screen.

## 📌 Screen Class
The `turtle.Screen()` class creates a GUI window where turtle graphics are drawn. Without it, the turtle wouldn't have a space to move!

`Why is Screen Needed?`
- When you use turtle, it automatically creates a default window. However, if you want more control, you should explicitly create a Screen object.

`exitonclick() – Closing the Window`
- The exitonclick() function keeps the GUI open and closes it when you click anywhere inside the window.

`What is tkinter?`
tkinter (short for Tk Interface) is Python’s built-in GUI (Graphical User Interface) library. It is used to create windows, buttons, text fields, labels, menus, and other interactive GUI elements.

🔹 `Is tkinter similar to Screen in turtle?`
While both turtle.Screen() and tkinter create GUI windows, they serve different purposes:

> `turtle.Screen()` is specifically designed for drawing and animations using the turtle module. It provides a canvas where a turtle moves and draws shapes. It has limited event handling, mainly supporting basic interactions like click-to-exit and keyboard inputs.

> `tkinter.Tk()`, on the other hand, is a full-fledged GUI framework used for building applications with buttons, labels, text boxes, and other interactive elements. It offers complete event handling, allowing developers to create functional user interfaces.

- Use `turtle.Screen()` if you want to draw shapes, make animations, or create visual simulations.
- Use `tkinter.Tk()` if you need to build an application with buttons, input fields, and interactive elements.