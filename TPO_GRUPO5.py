
import random
def archivo_notas_alumnos(cursos):
    try:
        arch = open("archivos_cursos.txt", "w")
        for curso, alumnos in cursos.items():
            arch.write(f"{curso}\n")
            for alumno, datos in alumnos.items():
                arch.write(f"{alumno}\n")
                for materia, notas in datos["Materias"].items():
                    notas_str = ', '.join(map(str, notas))
                    arch.write(f"{materia}: {notas_str}\n")
                arch.write("\n")
    finally:
        try:
            arch.close()
        except NameError:
            pass


def mostrar_notas(cursos_profe, materias_profe):
    for materia in materias_profe:
        print(f"\nNotas de {materia} por curso:")
        for curso in cursos_profe:
            if curso not in cursos:
                print(f"No hay datos para el curso {curso}.")
                continue
            print(f"\nCurso: {curso}")
            print(f"{'Alumno':<15}{'Nota 1':<10}{'Nota 2':<10}{'Promedio':<10}")
            print("-" * 45)
            for alumno, datos in cursos[curso].items():
                notas_alumno = datos["Materias"].get(materia, [0, 0, 0])
                print(f"{alumno:<15}{notas_alumno[0]:<10}{notas_alumno[1]:<10}{notas_alumno[2]:<10}")
            print("-" * 45)



def gestionar_asistencia(cursos_profe):
    if cursos:
        tomarasistencia(cursos_profe, cursos)
    else:
        print("No hay cursos registrados para tomar asistencia.")


def gestionar_estadisticas(cursos_profe, materia_profe):
    if not materia_profe or len(materia_profe) == 0:
        print("No hay materias asignadas para generar estadísticas.")
        return

    menu = [
        "1. Ver mejores alumnos por curso",
        "2. Ver alumnos que van a diciembre por promedio menor a 7",
        "3. Ver promedio global de la materia"
    ]
    op = elegir_opcion(menu)
    match op:
        case 1:
            mostrar_mejores_alumnos(cursos_profe, materia_profe)
        case 2:
            mostrar_alumnos_diciembre(cursos_profe, materia_profe)
        case 3:
            calcular_promedio_global(cursos_profe, materia_profe)
        case _:
            print("Opción no válida.")


def mostrar_mejores_alumnos(cursos_profe, materia_profe):
    
    for curso in cursos_profe:
        if curso in cursos and cursos[curso]:
            mejores_alumnos = sorted(
                (alumno for alumno in cursos[curso].items()
                 if alumno[1]["Materias"].get(materia_profe, [0, 0, 0])[2] > 6),
                key=lambda x: x[1]["Materias"][materia_profe][2], reverse=True
            )[:3]
            if mejores_alumnos:
                print(f"Mejores alumnos en {curso} para {materia_profe}:")
                for alumno, datos in mejores_alumnos:
                    promedio = datos["Materias"][materia_profe][2]
                    print(f"{alumno}: {promedio:.2f}")
                print("")
            else:
                print(f"No hay alumnos con promedio mayor a 6 en {curso}.")
        else:
            print(f"No hay alumnos para {curso}")

def mostrar_alumnos_diciembre(cursos_profe, materia_profe):
    for curso in cursos_profe:
        if curso in cursos and cursos[curso]:
            alumnos_diciembre = [
                (alumno, datos["Materias"][materia_profe][2])
                for alumno, datos in cursos[curso].items()
                if datos["Materias"][materia_profe][2] < 7
            ]
            if alumnos_diciembre:
                print(f"Alumnos que van a diciembre en {curso} para {materia_profe}:")
                for alumno, promedio in alumnos_diciembre:
                    print(f"{alumno}: {promedio:.2f}")
                print("")
            else:
                print(f"No hay alumnos con promedio menor a 7 en {curso}.")
        else:
            print(f"No hay alumnos para {curso}")


