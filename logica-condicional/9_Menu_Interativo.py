while True:
    print(15 * "-", "Operações Matemáticas", 15 * "-")
    print(25 * "-", "Opções", 20 * "-")
    print("1 - Somar \n2 - Subtrair \n3 - Multiplicar \n4 - Dividir \n5 - Sair")
    print(53 * "-")

    escolha = int(input("Digite a opção desejada: "))
    num1 = 0
    num2 = 0

    if escolha == 1:
        print(53 * "-")
        print(25 * "-", "Somar", 21 * "-")
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite o número a ser somado: "))
        print(f"{num1} + {num2} = {num1 + num2}")

        continuar = input("Deseja continuar? [s]im ou [n]ão: ").lower().startswith("s")
        if continuar:
            ...
        else:
            print(53 * "-")
            break

    elif escolha == 2:
        print(53 * "-")
        print(22 * "-", "Subtrair", 21 * "-")
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite o número a ser subtraído: "))
        print(f"{num1} - {num2} = {num1 - num2}")

        continuar = input("Deseja continuar? [s]im ou [n]ão: ").lower().startswith("s")
        if continuar:
            ...
        else:
            print(53 * "-")
            break

    elif escolha == 3:
        print(53 * "-")
        print(21 * "-", "Multiplicar", 19 * "-")
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite o número a ser multiplicado: "))
        print(f"{num1} x {num2} = {num1 * num2}")

        continuar = input("Deseja continuar? [s]im ou [n]ão: ").lower().startswith("s")
        if continuar:
            ...
        else:
            print(53 * "-")
            break

    elif escolha == 4:
        print(53 * "-")
        print(22 * "-", "Dividir", 21 * "-")
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite o número a ser dividido: "))

        if num2 == 0:
            print("Nenhum número pode ser dividiro por zero...")
            continue
        else:
            print(f"{num1} / {num2} = {num1 / num2:.2f}")
            continuar = (
                input("Deseja continuar? [s]im ou [n]ão: ").lower().startswith("s")
            )
        if continuar:
            ...
        else:
            print(53 * "-")
            break

    elif escolha == 5:
        print(53 * "-")
        break
print("Programa FINALIZADO")
