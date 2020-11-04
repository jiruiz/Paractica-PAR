import csv
import os.path


# def ejercicio7_guardar(archivo, campos):
#     guardar = "si"
#     listaVendedores = []
#     while guardar == "si":
#         vendedor = {}
#         for campo in campos:
#             vendedor[campo] = input(f"ingrese {campo} del vendedor: ")
#         listaVendedores.append(vendedor)
#         guardar = input("desea seguir agregando vendedores?: Si/No")
#
#     try:
#         archivo_existe = os.path.isfile(archivo)
#         with open(archivo, 'a', newline="") as file:
#             file_guarda = csv.DictWriter(file, fieldnames=campos)
#             if not archivo_existe:
#                 file_guarda.writeheader()
#             file_guarda.writeheader()
#             file_guarda.writerow(listaVendedores)
#             print("se guardo correctamente")
#             return
#     except IOError:
#             print("ocurrio un error con el archivo")
#
#
#
#
#
# def ejercicio7_cargar(archivo):
#     try:
#         with open(archivo, 'r', newline='') as file:
#             lecturaCSV = csv.DictWriter(file)
#             campos = lecturaCSV.fieldnames
#
#             for linea in lecturaCSV:
#                 print(f"{linea[1]} {linea[0]} trabaja en la empresa desde {linea[2]} y lleva comisionado {linea[4]}")
#             return
#     except IOError:
#         print("Ocurrio un error con el archivo")
#
#
# # 7 a
# def ejercicio7():
#     ARCHIVO = 'Vendedores.csv'
#     CAMPOS = ['Apellido', 'Nombre', 'Fecha de ingreso', 'Antigüedad', 'Comisiones']
#
#     while True:
#         print("Elija una opcion\n 1. Guardar Datos \n 2.Cargar Datos \n 3.Salir")
#         opcion = input("")
#         if opcion == "3":
#             exit()
#         if opcion == "1":
#             ejercicio7_guardar(ARCHIVO, CAMPOS)
#         if opcion == "2":
#             ejercicio7_cargar(ARCHIVO)
#         else:
#             print("por favor elija una opcion valida")
#
# ejercicio7()



import os.path

def eje7_guardar(archivo, campos):
    guardar = "si"
    lista_vendedores = []
    while guardar == "si":
        vendedor = {}

        for campo in campos:
            vendedor[campo] = input(f"Ingrese {campo} del vendedor: ")
        lista_vendedores.append(vendedor)
        guardar = input("Desea seguir agregando vendedores? Si/No")

    try:
        archivo_existe = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)

            if not archivo_existe:
                file_guarda.writeheader()

            file_guarda.writerows(lista_vendedores)
            print("se guardo correctamente")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

#7 c
def eje7_cargar(archivo):
    try:
        with open(archivo,'r', newline='') as file:
            lectura_csv = csv.DictReader(file)
            campos = lectura_csv.fieldnames

            for linea in lectura_csv:
                print(f"{linea[campos[1]]} {linea[campos[0]]} trabaja en la empresa desde {linea[campos[2]]} y lleva comisionado {linea[campos[4]]}")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

# 7 a
def ejercicio7():
    ARCHIVO = "vendedores.csv"
    CAMPOS = ['Apellido', 'Nombre', 'Fecha de ingreso', 'Antigüedad', 'Comisiones']

    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        opcion = input("")

        if opcion == "3":
            exit()
        if opcion == "1":
            eje7_guardar(ARCHIVO, CAMPOS)
        if opcion == "2":
            eje7_cargar(ARCHIVO)
        else:
            print("Por favor elija una opcion valida")

ejercicio7()
