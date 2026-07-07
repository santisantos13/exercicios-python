saldo = 0
deposito = 0
saque = 0
confirmacao = ""
# Aqui criei variáveis base, para não criar váriaveis dentro dos blocos (while / try)

while True:  # loop que mantém o programa funcionado
    try:
        print(50 * "-")
        print("Opções Bancárias")
        print(
            "1 - Ver saldo\n" "2 - Depositar\n" "3 - Sacar\n" "4 - Sair"
        )  # Mostra as escolhas possíveis
        escolha = int(
            input("Escolha uma opção: ")
        )  # defino a váriavel com o valor inteiro q o usuário decidir

        if (
            escolha == 1
        ):  # Condição mais simples do programa, caso seja a opção 1. O programa mostra o saldo.
            print(50 * "-")
            print(f"Saldo atual: R${saldo:.2f}")
            print(50 * "-")

        elif escolha == 2:  # Opção de depósito.
            print(20 * "-", "Depósito", 20 * "-")
            deposito = float(input("Valor a ser depositado: R$"))
            if (
                deposito <= 0
            ):  # Um tratamento de erro, caso o usuário tente depositar um valor negativo ou zero,
                # será emitida uma mensagem de erro
                print("Digite um valor válido...")
                continue
            else:
                print(
                    50 * "-"
                )  # Caso o usuário digite um valor positivo, o programa pede uma confirmação...
                confirmacao = (
                    input("Confirmar depósito? [s]im ou [n]ão: ")
                    .lower()  # Converte oq o usuário digitar para minúsculo;
                    .startswith(
                        "s"
                    )  # Checa se o que o usuário digitou começa com a letra s, ex: sim
                )

                if confirmacao:
                    saldo += deposito  # Caso o usuário confirme, o saldo anterior recebe o valor q o usuário escolheu
                    print("Realizando depósito...")  # somado ao valor anterior.
                    print(50 * "-")
                    print(f"Novo saldo : R${saldo:.2f}")
                    print(50 * "-")

                elif (
                    not confirmacao
                ):  # Caso o usuário cancele, é emitida uma mensagem de cancelamento...
                    print(50 * "-")
                    print("Depósito cancelado!")
                    continue

        elif escolha == 3:  # Opção de saque
            print(22 * "-", "Saque", 23 * "-")
            print(f"Saldo atual: R${saldo:.2f}")

            saque = float(input("Digite a quantia a ser sacada: R$"))

            # Valida valor
            if saque <= 0:
                print("Digite um valor válido...")
                continue

            # Valida saldo
            if saque > saldo:
                print("Saldo insuficiente.")
                continue

            # Confirma operação
            confirmacao = (
                input("Confirmar saque? [s]im ou [n]ão: ").lower().startswith("s")
            )

            if confirmacao:
                saldo -= saque
                print("Realizando saque...")
                print(50 * "-")
                print(f"Novo saldo: R${saldo:.2f}")
                print(50 * "-")

            else:
                print(50 * "-")
                print("Saque cancelado.")

        elif escolha == 4:
            print(50 * "-")
            print("Fechando banco...")
            break
        else:
            print(50 * "-")
            print("Opção inválida")
    except ValueError:
        print("Digite uma opção válida")


print("Programa encerrado...")
