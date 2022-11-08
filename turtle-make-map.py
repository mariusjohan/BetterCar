import turtle

screen = turtle.Screen()
screen.screensize(1920, 1080)
turtle.setpos(screen.window_height/2, screen.window_width/2)

screen.onkeypress(turtle.forward(1), key='w')
screen.onkeypress(turtle.back(1), key='s')
screen.onkeypress(turtle.left(1), key='a')
screen.onkeypress(turtle.right(1), key='d')