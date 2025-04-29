nomes = [""] * 5
for i in range(len(nomes)):
    nomes[i] = input("digite o nome:")
for i in range(len(nomes)):
    print(f"{nomes[i]} - {i}", end=" ")