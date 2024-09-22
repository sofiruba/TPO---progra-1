"""
Sistema de Evaluación Académica Crear un sistema de evaluación que utilice matrices para calificaciones, 
listas y diccionarios para gestionar estudiantes y materias,
"""
# Variables globales para la impresion
ancho = 50 
ancho_anuncio = 45
ramos = 0
# Funciones 

def eliminar_alumno(alumno, alumnos): 
    if alumno in alumnos:
        alumnos.pop(alumno) # Eliminar del diccionario
    else:
        print("No se encuentra el alumno")

def printflores(n):
    for i in range(n):
        print("✿", end=" ")

def eliminar_materia(alumno, materia, alumnos):
    if alumno in alumnos:
        if materia in alumnos[alumno]:
            alumnos[alumno].pop(materia)
        else:
            print("No se encuentra la materia")
    else:
        print("No se encuentra el alumno")

def display_notas_alumnos(alumnos):
    print (" ")
    printflores(1)
    print(" Listado de alumnos de Las Margaritas", end=" ")
    printflores(1)
    print("")
    print(f"{'Alumno':<10} {'Materia':<15} {'Notas':<25} {'Condición':<30}")
    print("-" * 60)

    for alumno, mats in alumnos.items():
        for mat, notas in mats.items():
            notas_str = ', '.join(map(str, notas[:-1]))  # Convertir  notas en string
            condicion = notas[-1]  # última posición 
            print(f"{alumno:<10} {mat:<15} {notas_str:<25} {condicion:<12}")
        print("-" * 60)

def mostrar_alumno(alumno, alumnos):
    if alumno not in alumnos:
        print("No se encuentra el alumno.")
    else:
        printflores(1)
        print(alumno, "Boletin académico")
        print("-" * 40)
        for materia in alumnos[alumno]:
            notas = alumnos[alumno][materia]
            print("Materia:", materia)
            print("Notas:", end=" ")
            for nota in notas[:-1]: 
                print(nota, end=" ")
            print()
            print("Condición:", notas[-1])
            print("-" * 40)

def imprimir_materia(materia, alumnos):
    print(f"{'Alumno':<10} {'Notas':<15} {'Condición':<25}")
    for alumno in alumnos:
        print("-" * 40)
        if materia in alumnos[alumno]:
            notas_str = ', '.join(map(str, alumnos[alumno][materia][:-1]))  # Convertimos las notas en string, excluyendo la condición
            condicion = alumnos[alumno][materia][-1]  # La última posición es la condición
            print(f"{alumno:<10} {notas_str:<15} {condicion:<15}")
            

def matriz_promedios(alumnos): 
    matriz = []
    for alumno in alumnos:
        fila = []
        for materia in alumnos[alumno]:
            notas = alumnos[alumno][materia][:-1]  # saco el ultimo indice
            if len(notas) > 0:
                promedio = round(sum(notas) / len(notas), 2)
            else:
                promedio = 0
            fila.append(promedio)
        matriz.append(fila)
    return matriz

def printmaterias(mats):
    printflores(10)

    for mat in mats:
        printflores(1)
        print( mat + " ".ljust(ancho - 14 - len(mat)) )
        printflores(1)
        print("")

    printflores(10)
    print(" ")

def cuadro_de_honor(alumnos):

    honor = []
    for alumno in alumnos: 
        materias = alumnos[alumno]  
        todas_aprobadas = True  # supongo que todas estan aprobadas
        for mat in materias:  
            notas = materias[mat]  
            condicion = notas[-1]  
            if condicion not in ["Promociona", "Aprobada"] and todas_aprobadas:
                todas_aprobadas = False  
        if todas_aprobadas:
            honor.append(alumno)  

    if honor:
        print ()
        print("✾ Cuadro de Honor  ✾ ".center(57))
        print("Las Margaritas felicita a...".center(57))
        for alumno in honor:  
            print(" ✾ ", alumno)
    else:
        print("No hay alumnos en el cuadro de honor.")

