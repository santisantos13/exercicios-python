import sqlite3

conexao = sqlite3.connect("sistema.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

conexao.commit()


def criar_usuario():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    cursor.execute(
        """
    INSERT INTO usuarios (nome, idade)
    VALUES (?, ?)
    """,
        (nome, idade),
    )

    conexao.commit()

    print("Usuário cadastrado com sucesso!")


def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    print("\n--- LISTA DE USUÁRIOS ---")

    if len(usuarios) == 0:
        print("Nenhum usuário encontrado.")

    for usuario in usuarios:
        print(f"ID: {usuario[0]}")
        print(f"Nome: {usuario[1]}")
        print(f"Idade: {usuario[2]}")
        print("-" * 20)


def atualizar_usuario():
    id_usuario = int(input("Digite o ID do usuário: "))

    novo_nome = input("Novo nome: ")
    nova_idade = int(input("Nova idade: "))

    cursor.execute(
        """
    UPDATE usuarios
    SET nome = ?, idade = ?
    WHERE id = ?
    """,
        (novo_nome, nova_idade, id_usuario),
    )

    conexao.commit()

    print("Usuário atualizado!")


def deletar_usuario():
    id_usuario = int(input("Digite o ID do usuário que deseja deletar: "))

    cursor.execute(
        """
    DELETE FROM usuarios
    WHERE id = ?
    """,
        (id_usuario,),
    )

    conexao.commit()

    print("Usuário deletado!")


while True:

    print("\n===== SISTEMA CRUD =====")
    print("1 - Criar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Deletar usuário")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_usuario()

    elif opcao == "2":
        listar_usuarios()

    elif opcao == "3":
        atualizar_usuario()

    elif opcao == "4":
        deletar_usuario()

    elif opcao == "5":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")

conexao.close()
