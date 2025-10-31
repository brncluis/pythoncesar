import os; os.system('cls')

numero_secreto = int(input("Digte um numero secreto de 1 a 100:  "))

tentativas = 0

os.system('cls')

while True:
    chute = int(input("Insira o chute: "))
    
    tentativas = tentativas + 1

    if chute == numero_secreto:
        print(f"Você acertou em {tentativas} tentativas.")
        break
    elif chute < numero_secreto:
        print("Chute muito baixo.")
    elif chute > numero_secreto:
        print("Chute muito alto")

