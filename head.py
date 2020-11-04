import csv
"""Escribir un programa, llamado head que reciba un archivo y un número N e
imprima las primeras N líneas del archivo."""
def ejercicio1(archivo, numero):
    with open(archivo, 'r') as file:
        lectura = file.readlines()
        for linea in range(len(lectura)):
            if linea <= numero:
                print(lectura[linea])
ejercicio1("README.md", 5)
#-------------------------------------------------------------------------------
"""Escribir un programa, llamado cp.py, que copie todo el contenido de un ar-
chivo (sea de texto o binario) a otro, de modo que quede exactamente igual.

Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes. """

def cp(archivo):
    with open(archivo, 'r') as file:
        lectura = file.readlines()

    with open('copiaReadme.md', 'w') as file2:
        file2.writelines(lectura)

cp("README.md")
#------------------------------------------------------------------------------

"""
Escribir un programa, llamado cut.py, que dado un archivo de texto, un deli-
mitador, y una lista de campos, imprima solamente esos campos, separados por ese delimitador.
"""
