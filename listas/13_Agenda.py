contatos = []  # Lista de contatos vazia


def mostrar_menu():
    """Mostra o menu principal"""
    print("            AGENDA")
    print("-" * 30)
    print("1 - Listar contatos")
    print("2 - Adicionar contatos")
    print("3 - Buscar contatos")
    print("4 - Sair")


def listar_contatos():
    """Lista todos os contatos salvos"""
    print("         CONTATOS SALVOS")
    print("-" * 30)

    if not contatos:  # Verifica a agenda não tem números salvos
        print("Não existem contatos salvos...❌")
        print("Adicione um contato para ver a lista.")
    else:
        for nome, numero in contatos:
            print(f"{nome} : {numero}")

    print("-" * 30)


def add_contatos():
    """Adiciona um novo contato à agenda"""
    print("         ADICIONAR CONTATO")
    print("-" * 30)

    # Validação de nome.

    while True:  #                     remove espaços no final e no começo da string
        nome = input("Digite o nome: ").strip()

        if not nome:  # Verifica se o usuário não digitou nada no campo "nome"
            print("❌ Nome não pode estar vazio!")
            continue

        if not nome.replace(" ", "").isalpha():  # Aceita apenas letras e espaços
            print("❌ Digite apenas letras (sem números ou caracteres especiais)")
            continue

        break

    # Validação de número
    while True:
        try:
            numero = input("Digite o número: ").strip()

            if not numero:
                print("❌ Número não pode estar vazio!")
                continue

            numero = int(numero)  # Converte para int

            if numero < 0:
                print("❌ O número deve ser positivo!")
                continue

            break
        except ValueError:
            print(
                "❌ Apenas números são válidos!"
            )  # Troca o erro que quebraria o programa por uma mensagem e continua rodando

    contato = [nome, numero]  # lista que recebe nome e número
    contatos.append(contato)  # Adicionando o contato dentro da lista "contatos"
    print("Adicionando contato...")
    print("Contato Adicionado!✅")
    print("-" * 30)


def buscar_contatos():
    """Busca um contato pela nome"""
    print("        BUSCAR CONTATO")
    print("-" * 30)

    if not contatos:
        print("❌ Nenhum contato para buscar!")
        print("-" * 30)
        return

    nome_buscado = input("Digite o nome do contato: ").strip().lower()

    if not nome_buscado:
        print("❌ Nome não pode estar vazio!")
        print("-" * 30)
        return

    encontrado = False

    for nome, numero in contatos:
        if nome.lower() == nome_buscado:
            print(f"✅ {nome} : {numero}")
            encontrado = True
            break

    if not encontrado:
        print("❌ Contato não encontrado.")

    print("-" * 30)


# Loop principal
while True:
    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("-" * 30)
        print("❌ Digite apenas números!")
        print("-" * 30)
        continue

    print("-" * 30)

    if opcao == 1:
        listar_contatos()

    elif opcao == 2:
        add_contatos()

    elif opcao == 3:
        buscar_contatos()

    elif opcao == 4:
        print("👋 Encerrando agenda...")
        break

    else:
        print("❌ Digite uma opção válida.")
        print("        1 | 2 | 3 | 4     ")
        print("-" * 30)
