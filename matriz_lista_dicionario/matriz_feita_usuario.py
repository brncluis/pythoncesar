matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        numeros = int(input("Insira os valores da matriz: "))
        matriz[i].append(numeros)
        

soma = 0

print(matriz[0][0]*matriz[1][1]*matriz[2][2])

for i in range(3):
    for j in range(3):
        soma = soma + matriz[i][j]

media = soma / 9
print(media)

maior = 0

for i in range(3):
    for j in range(3):
        if matriz[i][1] > maior:
            maior = matriz[i][1]
print(maior)

valor = 0
menor_media = []

for i in range(3):
    for j in range(3):
        if matriz[i][j] <= media:
            menor_media.append(matriz[i][j])

print(menor_media)
