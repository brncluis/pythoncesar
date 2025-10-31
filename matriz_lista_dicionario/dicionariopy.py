valores = {}

numeros = int(input())

for i in range(5):
    chave = int(input("Insira o valor: "))
    valor = chave * chave

    valores[chave] = valor

print(valores)