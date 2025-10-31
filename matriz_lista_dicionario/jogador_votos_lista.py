votos = []

while True:
     numcamisa = int(input("Digite o número da camisa do jogador: "))
     if numcamisa == 0:
         break
     elif 7 > numcamisa > 11:
         print("Número inválido. Tente novamente.")
     else:
         votos.append(numcamisa)

sete = 0
oito = 0
nove = 0
dez = 0
onze = 0

for i, v in enumerate(votos):
    if v == 7:
        sete += 1
    if v == 8:
        oito += 1
    if v == 9:
        nove += 1
    if v == 10:
        dez += 1
    else:
        onze += 1

totalv = len(votos)
print(f"Total de votos válidos: {totalv}.")
print(f"Jogador 7: {sete}. Porcentagem: {sete/totalv:.2f}%. \nJogador 8: {oito}. Porcentagem: {oito/totalv:.2f}%.\nJogador 9: {nove}. Porcentagem: {nove/totalv100:.2f}%.\nJogador 10: {dez}. Porcentagem: {dez/totalv100:.2f}%.\nJogador 11: {onze}. Porcentagem: {onze/totalv*100:.2f}%.")

vetor_jogadores = ["sete","oito","nove","dez","onze"]
votosporjog = [oito,sete,nove,dez,onze]

indice_maior = votosporjog.index(max(votosporjog))

print(f"Melhor jogador: {vetor_jogadores[indice_maior]}")