def calcular_promedio_global(cursos_profe, materia_profe):
    total_promedios = 0
    total_alumnos = 0
    for curso in cursos_profe:
        if curso in cursos and cursos[curso]:
            for alumno, datos in cursos[curso].items():
                total_promedios += datos["Materias"][materia_profe][2]
                total_alumnos += 1
        else:
            print(f"No hay alumnos para {curso}")
    if total_alumnos > 0:
        promedio_global = total_promedios / total_alumnos
        print(f"El promedio global de {materia_profe} entre todos los cursos es: {promedio_global:.2f}")
    else:
        print("No hay promedios registrados para calcular el promedio global.")


def gestionar_subida_notas(cursos_profe, materias_profe):
    if not cursos:
        print("No hay cursos registrados para subir notas.")
        return
    año_elegido = mostrar_años(cursos_profe)
    curso = cursos.get(año_elegido, {})
    if not curso:
        print(f"No hay alumnos registrados en el curso {año_elegido}.")
        return
    subir_notas(cursos_profe, curso, materias_profe)


def funciones_profesor(usuario):
    if not profesores or usuario not in profesores:
        print("No hay datos de profesores disponibles.")
        return

    menu = [
        "1) Ver notas",
        "2) Ver alumnos",
        "3) Tomar asistencia",
        "4) Estadísticas",
        "5) Subir notas"
    ]
    op = elegir_opcion(menu)
    cursos_profe = profesores[usuario].get("cursos", [])
    materias_profe = profesores[usuario].get("materias", [])

    if not cursos_profe or not materias_profe:
        print("No hay cursos o materias asignados a este profesor.")
        return

    match op:
        case 1:
            mostrar_notas(cursos_profe, materias_profe)
        case 2:
            for curso in cursos_profe:
                if curso in cursos and cursos[curso]:
                    print(f"Alumnos de {curso}:")
                    for alumno in cursos[curso].keys():
                        print(alumno)
                    print("")
                else:
                    print(f"No hay alumnos registrados en el curso {curso}.")
        case 3:
            gestionar_asistencia(cursos_profe)
        case 4:
            gestionar_estadisticas(cursos_profe, materias_profe[0])
        case 5:
            gestionar_subida_notas(cursos_profe, materias_profe)
        case _:
            print("Opción no válida.")

# FUNCIONES GENERALES
def elegir_opcion(menu):
    for item in menu:
        print(item)
    while True:  # Asegura que el usuario ingrese una opción válida
        try:
            op = int(input("Ingrese el número de la opción: "))
            return op
        except ValueError:
            print("Por favor, ingrese un número válido.")


def opcion_valida(op, opciones):
    while op not in opciones:
        print("Opción no válida. Intente de nuevo. ")
        op = input("¿Desea realizar otra operación? (si/no): ").lower()
    return op
               
def mostrar_años(años):
    print("Seleccione un curso:")
    for i, año in enumerate(años):
        print(f"{i + 1}. {año}")
    
    opcion = -1  # Inicializamos con un valor inválido
    while opcion < 0 or opcion >= len(años):
        entrada = input("Opción: ")
        if entrada.isdigit():
            opcion = int(entrada) - 1
            if opcion < 0 or opcion >= len(años):
                print("Número fuera de rango. Intente nuevamente.")
        else:
            print("Entrada inválida. Debe ingresar un número.")
    return años[opcion]

# Funciones de impresion
def mostrar_alumnos(alumnos):  # Imprime listado de alumnos
    for alumno in alumnos:
        print(f"- {alumno}")

def mostrar_todos_los_alumnos(cursos):
    print("Lista de todos los alumnos:")
    for curso, alumnos in cursos.items():
        print(f"Curso {curso}:")
        for alumno in alumnos.keys():  # Recorre los nombres de los alumnos
            print(f" - {alumno}")
        print("")

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
    if año_elegido in cursos:
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
    else:
        print(f"No hay alumnos registrados de {año_elegido}")
                   
