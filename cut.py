"""
1 - Escribir un programa, llamado cut.py, que dado un archivo de texto, un deli-
mitador, y una lista de campos, imprima solamente esos campos, separados por ese delimitador.
"""
import csv

def leerArchivo(archivo):
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        line = next(csv_reader, None)
        print(f'los nombres de las columas son {", ".join(line)}')
        for row in csv_reader:

            print(f'\t {row[0]}; {row[1]}; {row[2]}; {row[3]}')

def guardarArchivo(columna):
    with open("nuevafamilia.csv", mode="w", newline="") as archivo:
        columnaAEscribir = csv.writer(archivo, delimiter=";")

        for nombre in columna:
            columnaAEscribir.writerow(nombre)




leerArchivo("familia.txt")
guardarArchivo([['nombre', 'parentezco'],['Juan Ignacio Ruiz', 'Hijo'], ['Claudio Ruiz', 'Padre'], ['Karina Amaral', ' Madre'],['Gonzalo Ruiz', ' Hijo'],['Nicolas Ruiz', ' Hijo']])
