import os; os.system("cls")
matriz = [[], [], []]
soma=0; total_salarios=0

for i in range (3):
    if i == 0:
        print("Preencha com as informções de um Desenvolvedor Python: ")
    elif i == 1:
        print("Preencha com as informções de um Cientista de Dados: ")
    elif i == 2:
        print("Preencha com as informções de um Analista de QA: ")
    salario = int(input("Salário:"))
    exp_minima = int(input("Tempo de experiência: "))
    valor_hora = int(input("Valor hora:"))
    matriz[i].append(salario)
    matriz[i].append(exp_minima)
    matriz[i].append(valor_hora)

soma_diago = []
for i in range(3):
    soma_diago.append(matriz[i][i])
soma_diagonal = sum(soma_diago)
print(f"\nA soma da diagonal é: {soma_diagonal}\n")

for j in range(3):
    soma = soma + matriz[j][0]
    total_salarios +=1
    

print(" Sálario \tTempo minimo\tValor hora")
for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]:^13}", end=" ")
    print()
print(f"A média do sálario das três profissões juntas é: {soma/total_salarios}")