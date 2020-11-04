def copiarTXTaCSV(archivoALeer, nuevoNombre):
    with open(archivoALeer, "r") as primerArchivo:
        with open(nuevoNombre, "w") as nuevoArchivo:
            linea = primerArchivo.readline()
            while linea != '':
                nuevoArchivo.write(linea)
                linea = primerArchivo.readline()


copiarTXTaCSV("familia.txt", "familiaCopiada.csv")
