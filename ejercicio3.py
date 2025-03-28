#Almacenar dos listos de números enteros, lista1 y lista2, y generar la tercera lista con los
#siguientes criterios: Sumar el primer elemento de la lista1 con el último elemento de la lista2 

#guardar el resultado en la lista3, luego el segundo elemento de la lista1 sumarlo con el noveno
#elemento de la lista2. Al final imprimir las tres listas.

#definir dos listas
lista1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#lista 3 donde se almacenaran los datos
lista3=[]

# Recorrer lista1 y sumar con los elementos de lista2 en orden inverso
for i in range(len(lista1)):
    suma = lista1[i] + lista2[-(i+1)]  # Sumar elemento i de lista1 con el elemento inverso de lista2
    lista3.append(suma)

# Imprimir las listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3 (suma de elementos):", lista3)