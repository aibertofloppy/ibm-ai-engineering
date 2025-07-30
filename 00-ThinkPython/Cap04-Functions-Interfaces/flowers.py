import turtle
import math

def arc(radius, angle):
    # Dibuja un arco con aproximación por pequeños segmentos
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    steps = int(arc_length / 4) + 1  # Cuantos segmentos pequeños
    step_length = arc_length / steps
    step_angle = angle / steps

    for _ in range(steps):
        turtle.forward(step_length)
        turtle.left(step_angle)

def petal(radius, angle):
    # Un pétalo: dos arcos simétricos
    for _ in range(2):
        arc(radius, angle)
        turtle.left(180 - angle)

def flower(petals, radius, angle):
    # Dibuja la flor repitiendo pétalos
    for _ in range(petals):
        petal(radius, angle)
        turtle.left(360 / petals)

# --- Ejemplo: dibujar dos flores ---
turtle.speed(0)  # Máxima velocidad

# Primera flor
flower(7, 60, 60)
turtle.penup()
turtle.goto(200, 0)  # Mover a la derecha
turtle.pendown()

# Segunda flor
flower(10, 80, 80)

turtle.done()