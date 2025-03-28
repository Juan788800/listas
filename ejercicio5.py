#calcular la nota máxima y nota mínima de cada estudiante del curso de programación.
#Recordar que por cada estudiante al almacena 5 notas, las dos primeras son evaluaciones
#que equivalen al 30% de la nota final, la tercera y cuarta nota es de trabajos y equivale el 10%
#y la última nota es examen final que equivale al 60%. Al final por cada estudiante se debe
#mostrar su nombre, sus notas y su nota máxima y mínima. el curso está conformado por un
#total de 20 aprendices en total y con rango de notas que van de 1 al 10 en su escala.



import random

# Generar datos de 20 estudiantes con nombres y 5 notas cada uno
estudiantes = []
for i in range(1, 21):  # 20 estudiantes
    nombre = f"Estudiante {i}"
    notas = [random.randint(1, 10) for _ in range(5)]  # Notas entre 1 y 10
    estudiantes.append({"nombre": nombre, "notas": notas})

# Procesar cada estudiante
for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    notas = estudiante["notas"]
    
    nota_maxima = max(notas)
    nota_minima = min(notas)

    # Imprimir resultados
    print(f"Nombre: {nombre}")
    print(f"Notas: {notas}")
    print(f"Nota Máxima: {nota_maxima}")
    print(f"Nota Mínima: {nota_minima}")