def mostrar_menu_con_anuncio():
    print ( )
    menu = [
        "a) ✿ Profesor".ljust(ancho - 12) + "✿",
        "b) ❀ Alumno".ljust(ancho - 12) + "❀".ljust(10),
        "c) ✾ Admin".ljust(ancho - 12) + "✾".ljust(10),
        "d) ✿ Ver grilla alumnos".ljust(ancho - 12) + "✿".ljust(10),
        "s) ✿ Salir".ljust(ancho - 12) + "✿".ljust(10),
    ]

    anuncio = [
        "✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿".center(ancho_anuncio + 5),
        "✿".ljust(1) +  "FLORES AMARILLAS".center(ancho_anuncio - 16)+ "✿",
        "✿".ljust(1) +  "DE LA PROMO".center(ancho_anuncio - 16)+ "✿",
        "✿".ljust(ancho_anuncio - 15) + "✿",
        "✿ f) Hacer pedido de flores".ljust(ancho_anuncio - 15) + "✿",
        
    ]

    decoracion_superior = "✿ ✿ ✿ ✿ ✿ ✿  MENÚ PRINCIPAL ✿ ✿ ✿ ✿ ✿ ✿"
    decoracion_inferior = "✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿"
    
    print(decoracion_superior)
    
    for i in range(len(menu)):
        print(menu[i].ljust(ancho - 12) + anuncio[i].ljust(10))

    print(decoracion_inferior)

def operacion_a():
    print (" ")
    print("✿ ✿ ✿ ✿ ✿ ✿ ❀  HOLA PROFE ❀ ✿ ✿ ✿ ✿ ✿ ✿")
    print("a) ✿ Ver materias".ljust(ancho - 12) + "✿")
    print("b) ❀ Ver promedios generales".ljust(ancho - 12) + "❀")
    print("c) ✿ Ver cuadro de honor".ljust(ancho - 12) + "✿")
    printflores(10)
    print(" ")
    op = input("Ingrese la operacion que desea realizar: ").lower()
    print(" ")
    if op == 'a':
        printmaterias(materias)
        materia = input("Ingrese la materia que desea ver: ").lower()
        print(" ")
        if materia in materias:
            imprimir_materia(materia, alumnos)
        else:
            print("No se encuentra la materia")
    elif op == 'b':
        matrizprom = matriz_promedios(alumnos)
        i = 0
        for alumno in alumnos:
            print(" ❀ Alumno: ", alumno)
            materias_alumno = list(alumnos[alumno].keys())  
            for j in range(len(matrizprom[i])):
                # veo si hay misma cantidad de materias en matrizprom y en materias_alumno
                if j < len(materias_alumno):
                    print("Materia: ", materias_alumno[j], end=" ")
                    print("Promedio: ", matrizprom[i][j])
                else:
                    print("Promedio no disponible para la materia: ", materias_alumno[j])
            i += 1

    elif op == 'c':
        print ("Al cuadro de honor se llega habiendo promocionado o aprobado todas las materias.")
        cuadro_de_honor(alumnos)
    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60))

def operacion_b(ramos):
    print(f"TIENEN {ramos} PARA PREPARAR")
    print("✾ Ingrese su nombre ✾".center(60))
    nombre = input().capitalize()
    mostrar_alumno(nombre, alumnos)

