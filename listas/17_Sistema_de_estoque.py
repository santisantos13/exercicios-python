stock = []
keep_running = True


def end_program():
    print("Encerrando programa...")
    print("Programa encerrado.")


while keep_running:

    print("\n          Estoque         ")
    print("--------------------------")
    print("1 - Ver estoque\n2 - Adicionar item \n3 - Remover item \n0 - Sair")
    print("--------------------------")
    try:
        option = int(input("Escolha uma opção: "))

    except ValueError:

        print("Digite uma opção válida.")
        try:
            continuing = input("Deseja continuar? [s] ou [n]: ").lower()
            if continuing.startswith("s"):
                continue
            else:
                end_program()
                break

        except ValueError:
            end_program()
            break

    if option == 0:
        end_program()
        break

    if option == 1:
        if not stock:
            print("Estoque vazio.\nAdicione itens ao estoque para ver.")
        else:
            for i in stock:
                print(i)

    elif option == 2:
        print("--------------------------")
        print("Adicionando item ao estoque")
        print("--------------------------")
        item = input("Nome: ").capitalize()

        try:
            amount = int(input(f"Quantidade de {item}s: "))
        except ValueError:
            print("digite uma quantidade válida.")
        stock.append(item)
        stock.append(amount)
