produtos = [
    {
        "Nome": "Carro",
        "Preço": 10000,
        "Quantidade": 1,
    },
]
opcoes = {
    1: "listar",
    2: "Cadastrar",
    3: "Buscar",
    0: "Sair",
}


def buscar_produto():
    print("\n~ Buscando Produto ~\n")

    nome_buscado = input("Nome: ").capitalize()

    for produto in produtos:

        if nome_buscado == produto["Nome"]:

            print(f"{nome_buscado} já possui cadastro!✅\n")
            print(
                "⬇️ Ações\n"
                f"1 - Excluir {nome_buscado}\n"
                "2 - Alterar Preço\n"
                "3 - Alterar Quantidade\n"
                "4 - Voltar "
            )

            try:
                acao_do_usuario = int(input("Escolha uma opção: "))
            except (ValueError, NameError):
                print("Ação inválida❌")
                return

            if acao_do_usuario == 4:
                print("Voltando para a página principal...🔙\n")
                return

            elif acao_do_usuario == 1:
                confirmacao = input(
                    f"Quer mesmo excluir {nome_buscado}? Sim[1] | Não[2]\n:"
                ).upper()

                if confirmacao.startswith("S") or confirmacao == "1":
                    produtos.remove(produto)
                    print(f"{nome_buscado} excluído com sucesso.🗑️")
                else:
                    print(f"Cancelando exclusão de {nome_buscado}.")
                    print("Voltando ao menu principal.🔙")

                return

            elif acao_do_usuario == 2:
                print(f"Alterando o preço de {nome_buscado}")
                print(f"Preço antigo : R${produto['Preço']:.2f}")

                try:
                    novo_preco = float(input("Novo preço: "))
                except ValueError:
                    print("Digite um valor válido.❌")
                    return

                confirmacao = input(
                    f"Confirma a troca de preço de {nome_buscado}\n"
                    f"de R${produto['Preço']:.2f} para R${novo_preco:.2f}\n"
                    "? Sim[1] | Não[2]: "
                ).upper()

                if confirmacao.startswith("S") or confirmacao == "1":
                    produto["Preço"] = novo_preco
                    print(
                        f"Preço de {nome_buscado} alterado para R${novo_preco:.2f}✅\n"
                    )
                else:
                    print("Cancelando troca de preço.")
                    print("Voltando ao menu principal.🔙")

                return

            elif acao_do_usuario == 3:
                print(f"Alterando a quantidade de {nome_buscado}")
                print(f"Quantidade antiga {produto['Quantidade']}")

                try:
                    nova_quantidade = int(input("Nova quantidade: "))

                    if nova_quantidade < 0:
                        print("Não é possível adicionar uma quantidade negativa.❌")
                        return

                except ValueError:
                    print("Digite uma quantidade válida❌")
                    return

                confirmacao = input(
                    f"Confirma a troca de quantidade de {nome_buscado}\n"
                    f"de {produto['Quantidade']} para {nova_quantidade}\n"
                    "? Sim[1] | Não[2]: "
                ).upper()

                if confirmacao.startswith("S") or confirmacao == "1":
                    produto["Quantidade"] = nova_quantidade
                    print(
                        f"Quantidade de {nome_buscado} alterada para {nova_quantidade}✅\n"
                    )
                else:
                    print("Cancelando troca de quantidade.")
                    print("Voltando ao menu principal.🔙")

                return

            else:
                print("Escolha uma ação válida.❌")
                return

    print(f"{nome_buscado} NÃO está cadastrado❌.\nAdicione o item para ver.")


def listar_produto():
    print("\n~ Listando produtos ~")

    if not produtos:
        print("Não existem produtos cadastrados...")
    else:
        for indice, produto in enumerate(produtos):
            print(
                f"{indice+1} - {produto['Nome']}: R$ {produto["Preço"]:.2f} | Quantidade : {produto["Quantidade"]}"
            )
        print()


def cadastrar_produto():

    print("\n~ Cadastrando produto ~")

    nome_produto_cadastro = input("Nome: ").capitalize()

    if nome_produto_cadastro == "" or nome_produto_cadastro == " ":
        print("Nome não pode ser vazio")
        return

    try:
        preco_produto_cadastro = float(input("Preço: "))

        if preco_produto_cadastro <= 0:
            print("Preço não pode ser menor ou igual a zero.")
            return

    except ValueError:
        print("Digite um valor válido.")
        return

    try:
        quantidade_produto_cadastrado = int(input("Quantidade: "))

        if quantidade_produto_cadastrado < 0:
            print("Não é possível adicionar quantidades negativas.")
            return

    except ValueError:
        print("Digite uma quantidade válida.")
        return

    novo_produto = {
        "Nome": nome_produto_cadastro,
        "Preço": preco_produto_cadastro,
        "Quantidade": quantidade_produto_cadastrado,
    }

    produtos.append(novo_produto)

    print(f"{nome_produto_cadastro} cadastrado com sucesso.")


while True:
    print("----------------Página Principal----------------")
    for chave, valor in opcoes.items():
        print(chave, "-", valor)

    try:
        opcao_usuario = int(input("\nEscolha uma opção: \n"))
    except ValueError:
        print("Digite uma opção válida❌\n")

        continue

    if opcao_usuario in opcoes:

        if opcao_usuario == 0:
            print("Saindo...")
            break

        elif opcao_usuario == 1:
            listar_produto()

        elif opcao_usuario == 2:
            cadastrar_produto()

        elif opcao_usuario == 3:
            buscar_produto()
        else:
            print("Digite uma opção válida.❌\n")
