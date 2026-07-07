def soma(num1,num2):
  return num1 + num2

def multiplicacao(num1,num2):
  return num1 * num2

def divisao(num1, num2):
  if num2 == 0:
    return 'Não é possivel dividir por zero.'
  return num1 / num2

def subtracao(num1, num2):
  return num1 - num2
while True:
  
  print("Adição, Subtração, Multiplicação e Divisão   ")
  print("---------------------------------------------")
  print("------------escolha-de-operadores------------")
  operador = input("Digite um operador: ")

  if operador == "Adição" or operador == '+' or operador == "mais" or operador == "adicao":
    print("-------------------Adição-------------------")
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
  
    resultado = f"A soma é igual a {soma(n1,n2)}"
    print(resultado)

  elif operador == "menos" or operador == "-" or operador == "Subtração" or operador == "subtracao":
    print("----------------Subtração-------------------")
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
  
    resultado = f"A subtração é igual a {subtracao(n1,n2)}"
    print(resultado)

  elif operador == "vezes" or operador == "*" or operador == "Multiplicação" or operador == "Multiplicacao":
    print("----------------Multiplicação---------------")
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
  
    resultado = f"A Multiplicação é igual a {multiplicacao(n1,n2)}"
    print(resultado)

  elif operador == "divisao" or operador == "/" or operador == "Divisao" or operador == "Dividir":
    print("----------------Divisão---------------------")
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
  
    resultado = f"A Divisão é igual a {divisao(n1,n2)}"
    print(resultado)
  elif operador == 'sair':
    break
  else:
    print("--------------------------")
    print("Digite um operador válido")
  
  