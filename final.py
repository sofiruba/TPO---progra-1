import json
# FUNCIONES

def eliminar_alumno(alumno, alumnos):  # Eliminar alumno del diccionario
    if alumno in alumnos:
        alumnos.pop(alumno) 
    else:
        print("No se encuentra el alumno")

def display_notas_alumnos(alumnos):  # Imprime listado de alumnos con sus notas
    print("Listado de alumnos de Las Margaritas")
    print(f"{'Alumno':<10} {'Materia':<15} {'Notas':<25} {'Condición':<30}")
    print("-" * 60)

    for alumno, mats in alumnos.items():
        for mat, notas in mats.items():
            notas_str = ', '.join(map(str, notas[:-1]))  # Convertir notas en string
            condicion = notas[-1]  # última posición
            print(f"{alumno:<10} {mat:<15} {notas_str:<25} {condicion:<12}")
        print("-" * 60)

def mostrar_alumno(alumno, alumnos):  # Imprimir boletín académico de alumno
    if alumno not in alumnos:
        print("No se encuentra el alumno.")
    else:
        print(f"{alumno} - Boletín académico")
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

def imprimir_materia(materia, alumnos):  # Imprimir datos de una materia
    print(f"{'Alumno':<10} {'Notas':<15} {'Condición':<25}")
    print("-" * 40)
    for alumno in alumnos:
        if materia in alumnos[alumno]:
            notas_str = ', '.join(map(str, alumnos[alumno][materia][:-1]))  # Convertimos las notas en string, sacamos la condicion
            condicion = alumnos[alumno][materia][-1]  # La última posición es la condición
            print(f"{alumno:<10} {notas_str:<15} {condicion:<15}")
            print("-" * 40)

def matriz_promedios(alumnos):  # Genera matriz de promedios para dar resultados generales
    num_materias = len(materias)
    num_alumnos = len(alumnos)
    matriz = [[0] * num_materias for _ in range(num_alumnos)]
    i = 0
    for alumno in alumnos:
        j = 0
        for materia in materias:
            promedio = 0
            if materia in alumnos[alumno]:
                notas = alumnos[alumno][materia][:-1]  # saco el último índice
                if len(notas) > 0 and sum(notas) != 0:
                    promedio = (sum(notas) / len(notas))
                else:
                    promedio = 0
            matriz[i][j] = promedio  # Si el alumno no tiene esa materia o está en curso, el promedio es 0
            j += 1
        i += 1
    return matriz
def printmaterias(mats):
    
    print(" ")
    for mat in mats:
        print( mat )
        

    print(" ")

def cuadro_de_honor(alumnos):
    honor = []
    for alumno in alumnos: 
        materias = alumnos[alumno]
        todas_aprobadas = True  # Supongo que todas están aprobadas
        for mat in materias:  
            notas = materias[mat]  
            condicion = notas[-1]  
            if condicion not in ["Promociona", "Aprobada"] and todas_aprobadas:
                todas_aprobadas = False  
        if todas_aprobadas:
            honor.append(alumno)

    if honor:
        print("Cuadro de Honor:")
        print("Las Margaritas felicita a...")
        for alumno in honor:  
            print(alumno)
    else:
        print("No hay alumnos en el cuadro de honor.")

def mostrar_menu_con_anuncio():  # Imprimir menú
    print("MENÚ PRINCIPAL")
    menu = [
        "a) Profesor",
        "b) Alumno",
        "c) Admin",
        "s) Salir",
    ]

    for item in menu:
        print(item)


def operacion_a():
    print("HOLA PROFE")
    print("a) Ver materias")
    print("b) Ver promedios generales")
    print("c) Ver cuadro de honor")
    op = input("Ingrese la operación que desea realizar: ").lower()
    print(" ")
    if op == 'a':
        printmaterias(materias)
        materia = input("Ingrese la materia que desea ver: ").capitalize()
        print(" ")
        if materia in materias:
            imprimir_materia(materia, alumnos)
        else:
            print("No se encuentra la materia")
    elif op == 'b':
        matrizprom = matriz_promedios(alumnos)
        i = 0
        for alumno in alumnos:
            print("Alumno:", alumno)
            for j in range(len(matrizprom[i])):
                if matrizprom[i][j] != 0:  # Si el promedio es 0, no imprimo
                    print("Materia:", materias[j], end=" ")
                    print("Promedio: %.2f" % matrizprom[i][j])
                else:
                    print("Promedio no disponible para la materia:", materias[j])
            print("")
            i += 1

    elif op == 'c':
        print("Al cuadro de honor se llega habiendo promocionado o aprobado todas las materias.")
        cuadro_de_honor(alumnos)
    else:
        print("Opción no válida. Intente de nuevo.")


