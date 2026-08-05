for numero in range(1, 101):
    resultado = ''

    if numero % 3 == 0:
        resultado += 'Fizz'

    if numero % 5 == 0:
        resultado += 'Buzz'

    if numero % 7 == 0:
        resultado += 'Bang'

    if resultado == '':
        print(numero)

    else:
        print(resultado)