"""
matrizmaterias = crear_matriz(materias, alumnos)
imprimirmatriz(matrizmaterias, alumnos, materias)"""

"""for i in range(len(materias)):
    print("Materia: ", materias[i])
    print("Promocionaron: ",(cant_promocionados(matrizmaterias))[i], end=" ")
    print("Recursaron:", (cant_recursados(matrizmaterias))[i], end=" ")
    print("Aprobaron:",(cant_aprobados(matrizmaterias))[i], end=" ")
    print("Previos: ",(cant_previos(matrizmaterias))[i])

"""
"""
def cant_promocionados(matriz):
    matriz = []
    for i in range(len(matrizmaterias)):
        sum = 0
        for j in range(len(matrizmaterias[i])):
            if matrizmaterias[i][j][3] == "promociona":
                sum = sum + 1
        matriz.append(sum)
    return matriz

def cant_recursados(matriz):
    matriz = []
    for i in range(len(matrizmaterias)):
        sum = 0
        for j in range(len(matrizmaterias[i])):
            if matrizmaterias[i][j][3] == "recursa":
                sum = sum + 1
        matriz.append(sum)
    return matriz

def cant_aprobados(matriz):
    matriz = []
    for i in range(len(matrizmaterias)):
        sum = 0
        for j in range(len(matrizmaterias[i])):
            if matrizmaterias[i][j][3] == "aprobada":
                sum = sum + 1
        matriz.append(sum)
    return matriz

def cant_previos(matriz):
    matriz = []
    for i in range(len(matrizmaterias)):
        sum = 0
        for j in range(len(matrizmaterias[i])):
            if matrizmaterias[i][j][3] == "previo":
                sum = sum + 1
        matriz.append(sum)
    return matriz
"""
"""
def crear_matriz(materias, alumnos):
     matriz = []
     for materia in materias:
        fila = []
        for alumno in alumnos:
            notas = []
            condicion = ""
            for i in range(3):
                if i == 0:
                        print("ingrese la nota de " + materia + " de " + str(alumno) + "en el primer parcial")
                        nota = int(input())
                        nota = notavalida(nota)
                        notas.append(nota)
                elif i == 1:
                        print("ingrese la nota de " + materia + " de " + str(alumno) + "en el segundo parcial")
                        nota = int(input())
                        nota = notavalida(nota)
                        notas.append(nota)
                elif i == 2 and not promocione(notas):
                        if recurse(notas):
                            print("el alumno " + str(alumno) + " recursa la materia")
                            notas.append(0)
                            condicion = "recursa"
                            notas.append(condicion)
                        else:
                            if notas[0] < 4 or notas[1] < 4:
                                print("el alumno " + str(alumno) + " tiene que recuperar un parcial de la materia")
                                print("ingrese la nota de " + materia + " de " + str(alumno) + "en el recuperatorio")
                                nota = int(input())
                                nota = notavalida(nota)
                                notas.append(nota)
                                if nota > 4:
                                     condicion = "previo"
                                else:
                                     condicion = "recursa"
                            else:
                                print("el alumno " + str(alumno) + " tiene que rendir el final de la materia")
                                print("ingrese la nota de " + materia + " de " + str(alumno) + "en el final")
                                nota = int(input())
                                nota = notavalida(nota)
                                notas.append(nota)
                                if nota > 4:
                                    condicion = "aprobada"
                                else:
                                    condicion = "previo"
                            notas.append(condicion)
                else:
                        print("el alumno " + str(alumno) + " promociona la materia")
                        notas.append(promedio(notas))
                        condicion = "promociona"
                        notas.append(condicion)
            fila.append(notas)
        matriz.append(fila)                      
     return matriz"""
"""
def imprimirmatriz(matriz, alumnos, materias):
    for i in range(len(matriz)):
        print("Alumno legajo: ", alumnos[i])
        for j in range(len(matriz)):
            print("Notas de la materia:", materias[j])
            for k in range(len(matriz[i][j])):
                if k == 0:
                    print("Primer parcial:", matriz[i][j][k], end=" ")
                elif k == 1:
                    print("Segundo parcial:", matriz[i][j][k], end=" ")
                elif k == 2:
                    print("Final/promedio:", matriz[i][j][k], end=" ")
                elif k == 3:
                    print("Condicion:", matriz[i][j][k])
        print("")
"""