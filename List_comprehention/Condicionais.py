numeros = list(range(1, 11))
print(numeros)

novos_numeros = [numero for numero in numeros if numero > 5]  # Filter
print(novos_numeros)

odd = [numero for numero in numeros if numero % 2 != 0]
print(odd)

pair = [numero for numero in numeros if numero % 2 == 0]
print(pair)

other_condition = [
  numero 
  if numero != 6 else 600 
  for numero in pair
]
print(other_condition)
