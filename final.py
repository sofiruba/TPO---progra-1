import json
# FUNCIONES GENERALES
def elegir_opcion(menu):
    for item in menu:
        print(item)
    op = input("Ingrese la operación que desea realizar: ").lower()
    return op
def opcion_valida(op, opciones):
    while op not in opciones:
        op = input("Opción no válida. Intente de nuevo.").lower()
    return op
               
def mostrar_años(años):
    for año in años:
        print(año)
    año_elegido = int(input("Ingrese el numero del año que desea elegir: "))
    while año_elegido not in range(1,len(años)+1):
        año_elegido = int(input("Numero invalido, vuelva a ingresar: "))
    return años[año_elegido-1]

# Funciones de impresion
def mostrar_alumnos(alumnos):
    print("Alumnos del curso: ", end="")   
    for alumno in alumnos:
        print(alumno)
    print(" ")

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

def display_alumnos(cursos):  # Imprime listado de alumnos
    año_elegido = mostrar_años(años)
    alumnos_año = cursos[año_elegido]

    print(f"\nListado de alumnos de {año_elegido}")
    print(f"{'Curso':<10}{'Alumno':<10} {'Materia':<15} {'Notas':<25}")
    print("-" * 60)
    
    for alumno, datos in alumnos_año.items():
        materias = datos["Materias"]
        cont = 0
        for mat, notas in materias.items():
            notas_str = ', '.join(map(str, notas))
            if cont > 0:
                print(f"{'':<10}{'':<10} {mat:<15} {notas_str:<25}")
            else:
                print(f"{año_elegido:<10}{alumno:<10} {mat:<15} {notas_str:<25}")
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

# Notas
def promedio_pormateria(notas_pormateria):
    nota = notas_pormateria[:-1]
    return sum(nota)/len(nota)
def previa_pormateria(nota, años, alumno_elegido, materia):
    previa = False
    if nota[2] < 6:
            previa = True      
    if previa == True:
            cursos[años][alumno_elegido]["Previas"].append(materia)
            print ("Se actualizo las previas")

def elegir_notas(nota):
    nota_elegida1= input("Desea modificar la nota de la primera evalucacion? si/no: ").capitalize()
    nota_elegida1 = opcion_valida(nota_elegida1, ["si", "no"])
    if nota_elegida1 == "si":
        nota1 = int(input("Ingrese la nota modificada de la  primera evalucacion: "))
        nota.pop(0)
        nota[0:0] = [nota1]
                
    nota_elegida2= input("Desea modificar la nota de la segunda evalucacion? si/no: ").capitalize()
    nota_elegida2 = opcion_valida(nota_elegida2, ["si", "no"])
    if nota_elegida2 == "si":
        nota1 = int(input("Ingrese la nota modificada de la segunda evaluacion: "))
        nota.pop(1)
        nota[1:1] = [nota1]

def matriznotasxcurso(cursos_profe, materia):
    matriz = []
    for curso in cursos_profe:
        fila = []    
        for alumno in cursos[curso]:
            notas = cursos[curso][alumno]['Materias'][materia]
            fila.append(notas[2])
        matriz.append(fila)
    
    return matriz

def operaciones_notas():
    menu = [
        "a) Modificar las notas de los alumnos",
        "b) Ver notas del curso",
        "c) Ver datos de alumno"
    ]
    op = elegir_opcion(menu)
    match op:
        case "a":
            año_elegido = mostrar_años(años)
            if año_elegido in cursos:
                alumno = input("Ingrese el nombre del alumno: ").capitalize()
                alumnos_año = cursos[año_elegido]
                if alumno in alumnos_año:   
                    materias = alumnos_año[alumno]["Materias"].keys()
                    print (*materias)
                    mate = input(("Ingrese la materia: ")).capitalize()
                    if mate in materias:
                        notas = alumnos_año[alumno]["Materias"][mate]
                        elegir_notas(notas)
                        promedio = promedio_pormateria(notas)
                        notas.pop(2)
                        notas[2:2] = [promedio]
                        previa_pormateria(notas, año_elegido, alumno, mate)
                        print("Las notas se han actualizado correctamente.")
                        #display_alumnos(cursos)
                    else:
                        print ("No se encuentra la materia ")      
                else:
                    print ("El alunmo no se encuentra resgristrado. ")
            else: 
                print("No hay alumnos en ese curso")
        
        case "b":
            display_alumnos(cursos)
        case "c":
            año_elegido = mostrar_años(años)
            if año_elegido in cursos:
                alumnos_curso = cursos[año_elegido].keys()
                alumno = input("Ingrese el nombre del alumno: ").capitalize()
                if alumno not in alumnos_curso:
                    print(f"El alumno '{alumno}' no está en el curso '{año_elegido}'.")
                else:
                    imprimir_datos_alumno(cursos, año_elegido, alumno)
            else:
                print("No hay alumnos en ese curso")
        case _:
            print("Opcion invalida")

