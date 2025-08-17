"""
1- Calcula el promedio de notas de cada estudiante y determina quién tiene el promedio más alto y más bajo.
2- Cuenta cuántos estudiantes aprobaron todas sus asignaturas (todas las notas >= 4.0).
3-¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?
4-¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
5- Entrega un listado ordenado (de mayor a menor) de los estudiantes según su promedio.
"""

estudiantes = [
    {"nombre": "Alicia", "notas": [5.8, 7.0, 4.0]},
    {"nombre": "Tomas", "notas": [5.0, 4.1, 1.2]},
    {"nombre": "Benjamin", "notas": [3.4, 5.5, 2.2]},
    {"nombre": "Eliseo", "notas": [3.4, 4.1, 1.2]},
    {"nombre": "Carolaine", "notas": [2.3, 7.0, 4.0]},
    {"nombre": "Solis", "notas": [5.0, 4.1, 1.2]},
    {"nombre": "Hernan", "notas": [5.8, 7.0, 1.0]},
    {"nombre": "Diego", "notas": [5.0, 6.1, 7.0]},
]

######!      1 a     #####
"""1- Calcula el promedio de notas de cada estudiante"""
# Solamente hace el calculo de los promedios
def promedios(estudiantes):
    if len(estudiantes) == 0:
        exit
    # lista limpia
    prom_estudiantes = []

    for estudiante in estudiantes:
        # if(estudiante["nombre"] == "Eliseo"):
        promedio = round(sum(estudiante["notas"]) / len(estudiante["notas"]), 1)
        prom_estudiantes.append({"nombre": estudiante["nombre"], "promedio": promedio})
    return prom_estudiantes

# lo que se le asigna es el retorno (lo que devolvera) la funcion promedios(estudiantes)
# devuelve un arreglo/lista de objetos con propiedades(nombre y promedio)
promedio_estudiantes = promedios(estudiantes)
print(promedio_estudiantes)

######!      1 b     #####
"""determina quién tiene el promedio más alto y más bajo."""
# Hace el calculo de min y max (promedios)
def obtener_mayor_menor(lista_de_promedios):
    # validacion de lista vacia
    if len(lista_de_promedios) == 0:
        exit
    # nueva lista vacia
    promedios = []

    for promedio_a_evaluar in lista_de_promedios:
        # LA PROPIEDAD "PROMEDIO" DEL OBJ PERTENECIENTE AL ARREGLO/LISTA LLAMADO LISTA DE PROMEDIOS
        promedios.append(promedio_a_evaluar["promedio"])
    nota_min = min(promedios)
    nota_max = max(promedios)
    return nota_min, nota_max


# !A la funcion que llamamos OBTENER_MAYOR_MENOR
# !le pasamos como parametro el arreglo anteriormente calculado
# !pero hace uso de esa informacion sin modificar sus datos como tal
# !obtener_mayor_menor(promedio_estudiantes)
print(obtener_mayor_menor(promedio_estudiantes))

######!      2     #####
"""
2- Cuenta cuántos estudiantes aprobaron todas sus asignaturas (todas las notas >= 4.0).
"""


def contar_de_aprobados(alumnos):
    # validador
    if len(alumnos) == 0:
        exit
    # lista vacia que contendra todos los alumnos aprobados
    aprobados = []
    for alumno in alumnos:
        # Compara las notas de cada asignatura que cumplan nota >= 4.0
        if (
            alumno["notas"][0] >= 4.0
            and alumno["notas"][1] >= 4.0
            and alumno["notas"][2] >= 4.0
        ):
            aprobados.append(alumno)
    cantidad_de_alumnos = len(aprobados)
    return cantidad_de_alumnos


print(contar_de_aprobados(estudiantes))

######!      3     #####
"""
!3-¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?
"""
"""
Ejemplo para poder entender los 2 FOR  acontinuacion

estudiantes = [
    {"nombre": "Alicia", "notas": [5.8, 7.0, 4.0]},
    {"nombre": "Tomas", "notas": [5.0, 4.1, 1.2]},
]
    
    lo que se implemento es recorrer un for por cada estudiante
    y dentro de ese recorrido se vuelven a recorrer las notas de ese estudiante
    para así obtener solo un arreglo/lista de todas las notas"""

#! para no cometer un recorrido poco eficiente como este :
#? notas_del_diccionario.append([nota])
#! lo que hace es recorrer un arreglo dentro de otro arreglo

