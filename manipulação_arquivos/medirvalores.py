valores = []

for i in range(4):
    valor_medida = input("Insira os valores: ")
    valores.append(valor_medida)

with open("valores_medir.txt", "w") as arquivo:
    for valor in valores:
        arquivo.write(str(valor) + "\n")

valor_arquivo = []

with open("valores_medir.txt", "r") as arquivo:
    for escrito in arquivo:
        valor_dentro_do_arquivo = arquivo.readlines()
        for valor in valor_dentro_do_arquivo:
            print(valor)

valor_em_inteiro = []

for numeros in valor:
    numeros = int(numeros)
    valor_em_inteiro.append(numeros)

maiores = 0

for numeros in valor_em_inteiro:
    if numeros > maiores:
        maiores = maiores + 1

print(maiores)

    
