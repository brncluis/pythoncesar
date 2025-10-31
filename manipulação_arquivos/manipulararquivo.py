#file = open("arquivo.txt" , "a") #append, poe na ultima linha
#file = open("arquivo.txt", "w") #apaga e reescreve o arquivo com o que foi inserido

nomes_completos = []

file = open("arquivo.txt2", "w")
for i in range(5):
    nome = input()
    sobrenome = input()
    #file.write(nome + " " + sobrenome + "\n")

arquivo = open("arquivo2.txt")
arquivo.writelines("\n".join(nomes_completos) + "\n")
arquivo.close()