def imprimir_datos_alumno(cursos, curso, alumno):
    datos_alumno = cursos[curso][alumno]

    print(f"Datos del alumno '{alumno}' en el curso '{curso}':")
    print(f"  Materias:")
    for materia, notas in datos_alumno["Materias"].items():
        notass = ', '.join(map(str, notas))
        print(f"    - {materia}: Notas: {notass}, Promedio: {sum(notas) / len(notas):.2f}")
    print(f"  Faltas: {datos_alumno['Faltas']}")
    print(f"  Condición: {datos_alumno['Condicion']}")
    print(f"  Mora: {datos_alumno['Mora']}")
    print(f"  Previas: {', '.join(datos_alumno['Previas']) if datos_alumno['Previas'] else 'Ninguna'}")
    print(f"  Sanciones: {datos_alumno['Sanciones']}")

# Notas
def subir_notas(cursos_profe, curso, materia_profe): 
    for alumno, datos in curso.items():
        print(f"El alumno seleccionado es {alumno}")
        for materia, notas in datos["Materias"].items():
            if materia in materia_profe:
                print(f"La materia seleccionada es {materia}")
                subir_notas = input("Desea subir notas? si/no: ").lower()
                subir_notas = opcion_valida(subir_notas, ["si", "no"])
                nota1 = modificar_nota(notas, subir_notas)
                subir_notas = input("Desea subir notas? si/no: ").lower()
                subir_notas = opcion_valida(subir_notas, ["si", "no"])
                nota2 = modificar_nota(notas, subir_notas)
                promedio = promedio_pormateria([nota1, nota2])
                datos["Materias"][materia] = [nota1, nota2, promedio]
                print("Notas actualizadas correctamente.")

def modificar_nota(nota, nota_elegida):
    if nota_elegida.lower() == "si":
        while True:
            try:
                nota1 = int(input("Ingrese la nota modificada de la evaluación: "))
                if 1 <= nota1 <= 10:
                    break  # Salir del bucle si la nota es válida
                else:
                    print("La nota debe ser un número entre 1 y 10.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
    else:
        nota1 = nota[0] # Si no se modifica, se mantiene la nota original 
    return nota1
            
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
    nota_elegida1= input("Desea modificar la nota de la primera evalucacion? si/no: ").lower()
    nota_elegida1 = opcion_valida(nota_elegida1, ["si", "no"])
    nota_modificada = modificar_nota(nota, nota_elegida1)
    if nota_elegida1 == "si":
        nota.pop(0)
        nota[0:0] = [nota_modificada]
    nota_elegida2= input("Desea modificar la nota de la segunda evalucacion? si/no: ").lower()
    nota_elegida2 = opcion_valida(nota_elegida2, ["si", "no"])
    notas_modificada = modificar_nota(nota, nota_elegida2)
    if nota_elegida2 == "si":
        nota.pop(1)
        nota[1:1] = [notas_modificada]
    print("La nota ha sido actualizada correctamente.")

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
        "1) Modificar las notas de los alumnos",
        "2) Ver notas del curso",
        "3) Ver datos de alumno",
        "4) Crear un archivo con las notas de los alumnos"
    ]
    op = elegir_opcion(menu)
    match op:
        case 1:
            año_elegido = mostrar_años(años)
            if año_elegido in cursos:
                alumnos_año = cursos[año_elegido]
                mostrar_alumnos(cursos[año_elegido])
                alumno = input("Ingrese el nombre del alumno: ").capitalize()
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
                        display_notas_alumnos(cursos)
                        #display_alumnos(cursos)
                    else:
                        print ("No se encuentra la materia ")      
                else:
                    print ("El alunmo no se encuentra resgristrado. ")
            else: 
                print("No hay alumnos en ese curso")
        
        case 2:
            if cursos:
                display_alumnos(cursos)
                archivo = input("Desea guardar los datos en un archivo? si/no: ").lower()
                archivo = opcion_valida(archivo, ["si", "no"])
            else:
                print("No hay alumnos en el sistema")
        case 3:
            año_elegido = mostrar_años(años)
            if año_elegido in cursos:
                mostrar_alumnos(cursos[año_elegido])
                alumnos_curso = cursos[año_elegido].keys()
                alumno = input("Ingrese el nombre del alumno: ").capitalize()
                if alumno not in alumnos_curso:
                    print(f"El alumno '{alumno}' no está en el curso '{año_elegido}'.")
                else:
                    imprimir_datos_alumno(cursos, año_elegido, alumno)
            else:
                print("No hay alumnos en ese curso")
        case 4:
            print("Creando archivo con las notas de los alumnos...")
            archivo_notas_alumnos(cursos)
        case _:
            print("Opcion invalida")

