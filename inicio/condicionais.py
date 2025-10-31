import os

def inicio():
    os.system('cls')
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))

    soma = n1 + n2 

    if soma == 0:
        print("Cheia de manias")
        input("Digite qualquer tecla para voltar ao inicio")
        inicio()
    elif soma == 1:
        print("Me leva junto de voce")
        input("Digite qualquer tecla para voltar ao inicio")
        inicio()
    elif soma == 2:
        print("É tarde demais")
        input("Digite qualquer tecla para voltar ao inicio")
        inicio()
    elif soma == 3:
        print("Quando te troquei")
        input("Digite qualquer tecla para voltar ao inicio")
        inicio()
    elif soma == 4:
        print("Deus me livre")
        input("Digite qualquer tecla para voltar ao inicio")
        inicio()
    elif soma == 5:
        print("Ciume de voce")
        input("Digite qualquer tecla para voltar ao inicio")
        inicio()
    elif soma == 6:
        print("Cigana")
        input("Digite qualquer tecla para voltar ao inicio")
        inicio()
    else:
        print("Invalida, digite um valor valido\n")
        input("Digite qualquer tecla para sair")

inicio()