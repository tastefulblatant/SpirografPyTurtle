from turtle import Turtle, Screen, speed
import random
import turtle

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

tommy = Turtle()
tommy.shape("turtle")
tommy.speed(20)

for number in range(36):
    tommy.pencolor(random_color())
    tommy.circle(100)
    tommy.left(10)



window = Screen()
window.exitonclick()