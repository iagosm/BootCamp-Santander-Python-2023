carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)




for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


numeros = [1, 4,32, 10, 11, 45, 99]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
print(pares)
numeros2 = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


numeros = [1, 2, 3, 4, 5, 6]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    
print(quadrado)

numeros = [1, 2, 3, 4, 5, 6]
quadrado = [numero ** 2 for numero in numeros]
    
print(quadrado)
 