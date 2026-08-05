
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Monitor", "preco": 1200},
    {"nome": "Teclado", "preco": 150},
]
carros = [
    {"nome": "Fiat Palio", "preco": 39000},
    {"nome": "Fiat Siena", "preco": 41000},
    {"nome": "Fiat Fiorino", "preco": 45000},
    {"nome": "Fiat Uno", "preco": 12000},
]


def analisar_produtos(produtos):

    total = 0
    mais_caro = produtos[0] 
    mais_barato = produtos[0]

    for produto in produtos:
      total += produto["preco"]

      if produto["preco"] > mais_caro['preco']:
          mais_caro = produto

      if produto["preco"] < mais_barato['preco']:
          mais_barato = produto

    print(f"Total: R${total}")
    print(f"Mais caro: {mais_caro['nome'], mais_caro['preco']}")
    print(f"Mais barato: {mais_barato['nome'], mais_barato['preco']}")

    return total,mais_caro, mais_barato

analisar_produtos(produtos)
print()
analisar_produtos(carros)
