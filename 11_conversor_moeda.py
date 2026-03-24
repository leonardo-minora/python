valor_reais = float(input("Digite o valor em reais (R$): "))
cotacao_dolar = float(input("Digite a cotação do dólar: "))
cotacao_euro = float(input("Digite a cotação do euro: "))
em_dolares = valor_reais / cotacao_dolar
em_euros = valor_reais / cotacao_euro
print(f"R$ {valor_reais:.2f} equivale a:")
print(f"  US$ {em_dolares:.2f} (dólares)")
print(f"  € {em_euros:.2f} (euros)")
