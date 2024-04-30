from turtle import *

tiger = Turtle()
tiger.speed(0)
tiger.screen.setup(800, 600)
tiger.width(2)

# Рисуем голову тигра
tiger.penup()
tiger.goto(-50, 100)
tiger.pendown()
tiger.begin_fill()
tiger.setheading(45)
tiger.circle(50, 270)
tiger.setheading(-45)
tiger.circle(50, 270)
tiger.end_fill()

tiger.screen.exitonclick()
tiger.screen.mainloop()
