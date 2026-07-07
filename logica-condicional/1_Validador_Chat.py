try:
  numero = int(input("Digite um número: "))
  
# positivo ou negativo
  if numero > 0:
    print(f'O número {numero} é positivo.')

  elif numero < 0:
    print(f'O número {numero} é negativo.')

  else:
    print(f"{numero} é zero.") 

# checar se é par ou ímpar
  if numero % 2 == 0:
    print(f"O número {numero} também é par.")
  else:
    print(f'O número {numero} também é ímpar.')
except:
  print('Digite um número válido')