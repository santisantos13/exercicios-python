print(10*"-",'Média de notas',10*"-")
#Pede as notas


while True:
  nota1 = float(input("Digite a nota do primeiro trimestre: "))
  nota2 = float(input("Digite a nota do segundo trimestre: "))
  nota3 = float(input("Digite a nota do terceiro trimestre: "))

  media = (nota1 + nota2 + nota3) / 3
  #############################################################
  if media >= 7:
    print(f'Média = {media:.2f}')
    print("Aluno aprovado")
  
  elif media < 5:
    print(f'Média = {media:.2f}')
    print('Aluno reprovado.')

  elif media >= 5:
    print(f'Média = {media:.2f}')
    print("Aluno em recuperação.")
  else:
    print("Digite uma nota válida.")
  
  
  encerrar = input(
    'Deseja verificar outra nota?: [s]im ou [n]ão '
  ).lower()
  
  if encerrar not in ['s', 'sim','yes']:
    print('Programa encerrado.')
    break
