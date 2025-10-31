import os;os.system('cls')
total = 0
carronovo = 0
carroantigo = 9999

while True:
    nome = input("Insira a marca do carro: ")
    data = int(input("Insira o ano do carro: "))
    if data > carronovo:
        carronovo = data
    if data < carroantigo:
        carroantigo = data

    total = total + 1
    cont = input("Desseja continuar:")
    
    if cont == "Sim":
        print()
    else:
        break

print(carroantigo)
print(carronovo)
print(total)
    



