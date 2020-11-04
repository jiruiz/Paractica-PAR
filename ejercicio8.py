import csv


def cargar(alumnos, materias):
    materias_a = open(materias)
    alumnos_a = open(alumnos)

    materia_csv = csv.reader(materias_a)
    alumnos_csv = csv.reader(alumnos_a)

    next(materia_csv)
    next(alumnos_csv)

    alumnos = next(alumnos_csv, None)
    materias = next(materia_csv, None)


    while (alumnos):
        print(f"{alumnos[0]} ,{alumnos[1]}, {alumnos[2]},{alumnos[3]}")
        if (not materias or materias[0] != alumnos[0]):
            print("\tNo se registran materias Adeudadas")
        while (materias and materias[0] == alumnos[0]):
            print(f"\t {alumnos[1]},{alumnos[2]} debe la materia {materias[1]} del año {materias[2]}")
            materias = next(materia_csv, None)
        alumnos = next(alumnos_csv, None)

    materias_a.close()
    alumnos_a.close()
#if (not nota or nota[0] != alumno[0]):
#             print("\tNo se registran notas")
#         while (nota and nota[0] == alumno[0]):
#             print("\t{}: {}".format(nota[1], nota[2]))
#             nota = next(notas_csv, None)
#         alumno = next(alumnos_csv, None)

# import csv
#
# def imprimir_notas_alumnos(alumnos, notas):
#     """ Abre los archivos de alumnos y notas, y por cada alumno imprime
#         todas las notas que le corresponden. """
#     notas_a = open(notas)#se abre el archivo notas
#     alumnos_a = open(alumnos)#se abre el achivo alumnos
#     notas_csv = csv.reader(notas_a)#se lee el archivo notas
#     alumnos_csv = csv.reader(alumnos_a)#se lee el archivo alumnos
#
#     # Saltea los encabezados
#     next(notas_csv)
#     next(alumnos_csv)
#
#     # Empieza a leer
#     alumno = next(alumnos_csv, None)
#     nota = next(notas_csv, None)
#     while (alumno):
#         print(f"{alumno[0]},{alumno[1]} {alumno[2]} {alumno[3]}")
#
#         # print("{}, {} ({})".format(alumno[1], alumno[2], alumno[0]))
#         if (not nota or nota[0] != alumno[0]):
#             print("\tNo se registran notas")
#         while (nota and nota[0] == alumno[0]):
#             print("\t{}: {}".format(nota[1], nota[2]))
#             nota = next(notas_csv, None)
#         alumno = next(alumnos_csv, None)
#
#     # Cierro los archivos
#     notas_a.close()
#     alumnos_a.close()
#
# imprimir_notas_alumnos("alumnos80.csv", "deudaMaterias.csv")


cargar("alumnos800.csv", "deudaMaterias.csv")



# def carga(primerArchivo,segundoArchivo):
#     abrirPrimerArchivo = open(primerArchivo)
#     abrirSegundoArchivo = open(segundoArchivo)
#
#     leerPrimerArchivo = csv.reader(primerArchivo)
#     leerSegundoArchivo = csv.reader(segundoArchivo)
#
#
#     next(leerPrimerArchivo)
#     next(leerSegundoArchivo)
#
#     primerArchivo = next(leerPrimerArchivo, None)
#     segundoArchivo = next(leerSegundoArchivo, None)
#
#     while(primerArchivo):
#         print(f"{primerArchivo[0]},{primerArchivo[1]} {primerArchivo[2]} {primerArchivo[3]}")
#         if (not segundoArchivo or segundoArchivo[0] != primerArchivo[0]):
#             print("\t No hay registros")
#         while (segundoArchivo and segundoArchivo[0] == primerArchivo[0]):
#             print(f"\t {primerArchivo[2]},{primerArchivo[1]} debe la materia {segundoArchivo[1]} del año {segundoArchivo[2]}")
#             segundoArchivo = next(leerSegundoArchivo, None)
#         primerArchivo = next(leerPrimerArchivo, None)
#
#     abrirPrimerArchivo.close()
#     abrirSegundoArchivo.close()
