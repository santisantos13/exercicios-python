precos = {
  "Galaxy 25 265GB": 3800,
  "Galaxy Watch 6 Clasic": 1200,
  "Galaxy Tab S10 FE+": 2000
}
produto = input("Digite o produto desejado: ")
try:
  preco = precos[produto]
except:
  print("Produto não encontrado")
else:
  print(f"Preço do {produto}: R${preco}")