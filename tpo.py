"""
Sistema de Evaluación Académica Crear un sistema de evaluación que utilice matrices para calificaciones, 
listas y dic cionarios para gestionar estudiantes y materias,
"""
def promocione(lista):
    if lista[0] >=8 and lista[1] >= 8: return True
    else: return False

def recurse(lista):
    if lista[0] <4 and lista[1] < 4: return True
    else: return False

def promedio(lista):
    return sum(lista)/len(lista)

def notavalida(nota):
    while nota < 0 or nota > 10:
       nota = int(input("ingrese una nota valida"))
    return nota

alumnos = {
    "ana": {
        "matematicas": [8, 9, 8, "promociona"],
        "programacion": [3, 6, 4, "previo"],
        "repre": [0, 0, 0, 0,  "reprobado"]
    },
    "carlos": {
        "matematicas": [5, 8, 7, "promociona"],
        "historia": [2, 5, 2, "recursa"]
    },
    "lucia": {
        "historia": [9, 8, 8, "promociona"],
        "programacion": [9, 10, 9, "aprobada"]
    }
}

materias = ("matematicas", "historia", "programacion", "repre")
condicion_alumno = ("promociona", "previo", "reprobado", "recursa", "aprobada")

def display_notas_alumnos(students_data):
    # Print header
    print(f"{'Student':<10} {'Subject':<15} {'Grades':<25} {'Condition':<12}")
    print("-" * 60)
    
    # Print student grades
    for student, subjects in students_data.items():
        for subject, grades in subjects.items():
            grades_str = ', '.join(map(str, grades[:-1]))  # Convertimos las notas en string, excluyendo la condición
            condition = grades[-1]  # La última posición es la condición
            print(f"{student:<10} {subject:<15} {grades_str:<25} {condition:<12}")
        print("-" * 60)

def mostrar_alumno(alumno, alumnos):
    if alumno not in alumnos:
        print("no se encuentra el alumno")
    else:
        print(alumnos[alumno])

def imprimir_materia(materia, alumnos):
    for alumno in alumnos:
        if materia in alumnos[alumno]:
            print("Alumno: ", alumno)
            print(alumnos[alumno][materia])

def matriz_promedios(alumnos):
    matriz = []
    for alumno in alumnos:
        fila = []
        for materia in alumnos[alumno]:
            i = 0
            sum = 0
            for notas in alumnos[alumno][materia]:
                if str(notas).isnumeric() :
                    sum = sum + notas
                    i = i + 1
            promedio = sum/i
            fila.append(promedio)
        matriz.append(fila)
    return matriz

def matriz_resultados(alumnos):
    matriz = []
    for alumno in alumnos:
        fila = []
        for materia in alumnos[alumno]:
            for notas in alumnos[alumno][materia]:
                if not str(notas).isnumeric() :
                    fila.append(notas)
        matriz.append(fila)
    return matriz

ancho = 50 
def mostrar_menu():
 # Ancho del "cubo", lo ajustamos para que la decoración superior e inferior sea igual
    print()
    decoracion_superior = "✿ ✿ ✿ ✿ ✿ ✿  MENÚ PRINCIPAL ✿ ✿ ✿ ✿ ✿ ✿"
    decoracion_inferior = "✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿"
    flor = "✿"
    opciones = []
    # Mostramos las decoraciones y el menú
    print(decoracion_superior)
    print("a) ✿ profesor".ljust(ancho - 12) + "✿")
    print("b) ❀ alumno".ljust(ancho - 12) + "❀")
    print("c) ✾ admin (proximamente..)".ljust(ancho - 12) + "✾")
    print("d) ✿ Ver grilla alumnos".ljust(ancho - 12) + "✿")
    print("s) ✿ Salir".ljust(ancho - 12) + "✿")
    
    print(decoracion_inferior)

def operacion_a():
    print("❀ Hola profe ❀".center(60))
    print("a) ✿ Ver materias".ljust(ancho - 12) + "✿")
    print("b) ❀ Ver promedios generales".ljust(ancho - 12) + "❀")
    print("c) ❀ Ver resultados globales".ljust(ancho - 12) + "❀")

    op = input("ingrese la operacion que desea realizar: ").lower()
    if op == 'a':
        for mat in materias:
            print("│ ✿ "+ mat + "                         ✿".center(ancho))
        materia = input("ingrese la materia que desea ver: ").lower()
        if materia in materias:
            imprimir_materia(materia, alumnos)
        else:
            print("no se encuentra la materia")
    elif op == 'b':
        matrizprom = matriz_promedios(alumnos)
        i = 0
        for alumno in alumnos:
            print("Alumno: ", alumno)

            print("Promedio general: ", matrizprom[i])
            i = i + 1
    elif op == 'c':
        matrizres =matriz_resultados(alumnos)
        print(matrizres)
    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60))




def operacion_b():
    print("✾ Ingrese su nombre ✾".center(60))
    nombre = input().lower
    mostrar_alumno(nombre, alumnos)

def operacion_c():
    print("✿ Has seleccionado la operación C ✿".center(60))

# Bucle del menú
while True:
    mostrar_menu()
    print(" ")
    opcion = input("Seleccione una opción: ").lower()

    if opcion == 'a':
        operacion_a()
    elif opcion == 'b':
        operacion_b()
    elif opcion == 'c':
        operacion_c()
    elif opcion == 'd':
        display_notas_alumnos(alumnos)
    elif opcion == 's':
        print("Saliendo del programa... ✿".center(60))
        break
    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60))
