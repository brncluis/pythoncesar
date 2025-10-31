import os;os.system('cls')

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtracao(numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def divisao(numero1, numero2):
    if numero1 < numero2:
        resultado = numero2 / numero1
    else:
        resultado = numero1 / numero2
    return resultado

def produto(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

def rep(num1, num2):
    escolha = int(input("Escolha a opção nova que deseja fazer \n[1]Soma\n[2]Subtração\n[3]Divisão\n[4]Produto\n[5]Sair\n"))
    if escolha == 1:
        print(soma(num1, num2))
    elif escolha == 2:
        print(subtracao(num1, num2))
    elif escolha == 3:
        print(divisao(num1, num2))
    elif escolha == 4:
        print(produto(num1, num2))   
    return escolha
        
while True:
    print("\nCALCULADORA PYTHON")
    escolha = int(input("Escolha a opção \n[1]Soma\n[2]Subtração\n[3]Divisão\n[4]Produto\n[5]Sair\n"))
    if escolha >=1 and escolha <= 4:  
        num1 = int(input("Insira o primeiro número da operação: "))
        num2 = int(input("Insira o segundo número da operação: "))
        
        if escolha == 1:
            print(soma(num1, num2))
            vontade = input("Deseja fazer outra operação com esses números? Sim ou Nao\n")
            if vontade == "Sim":
                os.system('cls')
                quantidade = int(input("Quantas operações a mais você deseja realizar: "))
                if quantidade > 0:
                    for i in range (quantidade):
                        rep(num1, num2)
                        print()
            else:
                os.system('cls')
                continue
        elif escolha == 2:
            print(subtracao(num1, num2))
            vontade = input("Deseja fazer outra operação com esses números? Sim ou Nao\n")
            if vontade == "Sim":
                os.system('cls')
                quantidade = int(input("Quantas operações a mais você deseja realizar: "))
                if quantidade > 0:
                    for i in range (quantidade):
                        rep(num1, num2)
                        print()
            else:
                os.system('cls')
                continue
        elif escolha == 3:
            print(divisao(num1, num2))
            vontade = input("Deseja fazer outra operação com esses números? Sim ou Nao\n")
            if vontade == "Sim":
                os.system('cls')
                quantidade = int(input("Quantas operações a mais você deseja realizar: "))
                if quantidade > 0:
                    for i in range (quantidade):
                        rep(num1, num2)
                        print()
            else:
                os.system('cls')
                continue
        elif escolha == 4:
            print(produto(num1, num2))
            vontade = input("Deseja fazer outra operação com esses números? Sim ou Nao\n")
            if vontade == "Sim":
                os.system('cls')
                quantidade = int(input("Quantas operações a mais você deseja realizar: "))
                if quantidade > 0:
                    for i in range (quantidade):
                        rep(num1, num2)
                        print()
            else:
                os.system('cls')
                continue
    elif escolha == 5:
        print("\nSaindo...")
        break