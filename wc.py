"""
2- Escribir un programa, llamado wc.py que reciba un archivo,
lo procese e imprima por pantalla
cuántas líneas,
cuantas palabras y
cuántos caracteres contiene el archivo.
"""

import csv

def contador(archivo):
    contador_palabras = 0
    contador_caracteres = 0
    contador_linea = 0
    with open (archivo) as f:
        for row in f:
            contador_linea += 1
            cantidad_caracteres = len(row)
            contador_caracteres += cantidad_caracteres
            separador = row.split()
            for palabra in separador:
                contador_palabras += 1
    print(f"cantidad de lineas: {contador_linea}\ncantidad de palabras: {contador_palabras}\ncantidad de caracteres: {contador_caracteres}")


def wc(archivo):#le paso el archivo
    cantLineas = 0#contador de lineas
    cantPalabras = 0# contador de palabra
    cantCaracteres = 0#contador de caracteres
    try:#intentar
        with open(archivo, 'r', newline="") as file:
            for linea in file:#por cada linea en el archivo
                cantLineas += 1#dentro del for hacemos que la cantidad de lineas sea una mas
                linea = linea.rstrip('\n')#dentro del for  le agregamos a cada linea un salto de linea
                cantCaracteres += len(linea)#dentro del for la cantidad de caracteres se le suma la longitud de cada linea
                cantPalabras += len(linea.split())#dentro del for cantidad de palabras suma la linea separada por el espacio
    except IOError:
        print("error de nombre de archivo")

    print(f"lineas {cantLineas}, caracteres {cantCaracteres}, cantPalabras, {cantPalabras}")

wc("familia.txt")
