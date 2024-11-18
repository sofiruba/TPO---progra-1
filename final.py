import json
# FUNCIONES
#
def display_notas_alumnos(cursos):  # Imprime listado de alumnos con sus notas
    print("Listado de alumnos de Las Margaritas")
    print(f"{'Curso':<10}{'Alumno':<10} {'Materia':<15} {'Notas':<25}")
    print("-" * 60)
    for curso, alumnos in cursos.items():
        for alumno, it in alumnos.items():
            materias = it["Materias"]
            cont = 0
            for mat, notas in materias.items():
                notas_str = ', '.join(map(str, notas[:-1]))
                if cont > 0:
                    print(f"{'': <10}{'':<10} {mat:<15} {notas_str:<25}")
                else:
                    print(f"{curso: <10}{alumno:<10} {mat:<15} {notas_str:<25}")
                cont += 1
            print("-" * 60)
            

def imprimir_datos_alumno(cursos, curso, alumno):
    datos_alumno = cursos[curso][alumno]

    print(f"Datos del alumno '{alumno}' en el curso '{curso}':")
    print(f"  Materias:")
    for materia, notas in datos_alumno["Materias"].items():
        print(f"    - {materia}: Notas: {notas}, Promedio: {sum(notas) / len(notas):.2f}")
    print(f"  Faltas: {datos_alumno['Faltas']}")
    print(f"  Condición: {datos_alumno['Condicion']}")
    print(f"  Mora: {datos_alumno['Mora']}")
    print(f"  Previas: {', '.join(datos_alumno['Previas']) if datos_alumno['Previas'] else 'Ninguna'}")
    print(f"  Sanciones: {datos_alumno['Sanciones']}")


"""def matriz_promedios(alumnos):  # Genera matriz de promedios para dar resultados generales
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
    return matriz"""


"""def cuadro_de_honor(alumnos):
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
        print("No hay alumnos en el cuadro de honor.")"""


def matriznotasxcurso(cursos_profe, materia):
    matriz = []
    for curso in cursos_profe:
        fila = []    
        for alumno in cursos[curso]:
            notas = cursos[curso][alumno]['Materias'][materia]
            fila.append(notas[2])
        matriz.append(fila)
    
    return matriz


def funciones_profesor(nombre):
    menu =[
        "a) Ver notas",
        "b) Ver alumnos",
        
    ]
    for item in menu:
        print(item)
    op = input("Ingrese la operación que desea realizar: ").lower()
    print(" ")
    cursos_profe = profesores[nombre]["cursos"]
    materias_profe = profesores[nombre]["materias"]
    if op == "a":
        for materia in materias_profe:
            notas = matriznotasxcurso(cursos_profe, materia)
            print(notas)
    elif op=="b":
        for curso in cursos_profe:
            print("Alumnos de ", curso)
            alumnos_curso = cursos[curso].keys()
            for alumno in alumnos_curso:
                print(alumno, end=" ")
            print("")
    else:
        print("Opción no válida. Intente de nuevo.")
    """elif op == 'c':
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

    elif op == 'd':
        print("Al cuadro de honor se llega habiendo promocionado o aprobado todas las materias.")
        cuadro_de_honor(alumnos)"""
    
    


def funciones_admin():
    menu = [
        "a) Eliminar alumnos",
        "b) Agregar alumnos",
        "c) Ver datos de alumno"
    ]

    for item in menu:
        print(item)
    op = input("Ingrese la operación que desea realizar: ").lower()
    if op == "a":

        año = int(input("Ingrese el año del curso: "))
        año -=1
        alumnos_curso = cursos[años[int(año)]]
        for alumno in alumnos_curso:
            print(alumno)
        alumno = input("Ingrese el nombre del alumno que desea eliminar: ").capitalize()
        if alumno in alumnos_curso.keys():   # materias del alumno
            cursos[años[int(año)]].pop(alumno)
            display_notas_alumnos(cursos)
            
        else:
            print("No se encuentra el alumno. ")
            desea = input("Desea intentar de nuevo? si/no: ").lower()
            while desea not in ["si", "no"]: # esto esta horrible hacerlo mejor!!
                print("Opción no válida. Intente de nuevo.")
                desea = input("Desea intentar de nuevo? si/no: ").lower()
                while desea == "si":
                    alumno = input("Ingrese el nombre del alumno que desea eliminar de la materia: ").capitalize()
            

    elif op == "b":
        for año in años: 
            print(año, " ingrese el numero ", (años.index(año) + 1))
        año = input()
        alumno = input("Ingrese el nombre del alumno que desea agregar: ").capitalize()
        while alumno.isnumeric() or not alumno.isalpha():
            print("El nombre debe contener solo letras.")
            alumno = input("Ingrese el nombre del alumno que desea agregar: ").capitalize()
        materias_alumno = {materia: [] for materia in materias}
        cursos[años[int(año)]][alumno] = { "Materias": materias_alumno, "Faltas": 0, "Condicion": "OK" }
        display_notas_alumnos(cursos)

    elif op == "c":
        for año in años: 
            print(año, " ingrese el numero ", (años.index(año) + 1))
        año = input()
        alumnos_curso = cursos[años[int(año)]].keys()
        alumno = input("Ingrese el nombre del alumno: ").capitalize()
        if alumno not in alumnos_curso:
            print(f"El alumno '{alumno}' no está en el curso '{año}'.")
        else:
            imprimir_datos_alumno(cursos, años[int(año)], alumno)

    else:
        print("Opción no válida. Intente de nuevo.")




