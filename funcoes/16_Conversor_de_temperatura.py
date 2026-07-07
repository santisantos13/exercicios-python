def celsius_para_fahrenheit(celsius):
    f = (celsius * 9 / 5) + 32
    print(f"{celsius:.2f}Cº equivale a {f:.2f}Fº\n")


def fahrenheit_para_celsius(f):
    celsius = (f - 32) * 5 / 9
    print(f"{f:.2f}Fº equivale a {celsius:.2f}Cº\n")


def continuar_programa():
    resposta = input("Deseja continuar? [S] ou [N]\n").upper()
    return resposta


while True:

    print("----------- Conversor de Temperatura -----------")
    print("1 - Celsius para fahrenheit")
    print("2 - Fahrenheit para celsius")
    print("3 - Sair\n")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Escolha uma opção válida.\n")

    else:
        if opcao == 1:
            print("------------------ Célsius ------------------\n")
            try:
                celsius = float(input("Digite a temperatura em Cº: "))
            except ValueError:
                print("Digite apenas números...")

            else:
                celsius_para_fahrenheit(celsius)

                if continuar_programa().startswith("S"):
                    continue
                else:
                    print("Encerrando.")
                    break

        elif opcao == 2:
            print("---------------- Fahrenheit ----------------\n")
            try:
                f = float(input("Digite a temperatura em Fº: "))
            except ValueError:
                print("Digite apenas números...")
            else:

                fahrenheit_para_celsius(f)

                if continuar_programa().startswith("S"):
                    continue
                else:
                    print("Encerrando.")
                    break

        elif opcao == 3:
            print("Encerrando programa....")
            break

        else:
            print("Opção inválida...")
