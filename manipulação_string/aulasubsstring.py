import os;os.system('cls')
frase = input("Insira a frase: ")
palavraexistente = input("Qual palavra deseja substituir? ")
if palavraexistente not in frase:
    print("Palavra não está na frase.")
else:
    palavraadicionar = input("Qual palavra deseja adicionar? ")

frasemodificada = frase.replace(palavraexistente,palavraadicionar)

print(frasemodificada.upper())