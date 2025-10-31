with open("medicoes.txt", "w") as arquivo:
    for i in range(5):
        valor = input(f"Valor {i + 1}: ")
        arquivo.write(valor + "\n")

with open("medicoes.txt", "r") as arquivo:
    medicoes = []
    for linha in arquivo:
        medicoes.append(int(linha))

maiores = 0
for i in range(1, len(medicoes)):
    if medicoes[i] > medicoes[i - 1]:
        maiores += 1

print("Numeros maiores que o anterior é", maiores)
