""" 
1- Calcula el promedio de notas de cada estudiante y determina quién tiene el promedio más alto y más bajo. ✅
2- Cuenta cuántos estudiantes aprobaron todas sus asignaturas (todas las notas >= 4.0). ✅
3-¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?
4-¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
5- Entrega un listado ordenado (de mayor a menor) de los estudiantes según su promedio. 
"""

estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
    {"nombre": "Luis", "notas": [4.2, 5.1, 6.0]},
    {"nombre": "Sofía", "notas": [3.9, 4.0, 4.5]},
    {"nombre": "Pedro", "notas": [5.5, 6.1, 5.9]},
    {"nombre": "Valentina", "notas": [7.0, 6.8, 6.9]},
    {"nombre": "Javier", "notas": [4.0, 4.2, 4.1]},
    {"nombre": "Camila", "notas": [5.0, 5.5, 5.8]},
    {"nombre": "Martín", "notas": [3.5, 4.0, 4.2]},
    {"nombre": "Fernanda", "notas": [6.2, 6.5, 6.0]},
    {"nombre": "Tomás", "notas": [4.8, 5.0, 5.2]},
    {"nombre": "Josefa", "notas": [5.9, 6.0, 6.1]},
    {"nombre": "Matías", "notas": [3.8, 4.1, 4.0]},
    {"nombre": "Ignacio", "notas": [6.7, 6.9, 7.0]},
    {"nombre": "Daniela", "notas": [5.2, 5.4, 5.6]},
    {"nombre": "Sebastián", "notas": [4.3, 4.5, 4.7]}
]

#Esto seria un arreglo generico para el calculo de promedios
prom_Estudiantes = []

todos_los_promedios = []

#Este arreglo es para mostrar los alumnos con la condicion del 2do problema
alumnos_con_todas_las_notas_arriba_de_cuatro = []

contador_aprobados_todas_las_asignaturas = 0

for estudiante in estudiantes:
    ########################################################
    #                    Pregunta 1                        #
    ########################################################
    #Con esto capturo el nombre de CADA estudiante
    nombre_Estudiante = estudiante["nombre"]
    #1era forma de calular el promedio de CADA estudiante
    prom_Estudiante = round((estudiante["notas"][0]+estudiante["notas"][1]+estudiante["notas"][2])/len(estudiante["notas"]),1)
    #Generamos un objeto (igual a los de el arreglo estudiante), pero con la propiedad "promedio" para CADA estudiante
    alumno_con_promedio = {"nombre": nombre_Estudiante, "promedio": prom_Estudiante}
    #Agregar cada objeto creado al arreglo prom_Estudiantes
    prom_Estudiantes.append(alumno_con_promedio)
    print(alumno_con_promedio)
    #Agraga los valores numericos en un arreglo separado
    todos_los_promedios.append(prom_Estudiante)
    ########################################################
    #                    Pregunta 2                        #
    ########################################################
    if(estudiante["notas"][0] >= 4.0 and estudiante["notas"][1] >= 4.0 and estudiante["notas"][2] >= 4.0):
        alumnos_con_todas_las_notas_arriba_de_cuatro.append(estudiante)
        contador_aprobados_todas_las_asignaturas = contador_aprobados_todas_las_asignaturas + 1
        

########################################################
#                    Pregunta 1                        #
########################################################
promedio_min = min(todos_los_promedios)
promedio_max = max(todos_los_promedios)

# print("los alumnos con el promedio mas alto y bajo son:")

alumnos_con_promedio_min = []

alumnos_con_promedio_max = []


for alumno_actual in prom_Estudiantes:
    if(alumno_actual["promedio"] == promedio_min):
        alumnos_con_promedio_min.append(alumno_actual)
    if(alumno_actual["promedio"] == promedio_max):
        alumnos_con_promedio_max.append(alumno_actual)
        
        
print("########################################################")
print("#                 Respuesta pregunta 1                 #")
print("########################################################")

#print("Promedio de cada estudiante:")
print(f"Promedio mas bajo: {promedio_min}, lo tienen: {alumnos_con_promedio_min}")
print(f"Promedio mas alto: {promedio_max}, lo tienen: {alumnos_con_promedio_max}")

print("########################################################")
print("#                 Respuesta pregunta 2                 #")
print("########################################################")
print("Los estudiantes que aprobaron todas sus materias son:")
for alumno_arriba_de_cuatro in alumnos_con_todas_las_notas_arriba_de_cuatro:
    print(alumno_arriba_de_cuatro)
print(f"La cantidad de estudiantes que aprobaron todas sus materias es: {contador_aprobados_todas_las_asignaturas}")