#* Agrupar todas las notas de los estudiantes en un solo arreglo
def generar_arreglo_de_notas(estudiantes):
    #* Paso 1): Se genera un arreglo vacio para ir agregando las notas
    notas_del_diccionario = []
    #* Paso 2): Se comienza a recorrer cada uno de los estudiantes del arreglo estudiantes
    for estudiante in estudiantes:
        #* Paso 3): Dentro de cada estudiante se recorre el arreglo de notas
        for nota in estudiante["notas"]:
            #* Paso 4): Se va agregando al arreglo del Paso 1) las notas de cada estudiante 1 por 1
            notas_del_diccionario.append(nota)
    #* Paso 5): Se retorna finalmente las notas en formato de arreglo []
    return notas_del_diccionario
    
def obtener_moda():
    
    #* Se crea un objeto vacio
    repeticiones_de_notas = {}
    
    for nota in generar_arreglo_de_notas(estudiantes):
        if(nota in repeticiones_de_notas):
            repeticiones_de_notas[nota] = repeticiones_de_notas[nota] + 1
        else:
            repeticiones_de_notas[nota] = 1
            
    frecuencia_mas_alta = max(repeticiones_de_notas.values())
    moda = []
    for key_nota,value_frecuencia in repeticiones_de_notas.items():
        if frecuencia_mas_alta == value_frecuencia:
            moda.append(key_nota)
    return moda
print(obtener_moda())

######!      4     #####
""" 4-¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0? """
"""
estudiantes = [
    {"nombre": "Alicia", "notas": [5.8, 7.0, 4.0]},
    {"nombre": "Tomas", "notas": [5.0, 4.1, 1.2]},
]
"""
"""
    Se crea una funcion la cual permitira obtener el porcentaje de alumnos, que en sus notas
    tengan al menos una nota menor a 4.0, para esto, se itera en cada uno de los estudiantes,
    y a su vez, se itera dentro de cada una de las notas del estudiante iterado, para consultar
    si en alguna posicion de hay alguna nota menor a 4.
"""
def obtener_porcentajes_de_alumnos_con_alguna_nota_menor_a_4(estudiantes):
    #* Paso 1): se crea una variable la cual llevara el conteo de alumnos que cumplan esa condicion
    cantidad_de_alumnos = 0
    #* Paso 2): se recorre la lista de estudiantes para poder luego iterar en sus notas
    for estudiante in estudiantes:
        #* Paso 3): se recorre la lista de notas de cada estudiante para realizar la consulta de < 4.0
        for nota in estudiante["notas"]:
            #* Paso 4): condicional para verificar si la nota en la cual se esta evaluando es menor a 4.0
            if nota < 4.0 :
                #* Paso 5): se va incrementando la cantidad si se cumple esta condicion
                cantidad_de_alumnos = cantidad_de_alumnos + 1
                #* Paso 6): se agrega un break, para salir de la iteracion mas anidada, debido a que 
                #*          si hay 2 notas < a 4.0 duplicara el conteo de ese alumno.
                break
    #* Paso 7): se crea la variable que se retornara con el porcentaje calculado de alumnos con
    #*          nota < 4.0
    porcentaje = round((cantidad_de_alumnos/len(estudiantes))*100,1)
    return porcentaje
print(f"{obtener_porcentajes_de_alumnos_con_alguna_nota_menor_a_4(estudiantes)}%")

######!      5     #####
""" 5- Entrega un listado ordenado (de mayor a menor) de los estudiantes según su promedio. """
"""
estudiantes = [
    {"nombre": "Alicia", "notas": [5.8, 7.0, 4.0]},
    {"nombre": "Tomas", "notas": [5.0, 4.1, 1.2]},
]
"""
"""
    Se crea una funcion la cual se encarga de reordenar la lista de estudiantes segun su promedio
    para esto se utiliza una funcion creada en el problema 1, la cual estructura esta lista 
    con el nombre y el promedio de cada estudiante
"""
def ordenar_promedios_mayor_a_menor():
    #* paso 1: Se crea una variable que se le asigna la lista de promedios y nombres
    #*creada en el problema 1, lo que se hace es utilizar algo ya creado
    ordena_mayor_menor = promedios(estudiantes)
    #* paso 2: Se aplica una funcion interna de python para ordenar esta lista de mayor a menor
    #* esta funcion utiliza el parametro "key=lamnda" para darle a entender que parametro
    #* de los elementos de la lista se ultilizara para ordenar, despues recibe otro parametro
    #* llamado reverse el cual es un booleano para saber si se quiere mayor a menor o al reves
    ordena_mayor_menor.sort(key=lambda alumno : alumno["promedio"], reverse=True)
    #* paso 3: finalmente se itera cada elemnto de la lista para poder ver en consola mas ordenado
    for x in ordena_mayor_menor:
        print (x)
ordenar_promedios_mayor_a_menor()