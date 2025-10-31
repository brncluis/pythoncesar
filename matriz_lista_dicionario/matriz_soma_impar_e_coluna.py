matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        valor = int(input("Digite: "))
        matriz[i].append(valor)

soma_impar = 0
soma_coluna = 0
for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]:^3}", end=" ")
        if matriz[i][j] % 2 != 0:
            soma_impar += matriz[i][j]
        if j == 0:
            soma_coluna += matriz[i][j]
    print()

print(f"A soma dos valores impares é: {soma_impar}")
print(f"A soma da primeira coluna é {soma_coluna}")
print(f"O menor valor da terceira linha é {min(matriz[2])}")