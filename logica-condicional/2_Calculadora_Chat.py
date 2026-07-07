try:
  numero1 = int(input("Digite um número: "))
  numero2 = int(input('Digite outro número: '))
  print("Os operadores são: ")
  print("Adição =     +     ")
  print("Subtração =  -     ")
  print("Multiplicação = x  ")
  print("Divisão =    /     ")  
  
  operacao = str(input('Escolha o operador: '))


  if operacao == "+":
    print(f"A soma de {numero1} + {numero2} = {numero1 + numero2 }")
  
  elif  operacao == "-":
    print(f'A subtração de {numero1} - {numero2} = {numero1 - numero2 }')
  
  elif  operacao.lower() == "x":
    print(f'A multiplicação de {numero1} x {numero2} = {numero1 * numero2 }')
  
  elif  operacao == "/":
    if numero2 == 0:
      print('Não é possível dividir por zero.')
    else:
      print(f'A divisão de {numero1} / {numero2} = {numero1 / numero2}')
  
  else:
    print("Digite um operador válido.")

except:
  print('Escolha um número válido.')