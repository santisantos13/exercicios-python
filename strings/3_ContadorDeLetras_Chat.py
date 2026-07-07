nome = input('Digite seu nome: ')

vogais = 0

for letra in nome:
  if letra.lower() in 'aeiou':
    vogais += 1

print(f'{nome} tem {vogais} vogais')