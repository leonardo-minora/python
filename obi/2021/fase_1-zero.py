repeticoes = int(input())

numeros = []
soma = 0
for i in range(repeticoes):
    numero = int(input())
    if numero != 0:
        numeros.append(numero)
        soma += numero
    elif numero == 0:
        soma -= numeros.pop()
print(soma)