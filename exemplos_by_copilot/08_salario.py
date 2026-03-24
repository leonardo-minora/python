funcionario = input("Nome do funcionário: ")
salario = float(input("Salário base (R$): "))
percentual = float(input("Percentual de bônus (%): "))
bonus = salario * percentual / 100
salario_final = salario + bonus
print(f"Funcionário: {funcionario}")
print(f"Salário base: R$ {salario:.2f}")
print(f"Bônus ({percentual}%): R$ {bonus:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")
