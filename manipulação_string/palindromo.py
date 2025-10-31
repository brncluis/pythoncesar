import os;os.system('cls')
frase = input("Insira a frase: ")

frase = frase.replace(" ","").upper()
polindromo = frase[::-1]

if frase == polindromo:
    print("É palindromo")
else:
    print("Não é palindromo")