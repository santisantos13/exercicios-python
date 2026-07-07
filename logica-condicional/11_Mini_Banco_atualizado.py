valor = 0
depositar = 0
saque = 0
while valor < 10:
    saldo = 0
    try:
        escolha = int(
            input(
                "Escolha uma opção \n"
                "1 - Ver saldo\n"
                "2 - Depositar\n"
                "3 - Sacar:\n"
                "4 - Sair: \n"
            )
        )

        if escolha == 1:
            print(10 * "-", "saldo", 10 * "-")
            print(f"Saldo = R${saldo:.2f}")
            print(27 * "-")

        elif escolha == 2:
            print(10 * "-", "depositar", 10 * "-")
            depositar = float(input("Valor a ser depoistado: R$"))
            confirmacao = input("Confirma? [s]im ou [n]ão: \n").lower()
            if depositar <= 0:
                print("Não é possivel depositar valor negativo ou zero")
                continue
            if confirmacao.startswith("s"):
                saldo = saldo + depositar
                print(f"Depósito de R${depositar:.2f} confirmado.")
                print(35 * "-")
            else:
                print("Depósito não confirmado.")
                print(35 * "-")
        elif escolha == 3:
            print(10 * "-", "Saque", 10 * "-")
            print(f"Saldo = R${saldo:.2f}")
            print(35 * "-")

            saque = float(input("Valor do saque: R$"))
            confirmacao = input("Confirma? [s]im ou [n]ão: \n").lower()
            if confirmacao.startswith("s"):
                saldo = saldo - saque
                print(f"Saque de R${saque:.2f} realizado com sucesso.")
                print(35 * "-")
            else:
                print("Saque não confirmado.")
                print(35 * "-")
        else:
            print("saindo...")
            print("Programa encerrado.")
            break
    except:
        print(35 * "-")
        print("Tente novamente...")
        print(35 * "-")
