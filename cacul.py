def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro impossible."
    return a / b

def exposant(a, b):
    return a ** b


def calculer(expression):
    elements = expression.split()

    resultat = float(elements[0])
    i = 1

    while i < len(elements):
        operation = elements[i]
        nombre = float(elements[i + 1])

        if operation == '+':
            resultat = addition(resultat, nombre)

        elif operation == '-':
            resultat = soustraction(resultat, nombre)

        elif operation == 'x' or operation == '*':
            resultat = multiplication(resultat, nombre)

        elif operation == '÷' or operation == '/':
            resultat = division(resultat, nombre)

        elif operation == '^':
            resultat = exposant(resultat, nombre)

        else:
            return "Opération invalide."

        i += 2

    return resultat


print("=== CALCULATRICE ===")
print("Exemple : 10 + 5 x 3 - 2")
print("Tapez '=' pour quitter.")

while True:
    expression = input("\nCalcul : ")

    if expression == "=":
        print("Au revoir !")
        break

    resultat = calculer(expression)
    print("Total =", resultat)