estante = []

while True:
    resp = str(input("Defina sua ação: "))

    if resp == "P":
        print(estante)
    elif resp == "A":
        titulo = input("Nome do livro: ")
        estante.append(titulo)
    elif resp == "E":
        casa = int(input("Insira a casa para exlcuir: "))
        estante.pop(casa)
    elif resp == "Sair":
        break     