def operaciones_alumnos():
    menu = [
        "1) Eliminar alumnos",
        "2) Agregar alumnos"
    ]
    op = elegir_opcion(menu)
    match op:
        case 1:
            año_elegido = mostrar_años(años)
            if año_elegido in cursos:
                alumnos_curso = cursos[año_elegido]
                for alumno in alumnos_curso:
                    print(alumno)
                alumno = input("Ingrese el nombre del alumno que desea eliminar: ").capitalize()
                while alumno not in alumnos_curso.keys():
                    alumno = input("Ingrese un nombre valido: ").capitalize()
                # materias del alumno
                cursos[año_elegido].pop(alumno)
                display_notas_alumnos(cursos)
                
        case 2:
            año_elegido = mostrar_años(años)
            while True:
                alumno = input("Ingrese el nombre del alumno que desea agregar: ").capitalize()
                if not alumno.isalpha():
                    print("El nombre debe contener solo letras. Intente nuevamente.")
                elif alumno in cursos.get(año_elegido, {}):  # Verificar si el alumno ya existe en el año
                    print(f"El alumno '{alumno}' ya está registrado en {año_elegido}. Intente con otro nombre.")
                else:
                    break  # Nombre válido y único en el año
                
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
                cursos[año_elegido][alumno] = nuevo_alumno

            print("")
            print("Listado actualizado")
            print(" ")
            display_notas_alumnos(cursos) 
        case _:
            print("Operacion no valida")

# Sanciones
def visualizar_sanciones():
    menu = [
        "1. Ver todas las sanciones",
        "2. Ver sanciones por curso o de alumno especifico.",
        "3. Ver curso con mayor cantidad de sanciones."
    ]
    op = elegir_opcion(menu)
    match op:
        case 1:
            for alumnosdelcurso in cursos:
                print(f"-Sanciones de {alumnosdelcurso}: ")
                if alumnosdelcurso in cursos:
                
                    alumnos_curso = cursos[alumnosdelcurso]
                    for alumno in alumnos_curso:
                        if "Sanciones" in alumnos_curso[alumno]:
                            sanciones = alumnos_curso[alumno]["Sanciones"]
                            print(f"{alumno} tiene {sanciones} sancion/es. ")
                        else:
                            print(f"{alumno} no tiene sanciones registradas.")
                    print("")
                else:
                    print(f"No hay alumnos registrados en el sistema")
        case 2:
            año_elegido = mostrar_años(años)
            if año_elegido in cursos:
                alumnos_curso = cursos[año_elegido]
                menu = [
                    "1. Ver las sanciones de todos los alumnos del curso.",
                    "2. Ver las sanciones de uno de los alumnos del curso."
                ]
                eleccion = elegir_opcion(menu)
                match eleccion:
                    case 1:
                        for alumno in alumnos_curso:
                            if "Sanciones" in alumnos_curso[alumno]:
                                sanciones = alumnos_curso[alumno]["Sanciones"]
                                print(f"{alumno} tiene {sanciones} sancion/es. ")
                            else:
                                print(f"{alumno} no tiene sanciones registradas.")
                        print("")
                    case 2:
                        mostrar_alumnos(alumnos_curso)
                        alumno_elegido = (input("Ingresa el alumno del que se quiere ver las sanciones: ")).capitalize()
                        
                        while alumno_elegido not in alumnos_curso:
                            mostrar_alumnos(alumnos_curso)
                            alumno_elegido = (input("Alumno invalido, ingresar uno de la lista: ")).capitalize()
                        if "Sanciones" in alumnos_curso[alumno_elegido]:
                            sanciones = alumnos_curso[alumno_elegido]["Sanciones"]
                            print(f"{alumno_elegido} tiene {sanciones} sancion/es") 
                        else:
                            print(f"{alumno_elegido} no tiene sanciones registradas.")
                    case _:
                        print("Opcion no valida")
            else:
                print("No hay alumnos en el curso")
        case 3:
            max_sanciones = 0
            curso_max_sanciones = None
            for curso, alumnos in cursos.items():
                sanciones_curso = sum(alumno.get("Sanciones", 0) for alumno in alumnos.values())
                if sanciones_curso > max_sanciones:
                    max_sanciones = sanciones_curso
                    curso_max_sanciones = curso
            if curso_max_sanciones:
                print(f"El curso con mayor cantidad de sanciones es {curso_max_sanciones} con {max_sanciones} sanciones.")
            else:
                print("No hay sanciones registradas.")
        case _:
            print("Opcion no valida")
            visualizar_sanciones()
            
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
        "1) Visualizar las sanciones de los alumnos",
        "2) Agregar sanciones a los alumnos",
    ]
    op = elegir_opcion(menu)
    match op:
        case 1:
            visualizar_sanciones()
        case 2:
            agregar_sanciones()
        case _:
            print("Operacion no valida")
            print("")
            operaciones_sanciones() 