def operacion_c():
    print (" ")
    printflores(6)
    print("❀  HOLA ADMIN ❀ ")
    printflores(6)
    print(" ")
    print("a) ✿ Eliminar alumnos".ljust(ancho - 12) + "✿")
    print("b) ❀ Agregar alumnos".ljust(ancho - 12) + "❀")
    print("c) ❀ Eliminar alumno de materia".ljust(ancho - 12) + "❀")
    printflores(10)
    print(" ")
    op = input("Ingrese la operacion que desea realizar: ").lower()
    if op == "a":
        alumno = input("Ingrese el nombre del alumno que desea eliminar: ").capitalize()
        eliminar_alumno(alumno,alumnos)
        display_notas_alumnos(alumnos)

    elif op == "b":
        alumno = input("Ingrese el nombre del alumno que desea agregar: ").capitalize()
        printmaterias(materias)
        materias_alumno = []
        for materia in materias:
            print(materia, end=" ")
            agregar = input(" Desea agregar la materia? si/no: ").lower()
            opciones = ["si", "no"]
            while agregar not in opciones:
                print("Opción no válida. Intente de nuevo.")
                agregar = input("Desea agregar la materia? si/no: ").lower()
            if agregar == "si":
                materias_alumno.append(materia)

        alumnos[alumno] = {mat: [0,0,0,"en curso"] for mat in materias_alumno} # Inicializo como 0 todas las notas
        display_notas_alumnos(alumnos)

    elif op=="c":
        alumno = input("Ingrese el nombre del alumno que desea eliminar: ").capitalize()
        if alumno in alumnos: 
            materias_alumno = alumnos[alumno].keys() # materias del alumno
            printmaterias(materias_alumno)
            materia = input("Ingrese la materia que desea dar de baja: ").capitalize()
            if materia in materias_alumno:
                eliminar_materia(alumno, materia, alumnos)
            else:
                print("No se encuentra la materia")
            display_notas_alumnos(alumnos)
            print(" ")
        else:
            print("No se encuentra el alumno.")

    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60))     
    print(" ")


def operacion_f(ramos):
    flores = int(input("Ingrese la cantidad de ramos que desea: "))
    if flores > 0:
        print("Gracias por ordenar flores con nosotros!")
        ramos = flores
    else:
        ramos = 0
    return ramos
# PROGRAMA PRINCIPAL
alumnos = {
    "Ana": {
        "Matematicas": [8, 9, 8, "Promociona"],
        "Programacion": [3, 6, 4, "Previo"],
        "Literatura": [0, 0, 0,  "En curso"]
    },
    "Nicolas": {
        "Matematicas": [5, 8, 7, "Aprobada"],
        "Historia": [2, 5, 2, "Recursa"]
    },
    "Luciano": {
        "Historia": [9, 8, 8, "Promociona"],
        "Programacion": [9, 10, 9, "Aprobada"]
    },
    "Guadalupe": {
        "Matematicas": [9, 9, 9, "Promociona"],
        "Historia": [0, 0, 0, "En curso"],
        "Programacion": [5, 3, 3, "Recursa"],
        "Literatura": [4, 4, 6,  "Aprobada"]
    },
     "Julian": {
        "Historia": [2, 4, 3, "Recursa"],
        "Literatura": [5, 5, 5,  "Aprobada"]
    },
    "Francisco": {
        "Matematicas": [8, 8, 8, "Promociona"],
        "Historia": [9, 9, 9, "Promociona"]
    }
}

materias = ("Matematicas", "Historia", "Programacion", "Literatura")
condicion_alumno = ("Promociona", "Previo", "Reprobado", "Recursa", "Aprobada", "En curso")


print("❀ ❀ ❀ ❀ ❀ ❀".ljust(1) +  " ✿  Las Margaritas ✿ ".center(57)+ "❀ ❀ ❀ ❀ ❀ ❀",)


#Bucle del menú
continuar = True
while continuar:
    #mostrar_menu()
    mostrar_menu_con_anuncio()
    print(" ")
    opcion = input("Ingrese la operación que desea realizar: ").lower()
    
    if opcion == 'a':
        operacion_a()
    elif opcion == 'b':
        operacion_b(ramos)
    elif opcion == 'c':
        operacion_c()
    elif opcion == 'd':
        display_notas_alumnos(alumnos)
    elif opcion == 'f':
        ramos += operacion_f(ramos)

    elif opcion == 's':
        print("Saliendo del programa... ✿".center(60))
        continuar = False
    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60))
