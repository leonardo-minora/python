numero = int(input("Digite um número inteiro: "))
resto = numero % 2
tipo = "par" if resto == 0 else "ímpar"
print(f"O número {numero} é {tipo}.")
