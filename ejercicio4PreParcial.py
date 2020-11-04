# def guardarDatos(diccionario, archivo):
#     try:
#         with open(archivo, 'r') as file:
#             lectura = file.readline()
#             for linea in lectura:
#                 if clave, valor in diccionario:
#                     print(linea)
#
#
#
#     except IOError:
#         print("error al recibir el archivo")




def guardarDatos(datos, archivo):
    try:
        with open(archivo, 'w', newline="") as file:
            for dato in datos:
                file.write(f'{dato}: {datos[dato]}\n')
            print("se guardo correctamente")

    except IOError:
        print("error al abrir archivo")

def cargaDatos(archivo):
    try:
        with open(archivo, 'r', newline='') as file:
            linea = file.readline()
            diccionario = {}

            while linea:
                linea = linea.rstrip('\n')
                campos = linea.split(',')
                diccionario[campos[0]] = campos[1]
                lines = file.readline()

            return diccionario

    except IOError:
        print("error al abrir archivo")


datoss = {"nombre": "juani", "apellido": "ruiz"}




guardarDatos(datoss, "ejercicio4.txt")
# print(cargaDatos("ejercicio4.txt"))
