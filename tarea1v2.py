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

######      1 a     #####
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

######      1 b     #####
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


# A la funcion que llamamos OBTENER_MAYOR_MENOR
# le pasamos como parametro el arreglo anteriormente calculado
# pero hace uso de esa informacion sin modificar sus datos como tal
# obtener_mayor_menor(promedio_estudiantes)
print(obtener_mayor_menor(promedio_estudiantes))

######      2     #####
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

######      3     #####
"""
3-¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?
"""
# def moda(notas):
