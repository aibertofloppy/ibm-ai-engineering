# Resumen Capítulo 5 – Condicionales y Recursión

En este capítulo pasamos de dibujar cosas bonitas con `turtle` a **pensar con lógica**.  
Aquí aparecen dos conceptos que van a ser tu pan de cada día en programación:

- **Condicionales**: decidir qué hacer según las condiciones (`if`, `elif`, `else`).  
- **Recursión**: cuando una función se llama a sí misma para resolver el problema poco a poco.

---

## Qué hemos hecho

1. **Fermat**  
   Creamos `fermat.py` para comprobar si alguien puede contradecir el famoso teorema:  
   - Pide `a, b, c, n` y evalúa si `a^n + b^n = c^n` con `n > 2`.

2. **Triángulo**  
   En `triangle.py` comprobamos si tres lados pueden formar un triángulo usando la desigualdad triangular.

3. **Torres de Hanoi**  
   En `hanoi.py` usamos recursión para resolver el clásico problema de mover discos entre tres torres sin romper las reglas.

---

## Conceptos clave

- **Expresiones booleanas** (`True`, `False`)  
- **Comparaciones** (`==`, `!=`, `<`, `>`…)  
- **Condiciones múltiples** con `and`, `or`, `not`  
- **Caso base en recursión** (parar cuando llegas al punto más simple del problema)  

---

## Ejecución rápida

Dentro de la carpeta del capítulo 5:

```bash
python fermat.py
python triangle.py
python hanoi.py