import os

def inicio():
    os.system('cls')
    print("Calculadora em python")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operacao = input("Qual operação deseja fazer:\n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n")

    if operacao == "1" or operacao == "Soma":
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} é igual a: {soma}")
        input("Digite qualquer tecla para voltar ao inicio\n")
        inicio()
    elif operacao == "2" or operacao == "Subtração": 
        sub = n1 - n2
        print(f"A subtração de {n1} - {n2} é igual a: {sub}")
        input("Digite qualquer tecla para voltar ao inicio\n")
        inicio()
    elif operacao == "3" or operacao == "Multiplicação":
        mult = n1 * n2
        print(f"A multiplicação de {n1} * {n2} é igual a: {mult}")
        input("Digite qualquer tecla para voltar ao inicio\n")
        inicio()
    elif operacao == "4" or operacao == "Divisão":
        div = n1/n2
        print(f"A divisão de {n1} por {n2} é igual a: {div}")
        input("Digite qualquer tecla para voltar ao inicio\n")
        inicio()
    else: 
        print("Opção inválida, reinicia e insira a opção corretamente.")
        input("\nDigite qualquer tecla para voltar ao inicio\n")
        inicio()
    
inicio()