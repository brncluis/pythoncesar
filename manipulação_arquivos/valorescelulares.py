valores_celular = [1200, 3000, 4000, 10.000]

# "r" usado para ler algo
# "w" usado para somente escrever algo
# "r+" usado para ler e escrever algo ao final
# "a" usado para acrescentar algo (append)

with open("celulares.txt", "w") as arquivo:
    for valor in valores_celular:
        arquivo.write(str(valor) + "\n")
        
