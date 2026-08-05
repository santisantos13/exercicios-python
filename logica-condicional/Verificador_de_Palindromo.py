palavra_usuário = input("Digite uma palavra: ")
palavra_invertida = ''

for letra in palavra_usuário:
    palavra_invertida = letra + palavra_invertida


if palavra_usuário == palavra_invertida:
    print(f'{palavra_usuário} é palindromo:')
    print(palavra_invertida)
else:
    print(f'{palavra_usuário} não é palindromo.')
    print(palavra_invertida)
