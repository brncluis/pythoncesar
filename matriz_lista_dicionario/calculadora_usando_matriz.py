matriz = [[], [], []]

totalsoma = 0
multi = 1

operacao = int(input("Insira a operação desejada\n[1]Soma\n[2]Multiplicação\n"))
coluna = int(input("Insira a coluna desejada: "))
        
for i in range(3):
    for j in range(3):
        valor = int(input(f"Insira os valores da lista "))
        matriz[i].append(valor)
   
for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]}", end=" ")
    print()

for i in range(3):
    for j in range(3):
        if j == coluna:
            if operacao == 1:
                totalsoma = totalsoma + matriz[i][j]
            elif operacao == 2:
                produto = produto * matriz[i][j]

if operacao == 1:
    print(f"Soma é {totalsoma}")
elif operacao == 2:
    print(f"Multiplicação é {multi}")

            