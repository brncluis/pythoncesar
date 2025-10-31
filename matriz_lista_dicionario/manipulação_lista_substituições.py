import os;os.system('cls')
lista = []
while True:
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        nome = input("Digite o valor que deseja adicionar na lista: ")
        lista.append(nome)

    elif opcao == 2:
        for i in range (len(lista)):
            print([i], lista[i])

    elif opcao == 3:
        nome_remover = input("Insira o nome que deseja remover: ")
        lista.remove(nome_remover)
    
    elif opcao == 4:
        print(lista)
        nome_substituir = input("Digite o nome que deseja substituir: ")
        if nome_substituir in lista:
            nome_novo = input("Digite o novo nome: ")
            indice_sub = lista.index(nome_substituir)
            lista.insert(indice_sub,nome_novo)
            lista.remove(nome_substituir)
            print(lista)
        else:
            print("Digite um valor existente ou adicione.")
    elif opcao == 5:
        for i in range(len(lista)):
            print(i, lista[i])


        

            

        

