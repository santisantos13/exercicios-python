def soma(num1, num2):
    return num1 + num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não é possível dividir por zero"
    return num1 / num2

def subtracao(num1, num2):
    return num1 - num2

def pedir_numeros():
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    return n1, n2

while True:

    print("\nAdição, Subtração, Multiplicação e Divisão")
    print("-------------------------------------------")

    operador = input("Digite um operador ou 'sair': ").lower()

    if operador in ["adição", "+", "mais", "adicao"]:

        n1, n2 = pedir_numeros()
        print(f"A soma é igual a {soma(n1, n2)}")

    elif operador in ["menos", "-", "subtração", "subtracao"]:

        n1, n2 = pedir_numeros()
        print(f"A subtração é igual a {subtracao(n1, n2)}")

    elif operador in ["vezes", "*", "multiplicação", "multiplicacao"]:

        n1, n2 = pedir_numeros()
        print(f"A multiplicação é igual a {multiplicacao(n1, n2)}")

    elif operador in ["divisao", "/", "dividir"]:

        n1, n2 = pedir_numeros()
        print(f"A divisão é igual a {divisao(n1, n2)}")

    elif operador == "sair":
        print("Programa encerrado.")
        break

    else:
        print("Digite um operador válido.")