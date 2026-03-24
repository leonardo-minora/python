import math

raio = float(input("Digite o raio do círculo (cm): "))
area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio
print(f"Círculo com raio {raio} cm:")
print(f"  Área: {area:.4f} cm²")
print(f"  Perímetro: {perimetro:.4f} cm")
