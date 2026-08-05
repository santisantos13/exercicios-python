def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def potenciation(num1, num2):
    return num1**num2


numeros = [1, 2, 3, 4, 5]
division = [divide(numero, 2) for numero in numeros]
multiplicacion = [multiply(numero, 2) for numero in numeros]
square = [potenciation(numero, 2) for numero in numeros]

print(numeros)
print(division)
print(multiplicacion)
print(square)
