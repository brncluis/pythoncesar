import os;os.system('cls')
cardapio = {}


while True:
    opccao = int(input("Insira a opção \n[1]Adicionar \n[2]Remover \n[3]Mudar preço\n "))
    if opccao == 1:
        produto = input("Insira o nome do produto: ")
        valor = int(input("Insira o valor do produto: "))
        cardapio[produto] = valor
        print(cardapio)
    elif opccao == 2: 
        produto = input("Insira o nome do produto que quer remover: ")
        cardapio.pop(produto, "Produto não existe")
        print(cardapio)
    elif opccao == 3:
        produto = input("Insira o produto que deseja mudar o valor: ")
        valor = int(input("Insira o novo valor do produto: "))
        cardapio[produto] = valor

        print(cardapio)
    elif opccao == 4:
        print(cardapio)
        break

