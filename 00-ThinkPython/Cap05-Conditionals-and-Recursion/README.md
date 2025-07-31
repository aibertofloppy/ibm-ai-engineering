# Capítulo 5 – Condicionales y Recursión

Este bloque introduce dos conceptos fundamentales de la programación:

1. **Condicionales** (`if`, `elif`, `else`) para tomar decisiones en el código.  
2. **Recursión**, donde una función se llama a sí misma para resolver problemas complejos de manera sencilla.

Se aplican estos conceptos en tres ejercicios clásicos:

- Comprobación del **Teorema de Fermat**.
- Validación de la **desigualdad triangular**.
- Resolución del problema de las **Torres de Hanoi**.

---

## Archivos del proyecto

### 1. `fermat.py`
Comprueba si existe una solución que contradiga el Teorema de Fermat:
- Función `check_fermat(a, b, c, n)` → Verifica la igualdad `a^n + b^n = c^n`.
- Pide datos al usuario y muestra si “Fermat estaba equivocado”.

### 2. `triangle.py`
Determina si tres longitudes pueden formar un triángulo:
- Función `is_triangle(a, b, c)` → Usa la desigualdad triangular.
- Pide lados al usuario y devuelve “Sí” o “No”.

### 3. `hanoi.py`
Resuelve las Torres de Hanoi de forma recursiva:
- Función `move(n, source, target, spare)` → Imprime los movimientos para mover `n` discos.
- Muestra la secuencia completa para pasar los discos de una torre a otra.

---

## Conceptos aprendidos

- **Condicionales:**  
  Permiten ejecutar bloques de código solo si se cumple cierta condición.

- **Expresiones booleanas:**  
  Combinación de `and`, `or`, `not` para comprobar varias condiciones a la vez.

- **Recursión:**  
  Técnica donde una función se llama a sí misma hasta llegar a un caso base.

- **Descomposición de problemas:**  
  Resolver un problema grande dividiéndolo en pasos más simples.