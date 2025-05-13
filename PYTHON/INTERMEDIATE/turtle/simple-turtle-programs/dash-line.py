from turtle import Turtle, Screen

t1 = Turtle()
s1 = Screen()
i = 0
while i in range(2):
    j=0
    while j in range(10):
        t1.shape('arrow')
        t1.up()
        t1.forward(10)
        t1.down()
        t1.forward(10)
        j+=1
    i +=1
    t1.up()
    t1.forward(30)
s1.exitonclick()