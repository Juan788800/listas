#generar dos listas de longitudes n y m, la primera lista ordenarla de manera ascendente y la
#segunda de manera descendente.

import random
listan=6
listam=6

# Generar listas con números aleatorios
lista1 = [random.randint(1, 100) for _ in range(listan)]
lista2 = [random.randint(1, 100) for _ in range(listam)]

# Ordenar lista1 en orden ascendente
lista1.sort()

# Ordenar lista2 en orden descendente
lista2.sort(reverse=True)

# Imprimir resultados
print("Lista 1 ordenada (ascendente):", lista1)
print("Lista 2 ordenada (descendente):", lista2)