#Deudas
def operaciones_deudas():
    menu = [
        "1) Visualizar las deudas de los alumnos", 
        "2) Modificar las deudas de los alumnos"
    ]
    op = elegir_opcion(menu)
    match op:
        case 1:
            año_elegido = mostrar_años(años)
            if año_elegido in cursos:
                alumnos_curso = cursos[año_elegido]
                print(f"\nAlumnos con mora del curso {año_elegido}:")
                alumnos_con_mora = False
                for alumno, datos in alumnos_curso.items():
                    if datos["Mora"] == "Sí":
                        print(f"  - {alumno}")
                        alumnos_con_mora = True
                if not alumnos_con_mora:    
                    print("  No hay alumnos con mora en este curso.")
            else:
                print(f"No hay alumnos de {año_elegido}")
        case 2:
            año_elegido = mostrar_años(años)
            if año_elegido in cursos:
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
            else:
                print(f"No hay alumnos de {año_elegido}")
        
        case _:
            print("Operacion no valida")

# Estedisticas
def estadisticas(materias, cursos):
    menu = [
        "1) Ver alumnos libres por faltas",
        "2) Ver alumnos desaprobados"
    ]
    op = elegir_opcion(menu)
    match op:
        case 1:
            if cursos:
                print("Alumnos libres por faltas:")
                for curso, alumnos in cursos.items():
                    for alumno, datos in alumnos.items():
                        if datos["Condicion"] == "Libre":
                            print(f"{alumno} de {curso} con {datos['Faltas']} faltas")
            else:
                print("No hay alumnos en el sistema")
        case 2:
            menu = [
                "1) Ver alumnos desaprobados por curso",
                "2) Ver alumnos desaprobados por materia",
                "3) Ver alumnos desaprobados por alumno específico"
            ]
            op = elegir_opcion(menu)
            match op:
                case 1:
                    curso_elegido = mostrar_años(años)
                    if curso_elegido in cursos:
                        print(f"Alumnos desaprobados en el curso {curso_elegido}:")
                        for alumno, datos in cursos[curso_elegido].items():
                            for materia, notas in datos["Materias"].items():
                                if notas[2] < 6:
                                    print(f"{alumno} en {materia} con promedio {notas[2]:.2f}.")
                    else:
                        print("No hay alumnos en ese curso.")
                case 2:
                    print("Materias disponibles:")
                    for materia in materias:    
                        print(f"- {materia}")

                    materia_elegida = input("\nIngrese la materia: ").capitalize()
                    if cursos:
                        print(f"Alumnos desaprobados en {materia_elegida}:")
                        for curso, alumnos in cursos.items():
                            for alumno, datos in alumnos.items():
                                if materia_elegida in datos["Materias"]:
                                    notas = datos["Materias"][materia_elegida]
                                    if notas[2] < 6:
                                        print(f"{alumno} de {curso} en {materia_elegida} con promedio {notas[2]:.2f}.")
                    else:
                        print("No hay alumnos en el sistema")
                case 3:
                    if cursos:
                        mostrar_todos_los_alumnos(cursos)
                        alumno_elegido = input("Ingrese el nombre del alumno: ").capitalize()
                        for curso, alumnos in cursos.items():
                            if alumno_elegido in alumnos:
                                for materia, notas in alumnos[alumno_elegido]["Materias"].items():
                                    if notas[2] < 6:
                                        print(f"Desaprueba {materia} con promedio {notas[2]:.2f}.")
                    else:
                        print("No hay alumnos en el sistema")
                case _:
                    print("Opción no válida")

