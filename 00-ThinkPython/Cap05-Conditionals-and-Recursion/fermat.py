def check_fermat(a, b, c, n):
    """Comprueba si a^n + b^n = c^n para n > 2 (Teorema de Fermat)."""
    if n > 2 and a**n + b**n == c**n:
        print("¡Santo cielo, Fermat estaba equivocado!")
    else:
        print("No, eso no funciona.")

def ask_user():
    """Pide valores al usuario y llama a check_fermat."""
    a = int(input("Introduce a: "))
    b = int(input("Introduce b: "))
    c = int(input("Introduce c: "))
    n = int(input("Introduce n: "))
    check_fermat(a, b, c, n)

if __name__ == "__main__":
    ask_user()