# VARIABLES y diccionarios
años = ["1ro", "2do", "3ro", "4to", "5to"]
materias = ["Historia", "Matematicas", "Lengua"]
cursos = {
    "1ro": {
        "Lucas": {
            "Materias": {
                "Lengua": [7, 8, 6],
                "Matemática": [5, 6, 7],
                "Historia": [6, 5, 7]
            },
            "Faltas": 12,
            "Condicion": "OK",
            "Mora": "No",
            "Previas": ["Historia"],
            "Sanciones": 1
        },
        "Camila": {
            "Materias": {
                "Lengua": [8, 9, 10],
                "Matemática": [4, 5, 6],
                "Historia": [6, 7, 5]
            },
            "Faltas": 28,
            "Condicion": "Libre",
            "Mora": "No",
            "Previas": ["Lengua", "Historia", "Matemática"],
            "Sanciones": 2
        }
    },
    "2do": {
        "Martina": {
            "Materias": {
                "Lengua": [7, 7, 8],
                "Matemática": [8, 9, 7],
                "Historia": [5, 6, 5]
            },
            "Faltas": 18,
            "Condicion": "OK",
            "Mora": "No",
            "Previas": ["Historia"],
            "Sanciones": 0
        },
        "Mateo": {
            "Materias": {
                "Lengua": [4, 5, 6],
                "Matemática": [7, 8, 6],
                "Historia": [6, 7, 5]
            },
            "Faltas": 14,
            "Condicion": "Mora",
            "Mora": "Sí",
            "Previas": ["Lengua", "Historia", "Matemática", "Lengua"],
            "Sanciones": 3
        }
    },
    "3ro": {
        "Sofía": {
            "Materias": {
                "Lengua": [9, 8, 7],
                "Matemática": [6, 7, 6],
                "Historia": [7, 8, 8]
            },
            "Faltas": 10,
            "Condicion": "OK",
            "Mora": "No",
            "Previas": [],
            "Sanciones": 0
        },
        "Tomás": {
            "Materias": {
                "Lengua": [4, 5, 5],
                "Matemática": [7, 6, 8],
                "Historia": [5, 5, 5]
            },
            "Faltas": 27,
            "Condicion": "Libre",
            "Mora": "Sí",
            "Previas": ["Historia", "Matemática"],
            "Sanciones": 4
        }
    },
    "4to": {
        "Lola": {
            "Materias": {
                "Lengua": [7, 9, 8],
                "Matemática": [6, 6, 7],
                "Historia": [7, 8, 6]
            },
            "Faltas": 5,
            "Condicion": "OK",
            "Mora": "No",
            "Previas": ["Matemática"],
            "Sanciones": 0
        },
        "Camila": {
            "Materias": {
                "Lengua": [5, 6, 7],
                "Matemática": [8, 9, 6],
                "Historia": [5, 6, 5]
            },
            "Faltas": 8,
            "Condicion": "OK",
            "Mora": "No",
            "Previas": ["Lengua", "Historia"],
            "Sanciones": 1
        }
    },
    "5to": {
        "Juan": {
            "Materias": {
                "Lengua": [8, 9, 9],
                "Matemática": [6, 7, 6],
                "Historia": [9, 8, 7]
            },
            "Faltas": 23,
            "Condicion": "OK",
            "Mora": "No",
            "Previas": [],
            "Sanciones": 0
        },
        "Lucas": {
            "Materias": {
                "Lengua": [5, 6, 7],
                "Matemática": [4, 5, 6],
                "Historia": [6, 6, 5]
            },
            "Faltas": 29,
            "Condicion": "Libre",
            "Mora": "Sí",
            "Previas": ["Lengua", "Historia", "Matemática", "Matemática"],
            "Sanciones": 3
        }
    }
}

profesores = {
    "Julian": {
        "materias": ["Historia"],
        "cursos": ["1ro", "2do", "3ro"],
        "nombre_usuario": "jperez"
    },
    "Magdalena": {
        "materias": ["Matemáticas"],
        "cursos": ["2do", "4to"],
        "nombre_usuario": "agomez"
    },
    "Carlos": {
        "materias": ["Lengua"],
        "cursos": ["1ro", "5to"],
        "nombre_usuario": "crodriguez"
    },
    "Laura": {
        "materias": ["Historia"],
        "cursos": ["4to", "5to"],
        "nombre_usuario": "lfernandez"
    },
    "Maria": {
        "materias": ["Matemáticas"],
        "cursos": ["1ro", "3ro", "5to"],
        "nombre_usuario": "mlopez"
    }, 
    "Roberto":{
        "materias": ["Lengua"],
        "cursos": ["2do", "3ro", "4to"],
        "nombre_usuario": "rcarlos"
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
    display_notas_alumnos(cursos)
    if rol == "admin":
        funciones_admin()
        decision = input("Desea realizar otra operación? si/no: ").lower()
        while decision == "si":
            funciones_admin()
            decision = input("Desea realizar otra operación? si/no: ").lower()
    else:
        nombres_profesores = profesores.keys()
        nombre = input("Ingrese su nombre").capitalize()
        while nombre not in nombres_profesores:
            for profe in nombres_profesores:
                print(profe)
            nombre = input("Ingrese correctamente su nombre como en la lista").capitalize()
        funciones_profesor(nombre)
        decision = input("Desea realizar otra operación? si/no: ").lower()
        while decision == "si":
            funciones_profesor()
            decision = input("Desea realizar otra operación? si/no: ").lower()
    
    print("Adios")
else:
    print("Usuario no encontrado")

