def print_move(fr, to):
    print(f"Mover de {fr} a {to}")

def move(n, source, target, spare):
    """Resuelve Torres de Hanoi recursivamente."""
    if n == 1:
        print_move(source, target)
    else:
        move(n-1, source, spare, target)
        print_move(source, target)
        move(n-1, spare, target, source)

if __name__ == "__main__":
    # Ejemplo con 3 discos
    move(3, 'A', 'C', 'B')