#Usuarios
def operaciones_usuarios():
    menu = [
        "1) Agregar usuarios",
        "2) Eliminar usuarios",
        "3) Cambiar contraseñas",
        "4) Crear un archivo con usuarios registrados"
    ]
    op = elegir_opcion(menu)
    match op:
        case 1:
            agregar_usuarios()
        case 2:
            eliminar_usuarios()
        case 3:
            cambiar_contraseñas()
        case 4:
            guardar_usuarios_en_archivo(usuarios)
            print("Archivo generado correctamente.")
        case _:
            print("Operacion no valida")

def cambiar_contraseñas():
    users= regis_users()
    user_change= input("A que usuario desea cambiarle la contraseña? ")
    while user_change not in users:
        user_change= input("Invalido, elegir un usuario de la lista por favor: ")
    
    newpass= generarcontraseña()
    usuarios[user_change]["contraseña"] = newpass

def regis_users():
    usersreg= list(usuarios.keys())
    print("")
    print("Se encuentran registrados los siguientes usuarios:")
    for usuario in usersreg:
        print (f"- {usuario}")
    return usersreg

def eliminar_usuarios():
    users= regis_users()
    user_elim= input("A que usuario desea eliminar? ")
    while user_elim not in users:
        user_elim= input("Invalido, elegir un usuario de la lista por favor: ")

    if usuarios[user_elim]["rol"]== "profesor":
        profesores.pop(user_elim)
        usuarios.pop(user_elim)
    elif usuarios[user_elim]["rol"]== "admin":
        administradores.pop(user_elim)
        usuarios.pop(user_elim)
    
def agregar_usuarios():
    print("")
    print("--- Ingreso de datos del nuevo usuario ---")
    #rol
    print("Elegir rol")
    menu = [
        "1) Administrador",
        "2) Profesor",
    ]

    rol = elegir_opcion(menu)
    match rol:
        case "1":
            rol= "admin"
        case "2":
            rol= "profesor"
    #usuario

    while True:
        nuevo_usuario = input("Ingrese un usuario (min 5 y max 15 caracteres, solo letras y números): ").lower()
        if not nuevo_usuario.isalnum():
            print("Usuario inválido. Solo se permiten letras y números. Intente nuevamente.")
        elif 5 <= len(nuevo_usuario) <= 15:
            if nuevo_usuario in usuarios:
                print("Error: El usuario ya existe. Intente con otro nombre.")
            else:
                break  # Usuario válido y único
        else:
            print("Usuario inválido. Debe tener entre 5 y 15 caracteres.")

    #nombre
    nuevo_nombre= generarnewalpha("nombre")
    nuevo_nombre= nuevo_nombre.capitalize()
    #contraseña
    nueva_contraseña= generarcontraseña()
    if rol==1: 
        rol= "admin"
    if rol==2:
        rol="profesor"
    usuarios[nuevo_usuario]= {"rol": rol,"contraseña": nueva_contraseña}
    match rol:
        case "admin":
            administradores[nuevo_usuario]= {"nombre": nuevo_nombre}
        case "profesor":
            #materia del nuevo profe
            print("Que materia dicta el nuevo profesor?")
            for mat in materias:
                print (f"- {mat}")
            materia=input("")
            materia= materia.capitalize()
            while materia not in materias:
                materia=input("Materia invalida, volver a ingresar:")
                materia= materia.capitalize()
            materia= [materia]

            #cursos del nuevo profe
            print("¿En qué años dicta clases el nuevo profesor?")
            for año in cursos:
                print(f"- {año}")
            cursos_profe = set()  # 
            while True:
                curso = input("Ingresar por lo menos un curso (-1 para terminar): ")
                if curso == "-1" and len(cursos_profe) > 0:  # Permitir salir si hay al menos un curso
                    break
                if curso in cursos:
                    cursos_profe.add(curso)
                else:
                    print("Curso inválido, ingrese un curso válido o '-1' para terminar.")
            
            cursos_profe = list(cursos_profe)

            profesores[nuevo_usuario]= {"nombre": nuevo_nombre, "materias": materia, "cursos": cursos_profe}
   
