arquivo = open("arquivo.txt", "w", encoding="utf8")

nomes = []
racas = []

for i in range(2):
    nome = input("Digite o nome do cachorro: ")
    nomes.append(nome)
    raca = input("Digite a raça do cachorro: ")
    racas.append(raca)

for i in range(2):
    arquivo.writelines(" Nome: " + nomes[i] + " Raça: " + racas[i] + "\n")

arquivo.close()

arquivo = open("arquivo.txt", "r")
print("Animais cadastrados")
print(arquivo.read())
arquivo.close()