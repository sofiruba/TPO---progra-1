"""
Sistema de Evaluación Académica Crear un sistema de evaluación que utilice matrices para calificaciones, 
listas y diccionarios para gestionar estudiantes y materias,
"""

def eliminar_alumno(alumno, alumnos):
    if alumno in alumnos:
        alumnos.pop(alumno)
    else:
        print("no se encuentra el alumno")

def eliminar_materia(alumno, materia, alumnos):
    if alumno in alumnos:
        if materia in alumnos[alumno]:
            alumnos[alumno].pop(materia)
        else:
            print("no se encuentra la materia")
    else:
        print("no se encuentra el alumno")

def promociones(matriz):
    mats = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == "promociona":
                suma = suma + 1
        mats.append(suma)
    return mats

def aprobados(matriz):
    mats = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == "aprobada":
                suma = suma + 1
        mats.append(suma)
    return mats

def reprobados(matriz):
    mats = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == "reprobado":
                suma = suma + 1
        mats.append(suma)
    return mats

def previos(matriz):
    mats = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == "previo":
                suma = suma + 1
        mats.append(suma)
    return mats

def en_curso(matriz):
    mats = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == "en curso":
                suma = suma + 1
        mats.append(suma)
    return mats

alumnos = {
    "ana": {
        "matematicas": [8, 9, 8, "promociona"],
        "programacion": [3, 6, 4, "previo"],
        "literatura": [0, 0, 0,  "en curso"]
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

materias = ("matematicas", "historia", "programacion", "literatura")
condicion_alumno = ("promociona", "previo", "reprobado", "recursa", "aprobada", "en curso")

def display_notas_alumnos(alumnos_data):

    print(f"{'Alumno':<10} {'Materia':<15} {'Notas':<25} {'Condición':<30}")
    print("-" * 60)

    for alumno, mats in alumnos_data.items():
        for mat, notas in mats.items():
            notas_str = ', '.join(map(str, notas[:-1]))  # Convertir  notas en string, excluyendo la condición
            condicion = notas[-1]  # La última posición es la condición
            print(f"{alumno:<10} {mat:<15} {notas_str:<25} {condicion:<12}")
        print("-" * 60)
        


def mostrar_alumno(alumno, alumnos):
    if alumno not in alumnos:
        print("no se encuentra el alumno")
    else:
        print(alumnos[alumno])

def imprimir_materia(materia, alumnos):
    print(f"{'Alumno':<10} {'Notas':<15} {'Condición':<25}")
    for alumno in alumnos:
        if materia in alumnos[alumno]:
            print("-" * 40)
            notas_str = ', '.join(map(str, alumnos[alumno][materia][:-1]))  # Convertimos las notas en string, excluyendo la condición
            condicion = alumnos[alumno][materia][-1]  # La última posición es la condición
            print(f"{alumno:<10} {notas_str:<15} {condicion:<15}")
            

def matriz_promedios(alumnos): # Genera una matriz de los promedios de cada alumno en cada materia
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
            promedio = round(sum/i, 2)
            fila.append(promedio)
        matriz.append(fila)
    return matriz

def matriz_resultados(alumnos): #Genera una matriz con las condiciones de los alumnos en cada materia
    matriz = []
    for alumno in alumnos:
        fila = []
        for materia in alumnos[alumno]:
            for notas in alumnos[alumno][materia]:
                if not str(notas).isnumeric() :
                    fila.append(notas)
        matriz.append(fila)
    return matriz

def printmaterias(mats):
    print("✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿")
    for mat in mats:
            print("✿ "+ mat + " ".ljust(ancho - 14 - len(mat)) + "❀")
    print("✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿")
    print(" ")

ancho = 50 
def mostrar_menu():
 # Ancho del "cubo", lo ajustamos para que la decoración superior e inferior sea igual
    print()
    decoracion_superior = "✿ ✿ ✿ ✿ ✿ ✿  MENÚ PRINCIPAL ✿ ✿ ✿ ✿ ✿ ✿"
    decoracion_inferior = "✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿"
    # Mostramos las decoraciones y el menú
    print(decoracion_superior)
    print("a) ✿ profesor".ljust(ancho - 12) + "✿")
    print("b) ❀ alumno".ljust(ancho - 12) + "❀")
    print("c) ✾ admin".ljust(ancho - 12) + "✾")
    print("d) ✿ Ver grilla alumnos".ljust(ancho - 12) + "✿")
    print("s) ✿ Salir".ljust(ancho - 12) + "✿")
    print(decoracion_inferior)

def operacion_a():
    print("✿ ✿ ✿ ✿ ✿ ✿ ❀  HOLA PROFE ❀ ✿ ✿ ✿ ✿ ✿ ✿")
    print("a) ✿ Ver materias".ljust(ancho - 12) + "✿")
    print("b) ❀ Ver promedios generales".ljust(ancho - 12) + "❀")
    print("c) ❀ Ver resultados globales".ljust(ancho - 12) + "❀")
    print("✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿")
    print(" ")
    op = input("ingrese la operacion que desea realizar: ").lower()
    print(" ")
    if op == 'a':
        printmaterias(materias)
        materia = input("ingrese la materia que desea ver: ").lower()
        print(" ")
        if materia in materias:
            imprimir_materia(materia, alumnos)
        else:
            print("no se encuentra la materia")
    elif op == 'b':
        matrizprom = matriz_promedios(alumnos)
        i = 0
        for alumno in alumnos:
            print("Alumno: ", alumno, end=" ")
            for j in range(len(matrizprom[i])):
                print("Materia: ", materias[j], end=" ")
                print("Promedio: ", matrizprom[i][j])

            i = i + 1
    elif op == 'c':
        matrizres =matriz_resultados(alumnos)
        for i in range (len(matrizres)):
            print("Materia: ", [i], end=" ")
            print("Promociones: ", promociones(matrizres)[i], end=" ")
            print("Aprobados: ", aprobados(matrizres)[i], end=" ")
            print("Reprobados: ", reprobados(matrizres)[i], end=" ")
            print("Previos: ", previos(matrizres)[i], end=" ")
            print("En curso: ", en_curso(matrizres)[i])
    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60))

