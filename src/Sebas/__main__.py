import numpy

#Se Crean las listas de nombres y edades
listaNombre = ["Juan1","Juan2", "Juan3","Juan4", "Juan5","Juan6", "Juan7","Juan8", "Juan9","Juan10", "Juan11","Juan12", "Juan13","Juan14", "Juan15"]
listaEdades = [12,21,45,56,5,24,51,15,18,19,20,21,24,24,45]

#listaNombre = numpy.array(listaEdades)
#listaEdades = numpy.array(listaNombre)
#Se crea la variable para el diccionario
dicc = {}

cont = 0
#Recorro las listas con zip y luego asigno como llave un indice y valores el nombre y edad
for n, e in zip(listaNombre, listaEdades):
    dicc[cont] = [n, e]
    cont += 1

#print("Diccionario \n", dicc)
cont = 0
print("\nMayores a 30\n")
#Recorro la listas y verifico cual es mayor de 30 con numpy greater(value, condition)
for n, e in zip(listaNombre, listaEdades):
    if numpy.greater(dicc[cont][1], 30):
        print(f"{dicc[cont][0]} Edad {dicc[cont][1]}")
    cont += 1
print("\nMayores a 40 Menores a 15\n")
cont = 0
#Recorro la listas y verifico cual es mayor a 40 con numpy greater(value, condition) y menor a 15 con numpy less(value, condiion)
for n, e in zip(listaNombre, listaEdades):
    if numpy.greater(dicc[cont][1], 40) or numpy.less(dicc[cont][1], 15):
        print(f"{dicc[cont][0]} Edad {dicc[cont][1]}")
    cont += 1
#print(dict(zip(listaNombre, listaEdades)))

print("\nParte 2\n")

listaNumero = []

for i in range(0 , 20, 1):
    listaNumero.append(numpy.random.randint(1, 100))

listaNumero = numpy.array(listaNumero)

mediana = numpy.median(listaNumero)
minimo = numpy.amin(listaNumero)
maximo = numpy.amax(listaNumero)
potencia = numpy.pow(listaNumero, 2)

print(f"\nMediana:  {mediana}\nMinimo: {minimo}\nMaximo: {maximo}\nPotencias: {potencia}")