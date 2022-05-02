#使用turtle.goto(x,y)画一个五角星

import turtle
# turtle.setup(650,350,200,200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(2)
# turtle.pencolor("red")
# turtle.seth(-40)
#
# turtle.goto(100,0)
# turtle.goto(-50,-50)
# turtle.goto(0,100)
# turtle.goto(50,-50)
# turtle.goto(-50,0)
# turtle.goto(0,0)
#
# turtle.done()
turtle.penup()
turtle.fd(-30)
turtle.pendown()
turtle.pencolor('red')
turtle.pensize(6)
for i in range(5):
    turtle.fd(150)
    turtle.right(144)
turtle.done()
