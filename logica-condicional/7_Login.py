'''
senha = "senha"
tentativas = 0
while input('Digite uma senha: ') != senha and tentativas < 3:
  tentativas += 1
  print('Senha incorreta.')

print("Senha correta!")
'''
senha_correta = 'senha'
tentativa = 0

while tentativa < 3:
  tentativa += 1
  senha = input("Digite uma senha: ")

  if senha != senha_correta:
    print("Senha incorreta!")
  
  else:
    print("Senha correta")
    break
if tentativa == 3 and senha != senha_correta:
  print("Conta bloqueada.")
print("programa encerrado")