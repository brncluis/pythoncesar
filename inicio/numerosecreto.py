numeroSecreto = int(input("Digite o número secreto: "))
tentativas = 1

while True:
    chute = int(input("Insira o seu chute: "))

    if chute > numeroSecreto:
        print("O chute foi muito alto")
        tentativas+=1
    elif chute < numeroSecreto:
        print("O chute foi muito baixo")
        tentativas+=1
    else:
        print(f"Você acertou o número secreto com {tentativas} tentativas")
        break
