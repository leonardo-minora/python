produto = input("Nome do produto: ")
preco = float(input("Preço original (R$): "))
desconto = float(input("Desconto (%): "))
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto de {desconto}%: - R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
