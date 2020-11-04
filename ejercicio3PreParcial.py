def grep(archivo, expresion):#le pasamos el archivo como una variable y la expresion que buscamos en ese archivo
    try:#intentar
        with open(archivo, 'r', newline='') as file:
            for linea in file:#por cada linea en el archivo
                if expresion in linea:#si la expresion esta en la linea
                    print(linea)#inprimo la linea
                linea = linea.rstrip('\n')#dentro del for le agrego al final el salto de linea, para ir a la siguiente linea
    except IOError:
        print("Hubo un error al abrir el archivo.")

# def buscador(archivo, expresion):
#     try:
#         with open (archivo) as f:
#             contador = 0
#             for row in f:
#                 if row.find(expresion) > -1:
#                     print(row)
#                     contador += 1
#             if contador == 0:
#                 print("No se encontraron resultados")
#
#     except IOError:
#         print("Error al intentar abrir el archivo")


# def grep(expresion, nombr_arc):
#     encontrada= False
#
#     with open ( nombr_arc, 'r') as file:
#         lineas = file.readline()
#         for linea in lineas:
#             if expresion.lower() in linea.lower():#lower lo pone todo en minuscula
#                 encontrada = True
#                 print (linea)
#
#     if encontrada == False:
#         print("no se encuentra estra expresión")
#
# expresion= input("Escriba una expresion ")


grep('familia.txt', 'Hijo')
