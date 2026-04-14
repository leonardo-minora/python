vitorias = 0
for _ in range(6):
    resultado = input().upper()
    if resultado == 'V':
        vitorias += 1
if vitorias > 4:
    print(1)
elif vitorias > 2:
    print(2)
elif vitorias > 0:
    print(3)
else:
    print(-1)