def operacion_c():
    menu = [
        "a) Eliminar alumnos",
        "b) Agregar alumnos",
    ]

    for item in menu:
        print(item)
    op = input("Ingrese la operación que desea realizar: ").lower()
    if op == "a":
        for año in años: 
            print(año, " ingrese el numero ", años.index(año))
        año = input()
        alumnos_curso = cursos[años[int(año)]]
        alumno = input("Ingrese el nombre del alumno que desea eliminar de la materia: ").capitalize()
        if alumno in alumnos_curso:   # materias del alumno
            cursos[años[int(año)]].pop(alumno)
            
        else:
            print("No se encuentra el alumno. ")
            desea = input("Desea intentar de nuevo? si/no: ").lower()
            while desea not in ["si", "no"]: # esto esta horrible hacerlo mejor!!
                print("Opción no válida. Intente de nuevo.")
                desea = input("Desea intentar de nuevo? si/no: ").lower()
                while desea == "si":
                    alumno = input("Ingrese el nombre del alumno que desea eliminar de la materia: ").capitalize()

    elif op == "b":
        alumno = input("Ingrese el nombre del alumno que desea agregar: ").capitalize()
        while alumno.isnumeric() or not alumno.isalpha():
            print("El nombre debe contener solo letras.")
            alumno = input("Ingrese el nombre del alumno que desea agregar: ").capitalize()
            
        if alumno in alumnos:
            print("El alumno ya se encuentra en la lista.")
        else:
            printmaterias(materias)
            materias_alumno = []
            for materia in materias:
                print(materia, end=" ")
                agregar = input("Desea agregar la materia? si/no: ").lower()
                opciones = ["si", "no"]
                while agregar not in opciones:
                    print("Opción no válida. Intente de nuevo.")
                    agregar = input("Desea agregar la materia? si/no: ").lower()
                if agregar == "si":
                    materias_alumno.append(materia)

            alumnos[alumno] = {mat: [0,0,0,"en curso"] for mat in materias_alumno}
            display_notas_alumnos(alumnos)

    else:
        print("Opción no válida. Intente de nuevo.")




# ALUMNOS Y SUS MATERIAS
años = ["1ro", "2do", "3ro", "4to", "5to"]
materias = ["Historia", "Matematicas", "Lengua"]
cursos = {
    "1ro": {
        "Bautista": {
            "Materias": {
                "Historia": [7, 8, 9],
                "Geografía": [7, 7, 8],
                "Lengua": [8, 9, 10]
            },
            "Faltas": 5,
            "Condicion": "OK",
        },
        "Mateo": {
            "Materias": {
                "Historia": [7, 8, 9],
                "Geografía": [7, 7, 8],
                "Lengua": [8, 9, 10]
            },
            "Faltas": 5,
            "Condicion": "OK",
        }
    }, 
    "2do": {
        "Bautista": {
            "Materias": {
                "Historia": [7, 8, 9],
                "Geografía": [7, 7, 8],
                "Lengua": [8, 9, 10]
            },
            "Faltas": 5,
            "Condicion": "OK",
        },
        "Mateo": {
            "Materias": {
                "Historia": [7, 8, 9],
                "Geografía": [7, 7, 8],
                "Lengua": [8, 9, 10]
            },
            "Faltas": 5,
            "Condicion": "OK",
        }
    },
    "3ro": {
        "Bautista": {
            "Materias": {
                "Historia": [7, 8, 9],
                "Geografía": [7, 7, 8],
                "Lengua": [8, 9, 10]
            },
            "Faltas": 5,
            "Condicion": "OK",
        },
        "Mateo": {
            "Materias": {
                "Historia": [7, 8, 9],
                "Geografía": [7, 7, 8],
                "Lengua": [8, 9, 10]
            },
            "Faltas": 5,
            "Condicion": "OK",
        }
    },
     "4to": {
         "Bautista": {
            "Materias": {
                "Historia": [7, 8, 9],
                "Geografía": [7, 7, 8],
                "Lengua": [8, 9, 10]
            },
            "Faltas": 5,
            "Condicion": "OK",}
        ,
        "Mateo": {
            "Materias": {
                "Historia": [7, 8, 9],
                "Geografía": [7, 7, 8],
                "Lengua": [8, 9, 10]
            },
            "Faltas": 5,
            "Condicion": "OK",
        }
     },
     "5to": {
         "Bautista": {
            "Materias": {
                "Historia": [7, 8, 9],
                "Geografía": [7, 7, 8],
                "Lengua": [8, 9, 10]
            },
            "Faltas": 5,
            "Condicion": "OK",}
        ,
        "Mateo": {
            "Materias": {
                "Historia": [7, 8, 9],
                "Geografía": [7, 7, 8],
                "Lengua": [8, 9, 10]
            },
            "Faltas": 5,
            "Condicion": "OK",
        }
     }

}
# Inicio del programa

usuario = input("ingrese su usuario: ")
arch = open("usuarios.json", "rt")
usuarios = json.load(arch)
nombres_usuarios = usuarios.keys()
if usuario in nombres_usuarios:
    print("Bienvenido")
    rol = usuarios[usuario]["rol"]
    if rol == "admin":
        operacion_c()
        decision = input("Desea realizar otra operación? si/no: ").lower()
        while decision == "si":
            operacion_a()
            decision = input("Desea realizar otra operación? si/no: ").lower()
    else:
        operacion_a()
        decision = input("Desea realizar otra operación? si/no: ").lower()
        while decision == "si":
            operacion_a()
            decision = input("Desea realizar otra operación? si/no: ").lower()
    
    print("Adios")
else:
    print("Usuario no encontrado")

