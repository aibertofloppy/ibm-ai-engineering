import turtle

# Crear una sola tortuga
t = turtle.Turtle()
t.speed(1)

# Mover tortuga sin dibujar
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Dibuja paralelogramo genérico
def parallelogram(base, side, angle):
    for _ in range(2):
        t.forward(base)
        t.left(angle)
        t.forward(side)
        t.left(180 - angle)

# Rectángulo usando parallelogram
def rectangle(width, height):
    parallelogram(width, height, 90)

# Rombo usando parallelogram
def rhombus(side, angle):
    parallelogram(side, side, angle)

# --- DIBUJAR FIGURAS SEPARADAS ---

# Dibujar rectángulo en la izquierda
move_to(-150, 0)
rectangle(100, 50)

# Dibujar rombo en la derecha
move_to(150, 0)
rhombus(80, 60)

# Mantener ventana abierta
turtle.done()