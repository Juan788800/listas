#Almacenar una lista de números, identificar la longitud de la lista si es par: Los elementos
#invertir los elementos de la lista. Imprimir la lista original y lista invertida.

#definir una lista de numeros
numeros=[3, 8, 1, 6, 7, 4, 2, 9]
#lista originañ
print("lista original", numeros)
#verificar si la longitud de la lista es par
if len(numeros) %2 ==0:
    #invertir lista
    lista_invertida=numeros [::-1]
    #imprimir la lista invertida
    print(f"lista invertida: {lista_invertida}")
