import os
os.system('cls')
m = []
n = int(input("Insira o tamanho da matriz n x n: "))
print()
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input(f"Elemento [{i}][{j}]: ")))
    m.append(linha)
simetrica = True
for i in range(n):
    for j in range(n):
        if m[i][j] != m[j][i]:
            print(m[i][j])
            simetrica = False
            break
        if simetrica == False:
            break
diag_zero = True
for i in range(n):
    for j in range(n):
        if i == j:
            if m[i][j] != 0:
                diag_zero = False
                break
    if diag_zero == False:
        break
print()
if simetrica == True:
    print("Simétrica: Sim")
else:
    print("Simétrica: Não")
if diag_zero == True:
    print("Diagonal zero: Sim")
else:
    print("Diagonal zero: Não")

for i in range(n):
    for j in range(n):
        print(f"{m[i][j]}", end= " ")
    print()