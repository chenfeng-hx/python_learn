# import turtle
# def koch(size,n):
#     if n == 0:
#         turtle.fd(size)
#     else:
#         for angle in [0,60,-120,60]:
#             turtle.left(angle)
#             koch(size/3,n-1)
# def main():
#     turtle.setup(800,400)
#     turtle.speed(0)    # 控制绘制速度
#     turtle.penup()
#     turtle.goto(-350,-50)
#     turtle.pendown()
#     turtle.pensize(2)
#     koch(600,3)       # 0 阶科赫曲线长度，阶数
#     turtle.hideturtle()
#     turtle.done()
# main()

# 雪花
import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    leval = 5
    koch(400,leval)
    turtle.right(120)
    koch(400,leval)
    turtle.right(120)
    koch(400,leval)
    turtle.hideturtle()
    turtle.done()
main()