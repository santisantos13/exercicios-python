while True:
    tem_numero = False
    tem_letra = False

    senha = input("Digite uma senha: ")

    for caractere in senha:

        if caractere.isdigit():
            tem_numero = True

        if caractere.isalpha():
            tem_letra = True

    if tem_letra and tem_numero and len(senha) >= 8:
        print("Senha forte.")
    else:
        print("Senha fraca.")

    sair = input("Deseja fechar o programa? [s]im/[n]ão: ").lower()

    if sair.startswith("s"):
        break
