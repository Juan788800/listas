#imprimir la suma de números positivos y suma de números negativos.

#lista de numeros
lista_numeros=[3, -5, 0, 7, -2, 4, 0, -9, 8, -1, 0, 6, -4, 2, -7]
#contadores

ceros=0
positivo=0
negativo=0

#inciamos variables para las sumas de numeros positivos y negativos

suma_positiva=0
suma_negativa=0

#inciamos un lista para q imprima los ceros numeros positivos numero negativos y la suma de positivos y suma de negativos

for num in lista_numeros:
    if num ==0:                 #si el numero es cero
        ceros+=1
    elif num >1:
        positivo+=1              #si el numero es positivo
        suma_positiva+=num
    else:
        negativo+=1             # si el numero es negativo
        suma_negativa+=num


#imprimir los resultados

print(f"cantidad de ceros: {ceros}")
print(f"cantidad de positivos: {positivo}")
print(f"cantidad de negativos: {negativo}")
print(f"suma de positivos: {suma_positiva}")
print(f"suma de negativos {suma_negativa}")