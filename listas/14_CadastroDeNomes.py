nomes = []


def cadastro():
    nome = input("Digite um nome: ").capitalize()
    nome_verificado = nome.isalpha()

    if nome_verificado == False:
        print("Digite apenas nomes...")

    else:
        print(f"{nome} cadastrado com sucesso!✅")
        nomes.append(nome)


def listar_nomes():
    if not nomes:
        print("Nenhum nome cadastrado.")
    else:
        indice = 0

        for nome in nomes:
            indice += 1
            print(indice, nome)


def remover_nome():
    if not nomes:
        print("Não foi possível realizar a tarefa.")
        print("Nenhum nome foi cadastrado.")

    else:
        print(nomes)

        nome_removido = input("Qual nome deseja remover?: ").capitalize()

        if nome_removido not in nomes:
            print(f"{nome_removido} não está na lista.")
        else:
            nomes.remove(nome_removido)
            print(nomes)


while True:
    print("---------------------------- MENU ----------------------------")
    print("1 - Cadastrar | 2 - Listar nomes | 3 - Remover Nome | 4 - Sair")

    try:  # Validação de erro caso o valor digitado não seja um número int
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite uma opção válida (1,2,3 ou 4)")
        print("Reiniciando...")
        continue

    if opcao == 1:
        cadastro()

    elif opcao == 2:
        listar_nomes()

    elif opcao == 3:
        remover_nome()

    elif opcao == 4:
        print("Encerrando programa...")
        break
