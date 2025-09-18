import os;os.system('cls')
palavras = []

for i in range(5):
    palavra = input("Digite as palavras: ")
    palavras.append(palavra)

palavras.sort()
print(palavras)