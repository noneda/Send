from geopy.geocoders import Nominatim
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

#Ejercicio 3
print(f"\nEJercicio 3\n")
# Inicializar el geocodificador
geocoder = Nominatim(user_agent="city_coordinates")

# Diccionario para almacenar las coordenadas de las ciudades
ciudades = {}

# Lista de ciudades de ejemplo
lista_ciudades = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena']

# Obtener y almacenar las coordenadas de cada ciudad
for ciudad in lista_ciudades:
    location = geocoder.geocode(ciudad)
    if location:
        ciudades[ciudad] = (location.latitude, location.longitude)
    else:
        ciudades[ciudad] = (None, None)

# Solicitar al usuario que ingrese el nombre de una ciudad
ciudad_usuario = input("Ingrese el nombre de una ciudad: ")

# Buscar y mostrar las coordenadas de la ciudad ingresada
if ciudad_usuario in ciudades:
    latitud, longitud = ciudades[ciudad_usuario]
    if latitud and longitud:
        print(f"Las coordenadas de {ciudad_usuario} son: Latitud {latitud}, Longitud {longitud}")
    else:
        print(f"No se encontraron coordenadas para {ciudad_usuario}.")
else:
    print(f"{ciudad_usuario} no está en la lista de ciudades.")

print(f"\nEjercicio 4\n")

# Conjuntos de estudiantes que han aprobado cada asignatura
asignatura1 = {'Juan', 'María', 'Pedro', 'Ana'}
asignatura2 = {'Pedro', 'Ana', 'Luis', 'Sofía'}

# Estudiantes que han aprobado ambas asignaturas (intersección)
aprobados_ambas = asignatura1.intersection(asignatura2)
print("Estudiantes que han aprobado ambas asignaturas:", aprobados_ambas)

# Estudiantes que solo han aprobado una de las dos (diferencia simétrica)
aprobados_una = asignatura1.symmetric_difference(asignatura2)
print("Estudiantes que solo han aprobado una de las dos asignaturas:", aprobados_una)

print(f"\Ejecicio 5\n")

# Crear una lista de 25 estudiantes
estudiantes = []
for i in range(25):
    estudiante = {
        'nombre': f'Estudiante {i+1}',
        'edad': np.random.randint(18, 25),
        'notas': np.random.randint(0, 101, size=3).tolist()  # Tres calificaciones aleatorias entre 0 y 100
    }
    estudiantes.append(estudiante)

# Calcular y mostrar el promedio de notas de cada estudiante
for estudiante in estudiantes:
    notas = np.array(estudiante['notas'])
    promedio = np.mean(notas)
    print(f"{estudiante['nombre']} (Edad: {estudiante['edad']}) - Promedio de notas: {promedio:.2f}")
