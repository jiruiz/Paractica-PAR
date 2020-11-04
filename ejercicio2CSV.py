import csv

def cut(archivo, campos, delimitador):
    try:
        with open(archivo, 'r', newline='') as file:
            lectura = csv.reader(file, delimiter=delimitador)

            linea = next(lectura, None)

            campos_seleccionados = []

            while linea:

                for campo in campos:
                        if campo < len(linea):
                            campos_seleccionados.append(linea[campo])
                        else:
                            print(f"el campo {campo} no existe")
                linea = next(lectura, None)
            #impresion final
            for item in campos_seleccionados:
                print(item)
    except IOError:
        print("problemas de I/O")


cut("familia.txt", [0,1,2], ';')
