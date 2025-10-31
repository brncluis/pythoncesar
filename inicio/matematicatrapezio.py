e = 2.7182
resultados = []
a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
n = int(input("Insira o valor de N: "))

imgA = e**(a**2)
imgB = e**(b**2)
deltaX = (b - a) / n

for i in range(1, n):
    resultado = e ** ((a + i * deltaX) ** 2)
    resultados.append(resultado)

soma_resultado = sum(resultados)

areatrap = (deltaX / 2) * ((imgA + imgB) + ( 2 * soma_resultado))

print(areatrap)