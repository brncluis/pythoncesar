import os;os.system('cls')
votos = []

votantes = int(input("Insira a quantidade de pessoas que vao votar: "))

for i in range(votantes):
    print("Escolha entre A e B")
    voto = input("Insira [A] ou [B]\n")
    if voto == "A" or voto == "B":
        votos.append(voto)
    else:
        print("Insira uma opção correta.")

votosA = votos.count("A")
votosB = votos.count("B")
votos_total = len(votos)
prcA = votosA/votos_total * 100
prcB = votosB/votos_total * 100

if votosA > votosB:
    print("O candidato A venceu")
    print(f"A quantidade de votos foi: {votosA}")
    print(f"A porcentagem foi {prcA}%")
    
elif votosB > votosA:
    print("O candidato B ganhou")
    print(f"A quantidade de votos foi: {votosB}")
    print(f"A porcentagem foi {prcB}%")
else: 
    print("Empate, segundo turno necessario")


