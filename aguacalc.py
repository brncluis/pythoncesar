#pedir peso 
#calcular agua diaria do peso
#pedir qtd agua tomada por dia 
#retornar quantidade ideal
#35ml por peso 
import os

def inicio():
    os.system('cls')
    peso = float(input("Informe seu peso corporal em Kg: "))
    ideal = peso * 35
    litros = ideal / 1000 
    info = float(input("Quantos litros de agua voce consome por dia: "))

    if info < litros:
        os.system('cls')
        print(f"\nVocê não está consumindo a quantidade ideal de agua\n\nA quantidade ideal para seu peso é {litros:.1f} litros")  
        input('\nDigite qualquer tecla para voltar ao inicio\n')  
        inicio()
    elif info > litros: 
        os.system('cls')
        print(f"\nVocê está consumindo a quantidade ideal XD") 
        input('\nDigite qualquer tecla para voltar ao inicio\n') 
        inicio()  
    else:
        os.system('cls')
        print(f"Insira um valor válido")
        input('\nDigite qualquer tecla para voltar ao inicio\n')
        inicio()

inicio()