def generarnewalpha(param=" "):
    newalpha = input(f"Ingresar {param} (min 3 y max 15 caracteres, solo letras):")
    while not newalpha.isalpha() or len(newalpha) < 3 or len(newalpha) > 15:
        newalpha = input("Inválido, ingrese de nuevo:")
    return newalpha

def generarcontraseña():
    print("Desea:")
    menu = [
        "1) Ingresar manualmente una nueva contraseña",
        "2) Sugerir una contraseña",
    ]
    contra = elegir_opcion(menu)
    match contra:
        case 1:
            contra = input("Ingresar contraseña (min 5 y max 12 caracteres, solo números y letras):")
            while not (contra.isalnum() and 5 <= len(contra) <= 12):
                contra = input("Contraseña inválida, ingresar de nuevo:")
            return contra

        case 2:
            while True:  # Bucle para manejar sugerencias
                contra = generarcontraseña_ale()
                print(f"Contraseña sugerida: {contra}. ¿Desea guardarla?")
                menu = [
                    "1) Sí",
                    "2) No, crear otra",
                ]
                check = elegir_opcion(menu)
                if check == 1:
                    print(f"Contraseña guardada: {contra}")  # Mostrar la contraseña guardada
                    break  # Terminar el bucle si se elige guardar la contraseña
                else:
                    print("Se descartó la contraseña sugerida.")
            return contra

def generarcontraseña_ale(largo=12, contraseña=""):
    if len(contraseña) == largo:
        return contraseña
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    nuevo_caracter = random.choice(caracteres)
    return generarcontraseña_ale(largo, contraseña + nuevo_caracter)

def guardar_usuarios_en_archivo(userss):
    try:
        archivo_usuarios = open("usuarios.txt ", "w")
        for usuario, datos in userss.items():
            archivo_usuarios.write(f"Usuario: {usuario}\n")
            archivo_usuarios.write(f"  Rol: {datos['rol']}\n")
            archivo_usuarios.write(f"  Contraseña: {datos['contraseña']}\n")
            archivo_usuarios.write("\n")
    finally:
        try:
            archivo_usuarios.close()
        except NameError:
            pass


def funciones_admin():
    menu= [
        "1) Alumnos",
        "2) Deudas",
        "3) Sanciones",
        "4) Boletines",
        "5) Estadisticas",
        "6) Usuarios"
    ]
    op = elegir_opcion(menu)
    match op:
        case 1:
            print("")
            operaciones_alumnos()
        case 2:
            print("")
            operaciones_deudas()
        case 3:
            print("")
            operaciones_sanciones()
        case 4:
            print("")
            operaciones_notas()
        case 5:
            print("")
            estadisticas(materias, cursos)
        case 6:
            print("")
            operaciones_usuarios()
        case _:
            print("Operacion no valida")

#Operaciones profesor

def tomarasistencia(cursos_profe, cursos):
    año_elegido = mostrar_años(cursos_profe)
    curso = cursos[año_elegido]
    for alumno, datos in curso.items():
        print(alumno)
        op = elegir_opcion(["1. Presente", "2. Ausente"])
        if op == 2:
            datos["Faltas"] += 1
        else:
            print(f"{alumno} presente")

