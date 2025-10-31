import os; os.system('cls')

produtos = []
quantidades = []

while True:
    print("*"*20, "OPÇÕES", "*"*20)
    print("[1] - AP\n[2] - RP\n[3] - AE\n[4] - RE\n[5] - S")
    escolhas = int(input("escolha: "))

    if escolhas == 5:
        break 

    if escolhas == 1:
        produto = input("Digite o nome do produto: ")
        qtd = int(input("Digite a quantidade desse produto: "))
        produtos.append(produto)
        quantidades.append(qtd)

    if escolhas == 2: 
        nome_produ = input("nome do produto que quer apagar: ")
        indice_produ = produtos.index(nome_produ)
        produtos.pop(indice_produ)
        quantidades.pop(indice_produ)

    if escolhas == 3:
        nome_produ = input("nome do produto que voce quer atualizar a quantidade: ")
        indice_produ = produtos.index(nome_produ)
        qtd_aumento = int(input("Digite a quantidade que você quer aumentarm "))
        qa = quantidades[indice_produ]
        qa = qa + qtd_aumento 

        quantidades[indice_produ] = qa
        print(quantidades)
