def is_triangle(a, b, c):
    """Comprueba si se puede formar un triángulo."""
    if a + b < c or a + c < b or b + c < a:
        print("No")
    else:
        print("Sí")

def ask_user():
    """Pide longitudes al usuario y comprueba el triángulo."""
    a = int(input("Lado a: "))
    b = int(input("Lado b: "))
    c = int(input("Lado c: "))
    is_triangle(a, b, c)

if __name__ == "__main__":
    ask_user()