def iniciar_sesion(usuarios, profesores):
    while True:
        try:
            usuario = input("Ingrese su usuario: ").strip()
            usuario= usuario.lower()
            if usuario not in usuarios:
                raise KeyError("Usuario no encontrado. Intente nuevamente.")
 
            contraseña = input("Ingrese su contraseña: ").strip()
            if usuarios[usuario]["contraseña"] != contraseña:
                raise ValueError("Contraseña incorrecta. Intente nuevamente.")

            if usuarios[usuario]["rol"]== "admin":
                nombre_administrador = administradores[usuario]["nombre"]
                print("")
                print(f"Bienvenido, {nombre_administrador}.")
                return usuario, nombre_administrador, usuarios[usuario]["rol"]

            else:
                nombre_profesor = profesores[usuario]["nombre"]
                print("")
                print(f"Bienvenido, {nombre_profesor}.")
                return usuario, nombre_profesor, usuarios[usuario]["rol"]
        
        except (KeyError, ValueError) as e:
            print(e)

def realizar_operaciones(rol, nombre_profesor):
    if rol == "admin":
        print("Acceso como administrador.")
        while True:
            funciones_admin()  # Llama a tus funciones específicas para admin
            opccion = input("¿Desea realizar otra operación? (si/no): ").lower()
            otra_op = opcion_valida(opccion, ["si", "no"])
            if otra_op != "si":
                break
    elif rol == "profesor":
        print(f"Operaciones para el profesor {nombre_profesor}.")
        while True:
            funciones_profesor(nombre_profesor)  # Llama a tus funciones específicas para profesor
            opccion = input("¿Desea realizar otra operación? (si/no): ").lower()
            otra_op = opcion_valida(opccion, ["si", "no"])
            if otra_op != "si":
                break
    else:
        print("Rol desconocido.")

def main():
    try:
        print("---INICIO DE SESIÓN---")
        usuario, nombre_profesor, rol = iniciar_sesion(usuarios, profesores)
        realizar_operaciones(rol, usuario)
        print("¡Hasta luego!")
    except Exception as e:
        print(f"Error inesperado: {e}")

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
        }
    },
    "5to": {
        "Juan": {
            "Materias": {
                "Lengua": [0, 0, 0],
                "Matemática": [6, 7, 6],
                "Historia": [9, 8, 7]
            },
            "Faltas": 23,
            "Condicion": "OK",
            "Mora": "No",
            "Previas": [],
            "Sanciones": 0
        }
    }
}
usuarios = {
    "jperez": {
        "rol": "profesor",
        "contraseña": "password123" 
    },
    "agomez": {
        "rol": "profesor",
        "contraseña": "password456"  
    },
    "crodriguez": {
        "rol": "profesor",
        "contraseña": "password789"  
    },
    "lfernandez": {
        "rol": "profesor",
        "contraseña": "password101"  
    },
    "mlopez": {
        "rol": "profesor",
        "contraseña": "password202"  
    },
    "rcarlos": {
        "rol": "profesor",
        "contraseña": "password303"  
    },
    "admin1": {
        "rol": "admin",
        "contraseña": "adminpass1"
    },
    "admin2": {
        "rol": "admin",
        "contraseña": "adminpass2"
    }
}

profesores = {
    "jperez": {
        "nombre": "Julian",
        "materias": ["Historia"],
        "cursos": ["1ro", "2do", "3ro"]
    },
    "agomez": {
        "nombre": "Magdalena",
        "materias": ["Matemáticas"],
        "cursos": ["2do", "4to"]
    },
    "crodriguez": {
        "nombre": "Carlos",
        "materias": ["Lengua"],
        "cursos": ["1ro", "5to"]
    },
    "lfernandez": {
        "nombre": "Laura",
        "materias": ["Historia"],
        "cursos": ["4to", "5to"]
    },
    "mlopez": {
        "nombre": "Maria",
        "materias": ["Matemáticas"],
        "cursos": ["1ro", "3ro", "5to"]
    },
    "rcarlos": {
        "nombre": "Roberto",
        "materias": ["Lengua"],
        "cursos": ["2do", "3ro", "4to"]
    }
}

administradores = {
    "admin1": {
        "nombre": "Alejandra",
    },
    "admin2": {
        "nombre": "Mauricio",
    }
}

main()
