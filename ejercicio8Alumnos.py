"""8A- La capacidad de cargar los datos de la nómina de alumnos,
 pidiendo el ingreso de los mismos
  teniendo en cuenta el formato
  DNI, Apellido, Nombre, Año, Comisión
   a la hora de generar el archivo csv."""

import csv
import os.path

# def copiarTXTaCSV(archivoALeer, nuevoNombre):
#     try:
#         with open(archivoALeer, "r") as primerArchivo:
#             with open(nuevoNombre, "w") as nuevoArchivo:
#                 linea = primerArchivo.readline()
#                 while linea != '':
#                     nuevoArchivo.write(linea)
#                     linea = primerArchivo.readline()
#     except IOError:
#         print("¡Probrema en la lectura del archivo!")
#copiarTXTaCSV("alumnos8.txt", "alumnosCopiados.csv")

#
# def guardar(archivo, campos):
#     guardar = "si"
#     filas = []
#     while guardar == "si":
#         alumno = {}
#
#         for campo in campos:
#             alumno[campo] = input(f"Ingrese {campo} del Alumno: ")
#         filas.append(alumno)
#         guardar = input("Desea seguir agregando renglones? Si/No")
#
#     try:
#         archivo_existe = os.path.isfile(archivo)
#         with open(archivo, 'a', newline='') as file:
#             file_guarda = csv.DictWriter(file, fieldnames=campos)
#
#             if not archivo_existe:
#                 file_guarda.writeheader()
#
#             file_guarda.writerows(filas)
#             print("se guardo correctamente")
#             return
#     except IOError:
#         print("Ocurrio un error con el archivo")
#
#
#
# def cargar(archivo):
#     try:
#         with open(archivo,'r', newline='') as file:
#             lectura_csv = csv.DictReader(file)
#             campos = lectura_csv.fieldnames
#
#             for linea in lectura_csv:
#                 print(f"{linea[campos[0]]}, {linea[campos[1]]},  {linea[campos[2]]},  {linea[campos[3]]}")
#             return
#     except IOError:
#         print("Ocurrio un error con el archivo")

# def cargar(archivo, campos):
#     guardar = "si"
#     listaAlumnos = []
#     while guardar == "si":
#         alumno = {}
#
#         for campo in campos:
#
#             alumno[campo] = input(f"Ingrese {campo} del Alumno: ")
#         listaAlumnos.append(alumno)
#         guardar = input("Desea seguir agregando alumnos? Si/No")
#
#     try:
#         with open(archivo,'a', newline="") as archivoAEscribir:
#             archivoGuarda = csv.DictWriter(archivoAEscribir, fieldnames=campos)
#             archivoGuarda.writeheader()
#             archivoGuarda.writerow(listaAlumnos)
#             print("se guardaron los datos")
#             print(alumno)
#             return
#     except IOError:
#         print("error")

def cargar(archivo, campos):
    guardar = "si"
    filas = []
    while guardar == "si":
        alumno = {}

        for campo in campos:
            alumno[campo] = input(f"Ingrese {campo} del Alumno: ")
        filas.append(alumno)
        guardar = input("Desea seguir agregando alumnos? Si/No")

    try:
        archivo_existe = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)

            if not archivo_existe:
                file_guarda.writeheader()

            file_guarda.writerows(filas)
            print("se guardo correctamente")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

def cargaDatos(archivo,campos):
    try:
        with open(archivo, 'r', newline='') as file:
            lectura = csv.DictReader(file, fieldnames= campos)
            campos = lectura_cs

            for cadaLinea in lectura:
                if campo in campos:
                    print(f"{linea[campo[0]]}")


            return

    except IOError:
        print("error al abrir archivo")

def ejercicio8():
    ARCHIVO = "alumnos80.csv"
    archivoMaterias = "deudaMaterias.csv"
    CAMPOS = ['DNI', 'Apellido', 'Nombre', 'Año', 'Comisión']

    while  True:
        print("Elija una opcion:\n 1.Cargar datos \n 2.recuperar datos \n 3.Salir")
        opcion = input("")


        if opcion == "1":
            cargar(ARCHIVO,CAMPOS)
        if opcion == "2":
            cargaDatos(ARCHIVO,CAMPOS)
        if opcion == "3":
            exit()
        else:
            print("Por favor elija una opcion valida")
ejercicio8()
