def registro(votos):
    with open("registrador.txt", "w") as arquivo:
        for i in range(len(votos)):
            arquivo.write(votos[i] + "\n")
    return arquivo

votos = []

for i in range(5):
    voto = input("Vote: ")
    votos.append(voto)

registro(votos)

sushi = 0
churras = 0

with open("registrador.txt", "r") as arquivo:
    for linha in arquivo:
        voto = linha.strip("\n")
        if voto == "1":
            sushi = sushi + 1
        elif voto == "2":
            churras = churras + 1

if sushi > churras:
    print(f"Sushi venceu com {sushi} votos")
elif churras > sushi:
    print(f"Churras venceu com {churras} votos")
else:
    print("Empatou")
