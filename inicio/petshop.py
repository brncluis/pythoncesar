banho = 0
tosa = 0
banho_tosa = 0
outros = 0
import os; os.system('cls')
for i in range(5):
    print("Escolha o serviço que foi feito\n[1]Banho\n[2]Tosa\n[3]Banho e tosa\n[4]Outros\n")
    servico = int(input("Insira: "))
    if servico == 1:
        banho = banho + 1
    elif servico == 2:
        tosa = tosa + 1
    elif servico == 3:
        banho_tosa = banho_tosa + 1
    elif servico == 4:
        outros = outros + 1
    else:
        print("Valor invalido")

print(f"\nServiços feitos:\nBanho: {banho} \nTosa: {tosa} \nBanho e tosa: {banho_tosa}\nOutro: {outros}")