def operacion_b():
    print("✾ Ingrese su nombre ✾".center(60))
    nombre = input()
    mostrar_alumno(nombre, alumnos)

def operacion_c():
    print("✿ ✿ ✿ ✿ ✿ ✿ ❀  HOLA ADMIN ❀ ✿ ✿ ✿ ✿ ✿ ✿")
    print("a) ✿ Eliminar alumnos".ljust(ancho - 12) + "✿")
    print("b) ❀ Agregar alumnos".ljust(ancho - 12) + "❀")
    print("c) ❀ Eliminar alumno de materia".ljust(ancho - 12) + "❀")
    print("✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿")
    print(" ")
    op = input("ingrese la operacion que desea realizar: ").lower()
    if op == "a":
        alumno = input("ingrese el nombre del alumno que desea eliminar: ")
        eliminar_alumno(alumno,alumnos)
        display_notas_alumnos(alumnos)

    elif op == "b":
        alumno = input("ingrese el nombre del alumno que desea agregar: ")
        printmaterias(materias)
        materias_alumno = []
        for materia in materias:
            print(materia, end=" ")
            agregar = input(" desea agregar la materia? s/n: ").lower()
            if agregar == "s":
                materias_alumno.append(materia)

        alumnos[alumno] = {mat: [0,0,0,"en curso"] for mat in materias_alumno}
        display_notas_alumnos(alumnos)

    elif op=="c":
        alumno = input("ingrese el nombre del alumno que desea eliminar: ")
        materias_alumno = alumnos[alumno].keys() # materias del alumno
        printmaterias(materias_alumno)
        materia = input("ingrese la materia que desea ver: ").lower()
        if materia in materias:
            eliminar_materia(alumno, materia, alumnos)
        else:
            print("no se encuentra la materia")
        display_notas_alumnos(alumnos)
        print(" ")

    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60))     
    print(" ")

# Bucle del menú
continuar = True
while continuar:
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
        continuar = False
    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60))
