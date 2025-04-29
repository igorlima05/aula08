notas = [""] * 5
soma = 0
cont = 0
for i in range(len(notas)):
    notas[i] = float(input(f"digite as notas {i + 1}:"))
for x in range(len(notas)):
    soma += notas[x]
media = soma / len(notas)
for c in range(len(notas)):
    if notas[c] > media:
        cont += 1
print(f"encontramos {cont} alunos acima da media ")
