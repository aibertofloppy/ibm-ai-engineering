import turtle

def rectangle(width, height):
    t = turtle.Turtle()
    t.speed(1)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    turtle.done()

rectangle(80, 40)

make_turtle()
rectangle(80, 40)