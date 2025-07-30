# Resumen – Capítulo 4: Functions and Interfaces

## Conceptos clave

- **Interfaz de función**: cómo otras funciones o el usuario interactúan con ella.
- **Parámetros y argumentos**: datos que entran en la función.
- **Valores de retorno**: datos que la función devuelve al finalizar.
- **Modularidad**: dividir un problema en funciones pequeñas y combinarlas.

## Aplicación práctica
- Uso de **Turtle** para crear interfaces gráficas sencillas (dibujos).
- Creación de figuras: rectángulos, rombos, paralelogramos y composiciones (flores).
- Encadenar funciones: cada figura es una función reutilizable que puede combinarse en `test_turtle.py`.

## Ejemplo de interfaz
```python
from turtle import *

def rectangle(width, height):
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

# Llamar la función
rectangle(100, 50)
done()

