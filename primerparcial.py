"""
Sistema de Evaluación Académica Crear un sistema de evaluación que utilice matrices para calificaciones, 
listas y diccionarios para gestionar estudiantes y materias,
"""
# VARIABLES GLOBALES PARA LA IMPRESIÓN
ancho = 50 
ancho_anuncio = 45
ramos = 0

# FUNCIONES

def printflores(n):
    for i in range(n):
        print("✿", end=" ")

def eliminar_alumno(alumno, alumnos):  #Eliminar alumno del diccionario
    if alumno in alumnos:
        alumnos.pop(alumno) 
    else:
        print("No se encuentra el alumno")

def display_notas_alumnos(alumnos): # Imprime listado de alumnos con sus notas
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

def mostrar_alumno(alumno, alumnos): # Imprimir boletin academico de alumno
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

def imprimir_materia(materia, alumnos): # Imprimir datos de una materia
    print(f"{'Alumno':<10} {'Notas':<15} {'Condición':<25}")
    print("-" * 40)
    for alumno in alumnos:
        if materia in alumnos[alumno]:
            notas_str = ', '.join(map(str, alumnos[alumno][materia][:-1]))  # Convertimos las notas en string, sacamos la condicion
            condicion = alumnos[alumno][materia][-1]  # La última posición es la condición
            print(f"{alumno:<10} {notas_str:<15} {condicion:<15}")
            print("-" * 40)           

def matriz_promedios(alumnos): #Genera matriz de promedios para dar resultados generales
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
                    promedio
                else:
                    promedio = 0
            matriz[i][j] = promedio  # Si el alumno no tiene esa materia o esta en curso, el promedio es 0
            j += 1
        i += 1
    return matriz
    
def printmaterias(mats):
    printflores(10)
    print(" ")
    for mat in mats:
        printflores(1)
        print( mat + " ".ljust(ancho - 14 - len(mat)) )
        
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
            if condicion not in ["Promociona", "Aprobada"] and todas_aprobadas: # cuando encuentra una desaprobada cambia la condicion
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

def mostrar_menu_con_anuncio(): # Imprimir menu
    print ( )
    menu = [
        "a) ✿ Profesor".ljust(ancho - 12) + "✿",
        "b) ❀ Alumno".ljust(ancho - 12) + "❀".ljust(10),
        "c) ✾ Admin".ljust(ancho - 12) + "✾".ljust(10),
        "d) ✿ Ver grilla alumnos".ljust(ancho - 12) + "✿".ljust(10),
        "e) ❀ Ver pedidos de flores".ljust(ancho - 12) + "❀".ljust(10),
        "s) ✿ Salir".ljust(ancho - 12) + "✿".ljust(10),
    ]

    anuncio = [
        "✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿".center(ancho_anuncio + 5),
        "✿".ljust(1) +  "FLORES AMARILLAS".center(ancho_anuncio - 16)+ "✿",
        "✿".ljust(1) +  "DE LA PROMO".center(ancho_anuncio - 16)+ "✿",
        "✿".ljust(ancho_anuncio - 15) + "✿",
        "✿ f) Hacer pedido de flores".ljust(ancho_anuncio - 15) + "✿",
        "",
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
    printflores(20)
    print(" ")
    op = input("Ingrese la operacion que desea realizar: ").lower()
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
            print(" ❀ Alumno: ", alumno)
            for j in range(len(matrizprom[i])):
                if matrizprom[i][j] != 0:  # Si el promedio es 0, no imprimo
                    print("Materia: ", materias[j], end=" ")
                    print("Promedio:%.2f " %matrizprom[i][j])
                else:
                    print("Promedio no disponible para la materia: ", materias[j])

            print("")
            i += 1

    elif op == 'c':
        print ("Al cuadro de honor se llega habiendo promocionado o aprobado todas las materias.")
        cuadro_de_honor(alumnos)
    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60))

def operacion_b():
    print("✾ Ingrese su nombre para ver sus notas ✾".center(30))
    nombre = input().capitalize()
    mostrar_alumno(nombre, alumnos)

def operacion_c():
    print (" ")
    printflores(6)
    print("❀  HOLA ADMIN ❀", end=" ")
    printflores(6)
    print(" ")
    print("a) ✿ Eliminar alumnos".ljust(ancho - 12) + "✿")
    print("b) ❀ Agregar alumnos".ljust(ancho - 12) + "❀")
    print("c) ❀ Eliminar alumno de materia".ljust(ancho - 12) + "❀")
    printflores(20)
    print(" ")
    op = input("Ingrese la operacion que desea realizar: ").lower()
    if op == "a":
        alumno = input("Ingrese el nombre del alumno que desea eliminar: ").capitalize()
        eliminar_alumno(alumno,alumnos)
        display_notas_alumnos(alumnos)

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
                alumnos[alumno].pop(materia)
            else:
                print("No se encuentra la materia")
            display_notas_alumnos(alumnos)
            print(" ")
        else:
            print("No se encuentra el alumno.")

    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60))     
    print(" ")

pedidos_flores = {}

def operacion_e(ramos):
    print("✾ Pedidos de flores de Las Margaritas ✾".center(30))
    print(" ")
    if pedidos_flores:
        for nombre, ramos in pedidos_flores.items():
            print(f"Nombre: {nombre}, Ramos: {ramos}")
    else:
        print("No hay pedidos de flores.")
    print(" ")

def operacion_f(ramos):
    max_ramos = 100
    disponibles = max_ramos - ramos
    
    if disponibles <= 0:
        print("Lo siento, no tenemos más ramos disponibles.")
    else:
        flores = int(input(f"Ingrese la cantidad de ramos que desea (Máx. {disponibles} ramos disponibles): "))
        
        while flores <= 0:
            print("La cantidad de ramos debe ser mayor que 0.")
            flores = int(input(f"Ingrese la cantidad de ramos que desea (Máx. {disponibles} ramos disponibles): "))

        if flores > disponibles:
            print(f"No tenemos suficientes ramos para cubrir {flores}. Podemos ofrecerle {disponibles} ramos.")
            respuesta = input(f"¿Desea pedir {disponibles} ramos en su lugar? (si/no): ").lower()
            if respuesta == "si":
                flores = disponibles
            else:
                print("No se ha realizado el pedido.")
                flores = 0
        if flores != 0:
            ramos += flores
            nombre = input("Ingrese su nombre: ").capitalize()
            if nombre in pedidos_flores:
                pedidos_flores[nombre] += flores
            else:
                pedidos_flores[nombre] = flores
            print(f"Gracias {nombre}, ha pedido {flores} ramos de flores.")
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


print("❀ ❀ ❀ ❀ ❀ ❀" +  " ✿  Las Margaritas ✿ ".center(57)+ "❀ ❀ ❀ ❀ ❀ ❀",)


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
        operacion_b()
    elif opcion == 'c':
        operacion_c()
    elif opcion == 'd':
        display_notas_alumnos(alumnos)
    elif opcion == 'f':
        ramos = operacion_f(ramos)
    elif opcion == 'e':
        operacion_e(ramos)
    elif opcion == 's':
        print ()
        if ramos==0:
            print("Recuerde colaborar con la promo encargando sus flores amarillas ❀❀❀".center(60))
        else: 
            print ("La promo ya ha vendido", ramos,"ramos de flores amarillas ❀ Agradecemos a la comunidad de Las Margaritas ")
        print("Saliendo del programa... ✿".center(60))
        continuar = False
    else:
        print("Opción no válida. Intente de nuevo. ❀".center(60)) 