import csv
import os

def cargarDeudas(archivo, campos):
    guardar = "si"
    filasDeudas = []
    while guardar == "si":
        deuda = {}

        for campo in campos:
            deuda[campo] = input(f"Ingrese {campo} del Alumno: ")
        filasDeudas.append(deuda)
        guardar = input("Desea seguir agregando alumnos? Si/No")

    try:
        archivo_existe = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)

            if not archivo_existe:
                file_guarda.writeheader()

            file_guarda.writerows(filasDeudas)
            print("se guardo correctamente")
            return
    except IOError:
        print("Ocurrio un error con el archivo")


def cargarAlumnos(archivo, campos):
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

def recuperar(archivo,archivo2):
    archivo2 = "deudaMaterias.csv"

    archivo2 = open(archivo2)#se abre el archivo notas
    archivo = open(archivo)#se abre el achivo alumnos
    archivo2CSV = csv.reader(archivo2)#se lee el archivo notas
    archivo1CSV = csv.reader(archivo)#se lee el archivo

    # Saltea los encabezados
    next(archivo2CSV)
    next(archivo1CSV)

    # Empieza a leer
    alumno = next(archivo1CSV, None)
    deuda = next(archivo2CSV, None)
    while (alumno):
        print(f"{alumno[0]} ,{alumno[1]}, {alumno[2]}")
        if (not deuda or deuda[0] != alumno[0]):
            print("\tNo se registran materias Adeudadas")
        while (deuda and deuda[0] == alumno[0]):
            print(f"\tdebe la materia {deuda[1]} del año {deuda[2]}")
            deuda = next(archivo2CSV, None)
        alumno = next(archivo1CSV, None)

    archivo2.close()
    archivo.close()


    # while (alumno):
    #
    #     #print(f"{alumno[1]},{alumno[2]}")
    #     if (not deuda or deuda[0] != alumno[0]):
    #         print("\tNo se registran notas")
    #     while (deuda and deuda[0] == alumno[0]):
    #         #print(f"\t {alumno[1]},{alumno[2]} debe la materia {deuda[1]} del año {deuda[2]}")
    #
    #
    #
    #         #print(f"\t debe la materia {deuda[1]} del año {deuda[2]}")
    #
    #         #print(f"\tdebe {deuda[1]},{deuda[2]}")
    #         # print(f"\t{deuda[1]} del año {deuda[2]}")
    #         deuda = next(archivo2CSV, None)
    #     alumno = next(archivo2CSV, None)
    #
    # # Cierro los archivos
    # archivo2.close()
    # archivo.close()



def ejercicio8():
    ARCHIVO = "alumnos800.csv"
    MATERIAS= "deudaMaterias.csv"
    CAMPOS = ['DNI', 'Apellido', 'Nombre', 'Año', 'Comisión']
    CAMPOSMATERIAS = ['DNI', 'Materia', 'Año']
    while  True:
        print("Elija una opcion:\n 1.Cargar datos \n 2.Agregar Deuda Materias \n 3.Consulta deuda de Materias\n 4.Salir")
        opcion = input("")


        if opcion == "1":
            cargarAlumnos(ARCHIVO,CAMPOS)
        if opcion == "2":
            cargarDeudas(MATERIAS,CAMPOSMATERIAS)
        if opcion == "3":
            recuperar(ARCHIVO,MATERIAS)
        if opcion == "4":
            exit()
        else:
            print("Por favor elija una opcion valida")
ejercicio8()
