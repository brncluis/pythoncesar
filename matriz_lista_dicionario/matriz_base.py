import os;os.system('cls')
matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        matriz[i].append(input(""))
        print(matriz)
        
for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]}", end = " ")
    print("") 