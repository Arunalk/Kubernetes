from turtle import Turtle, Screen
s1 = Screen()
t1 = Turtle()
colors = ["dark olive green", "navy", "light coral", "pale turquoise", "brown", "purple", "pale violet red", "dark slate gray"]
def find_angle(sides):
    return 360 / sides
for i in range(3, 11):
    angle = find_angle(i)
    for j in range(0, i):
        t1.color(colors[i-3])
        t1.right(angle)
        t1.forward(100)

s1.exitonclick()