def operaciones_alumnos():
    menu = [
        "a) Eliminar alumnos",
        "b) Agregar alumnos"
    ]
    op = elegir_opcion(menu)
    match op:
        case "a":
            año_elegido = mostrar_años(años)
            if año_elegido in cursos:
                alumnos_curso = cursos[año_elegido]
                for alumno in alumnos_curso:
                    print(alumno)
                alumno = input("Ingrese el nombre del alumno que desea eliminar: ").capitalize()
                if alumno in alumnos_curso.keys():   # materias del alumno
                    cursos[año_elegido].pop(alumno)
                    display_notas_alumnos(cursos)
                else:
                    print("No se encuentra el alumno. ")
        case "b":
            año_elegido = mostrar_años(años)
            alumno = input("Ingrese el nombre del alumno que desea agregar: ").capitalize()
            while alumno.isnumeric() or not alumno.isalpha():
                print("El nombre debe contener solo letras.")
                alumno = input("Ingrese el nombre del alumno que desea agregar: ").capitalize()
            
            materias_alumno = {materia: [0,0,0] for materia in materias}
            nuevo_alumno = {
                "Materias": materias_alumno,
                "Faltas": 0, 
                "Condicion": "OK",
                "Mora": "No",
                "Previas": [],
                "Sanciones": 0
            }
            if año_elegido not in cursos:
                cursos[año_elegido] = {alumno : nuevo_alumno }
            else: 
                cursos[año_elegido][alumno] = { nuevo_alumno }
            display_notas_alumnos(cursos) 
        case _:
            print("Operacion no valida")

# Sanciones
def visualizar_sanciones():
    menu = [
        "a. Ver todas las sanciones",
        "b. Ver sanciones por curso o de alumno especifico.",
        "c. Ver curso con mayor cantidad de sanciones."
    ]
    op = elegir_opcion(menu)
    match op:
        case "a":
            for alumnosdelcurso in cursos:
                print(f"-Sanciones de {alumnosdelcurso}: ")
                for alumno in alumnosdelcurso:
                    sanciones=cursos[alumnosdelcurso][alumno]["Sanciones"]
                    print(f"{alumno} tiene {sanciones} sancion/es. ")
                print("")
        case "b":
            año_elegido = mostrar_años(años)
            if año_elegido in cursos:
                alumnos_curso = cursos[año_elegido]
                menu = [
                    "a. Ver las sanciones de todos los alumnos del curso.",
                    "b. Ver las sanciones de uno de los alumnos del curso."
                ]
                eleccion = elegir_opcion(menu)
                eleccion = opcion_valida(eleccion, ["a", "b"])
                match eleccion:
                    case "a":
                        for alumno in alumnos_curso:
                            sanciones= alumnos_curso[alumno]["Sanciones"]
                            print(f"{alumno} tiene {sanciones} sancion/es. ")
                        print("")
                    case "b":
                        alumno_elegido = (input("Ingresa el alumno del que se quiere ver las sanciones: ")).capitalize()
                        
                        while alumno_elegido not in alumnos_curso:
                            mostrar_alumnos(alumnos_curso)
                            alumno_elegido = (input("Alumno invalido, ingresar uno de la lista: ")).capitalize()
                        sanciones= alumnos_curso[alumno_elegido]["Sanciones"]
                        print(f"{alumno_elegido} tiene {sanciones} sancion/es") 
                    case _:
                        print("Opcion no valida")
            else:
                print("No hay alumnos en el curso")
        case "c":
            pass
        case _:
            print("Opcion no valida")

