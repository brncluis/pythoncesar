palavras = []

for i in range(5):
    palavras.append(input("Digite a palavra: ")) 
    ## ou
    # palavra = input("Digite a palavra: ")
    #palavras.apprend(palavra)
    palavras.sort()
    
for i in palavras:
    print(i)