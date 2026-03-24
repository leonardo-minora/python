dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
quociente = dividendo // divisor
resto = dividendo % divisor
print(f"{dividendo} ÷ {divisor} = {quociente} (quociente) com resto {resto}")
print(f"Verificação: {divisor} × {quociente} + {resto} = {divisor * quociente + resto}")