def agregar_sanciones():
        ptosmaximos= 50
        año_elegido = mostrar_años(años)
        if año_elegido in cursos:
            alumnos_curso = cursos[año_elegido]
            mostrar_alumnos(alumnos_curso)
            san_alumn = (input("Ingresa el alumno del que se quiere ver las sanciones: ")).capitalize()
            while san_alumn not in alumnos_curso:
                san_alumn = (input("Alumno invalido, ingresar uno de la lista: ")).capitalize()
            ptos= int(input("Ingresar cantidad de puntos de sancion a agregar: "))
            
            newsanciones= alumnos_curso[san_alumn]["Sanciones"] + ptos
            alumnos_curso[san_alumn]["Sanciones"]= newsanciones
            
            if alumnos_curso[san_alumn]["Sanciones"]>ptosmaximos:
                print("El alumno ha sobrepasado la mayor cantidad de sanciones permitidas. Por lo tanto queda libre")
                alumnos_curso[san_alumn]["Condicion"]= "Libre"
                print("Condición actualizada")
            else:
                print(f"Puntos de sanciones actualizados. A {san_alumn} le quedan {ptosmaximos-newsanciones} puntos de sanciones disponibles para quedar libre.")
        else: 
            print("No hay alumnos en ese curso")
def operaciones_sanciones():
    menu = [
        "a) Visualizar las sanciones de los alumnos",
        "b) Agregar sanciones a los alumnos",
    ]
    op = elegir_opcion(menu)
    match op:
        case "a":
            visualizar_sanciones()
        case "b":
            agregar_sanciones()
        case _:
            print("Operacion no valida")

#Deudas
def operaciones_deudas():
    menu = [
        "a) Visualizar las deudas de los alumnos", 
        "b) Modificar las deudas de los alumnos"
    ]
    op = elegir_opcion(menu)
    match op:
        case "a":
            año_elegido = mostrar_años(años)
            alumnos_curso = cursos[año_elegido]
            print(f"\nAlumnos con mora del curso {año_elegido}:")
            alumnos_con_mora = False
            for alumno, datos in alumnos_curso.items():
                if datos["Mora"] == "Sí":
                    print(f"  - {alumno}")
                    alumnos_con_mora = True
            if not alumnos_con_mora:    
                print("  No hay alumnos con mora en este curso.")
        case "b":
            año_elegido = mostrar_años(años)
            alumno = input("Ingrese el nombre del alumno: ").capitalize()
            alumnos_curso = cursos[año_elegido]
            if alumno in alumnos_curso:
                if alumnos_curso[alumno]["Mora"] == "Sí":
                    alumnos_curso[alumno]["Mora"] = "No"
                else:
                    alumnos_curso[alumno]["Mora"] = "Sí"
                print(f"Estado de mora actualizado para {alumno}.")
            else:
                print("El alumno no se encuentra.")
        
        case _:
            print("Operacion no valida")


def funciones_admin():
    menu= [
        "a) Alumnos",
        "b) Deudas",
        "c) Sanciones",
        "d) Boletines"
    ]
    op = elegir_opcion(menu)
    match op:
        case "a":
            operaciones_alumnos()
        case "b":
            operaciones_deudas()
        case "c":
            operaciones_sanciones()
        case "d": 
            operaciones_notas()
        case _:
            print("Operacion no valida")

#Operaciones profesor
def funciones_profesor(nombre):
    menu =[
        "a) Ver notas",
        "b) Ver alumnos",  
    ]
    op = elegir_opcion(menu)
    cursos_profe = profesores[nombre]["cursos"]
    materias_profe = profesores[nombre]["materias"]
    match op:
        case "a":
            # Falta excp
            for materia in materias_profe:
                notas = matriznotasxcurso(cursos_profe, materia)
                print(notas)
        case "b":
            for curso in cursos_profe:
                if curso in cursos:
                    print("Alumnos de ", curso)
                    alumnos_curso = cursos[curso].keys()
                    for alumno in alumnos_curso:
                        print(alumno, end=" ")
                    print("")



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
usuarios = {
      "profesor1":{
        "rol": "profesor"
      },
      "admin1":{
        "rol": "admin"
      },
      "profesor2":{ 
        "rol": "profesor"
      },
      "admin2":{
        "rol": "admin"
      }
    
  }
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
            funciones_profesor(nombre)
            decision = input("Desea realizar otra operación? si/no: ").lower()
    
    print("Adios")
else:
    print("Usuario no encontrado")

