import os;os.system('cls')

repteis = []
mamiferos = []
aves = []
outros = []

for i in range(10):
    print("Escolha entre \n[1]Reptil \n[2]Mamifero \n[3]Ave \n[4]Outros")

    numero =  int(input("Insira o número de escolha: \n"))
    if numero == 1:
        repteis.append(input("Insira o nome do animal: "))
        print("O animal foi cadastrado com sucesso.")
    elif numero == 2:
        mamiferos.append(input("Insira o nome do animal: "))
        print("O animal foi cadastrado com sucesso.")
    elif numero == 3:
        aves.append(input("Insira o nome do animal: "))
        print("O animal foi cadastrado com sucesso.")
    elif numero == 4:
        outros.append(input("Insira o nome do animal: "))
        print("O animal foi cadastrado com sucesso.")
    else:
        print("Insira uma opção válida")

print(f"Repteis: {repteis} {len(repteis)}")
print(f"Mamiferos: {mamiferos} {len(mamiferos)}")
print(f"Aves: {aves} {len(aves)}")
print(f"Outros: {outros} {len(outros)}")
