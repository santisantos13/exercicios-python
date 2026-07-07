import random

numero_aleatorio = random.randint(1, 100)
numero_usuario = 0
tentativas = 0


def igual():
    print(f"Acertou, o número sorteado era {numero_aleatorio}.")
    print(f"Você acertou em {tentativas} tentativas.")


def menor():
    print(f"Errou, o número sorteado é maior que {numero_usuario}.")
    print("Tente novamente...")


def maior():
    print(f"Errou, o número sorteado é menor que {numero_usuario}.")
    print("Tente novamente...")


while True:

    try:
        print("---------------------- JOGO DE ADIVINHAÇÃO ----------------------")
        numero_usuario = int(input("Digite um número entre 1 e 100: "))
        if numero_usuario > 100:
            print("O número não pode ser maior que 100...")
            continue
        elif numero_usuario <= 0:
            print("Números negativos não são válidos...")
            continue

    except ValueError:
        print("Digite um número INTEIRO.")
        continue

    if numero_usuario == numero_aleatorio:

        tentativas += 1
        igual()
        continuar = input("Deseja continuar? [s]/[n]: ").lower()

        if continuar.startswith("s"):
            numero_aleatorio = random.randint(1, 100)
            tentativas = 0
            continue
        else:
            print("encerrando...")
            break

    elif numero_usuario < numero_aleatorio:
        menor()
        tentativas += 1
    elif numero_usuario > numero_aleatorio:
        maior()
        tentativas += 1
    else:
        print("Não deveria chegar aqui...")
