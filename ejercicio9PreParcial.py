"""
Usted está a cargo del desarrollo de un programa facturación para una obra social.
Se pide que:
El programa permita la búsqueda de un beneficiario, por DNI,
 a partir del archivo especificado que contiene los datos de las prestaciones.
 Deberá mostrar cuántas consultas ha hecho por prestación y el total en dinero consumido.
 Y el total de dinero consumido por todos los beneficiarios.



"""
import csv




def facturacion(archivoPrestaciones):
    presta = open(archivoPrestaciones)
    presta_csv = csv.reader(presta, delimiter=";")

    item = next(presta_csv, None)
    total = 0

    while item:
        dni = item[0]
        total_cliente = 0

        print(f"cliente: {dni}")

        while item and item[0] == dni:

            total_anyo = 0
            prestacionesAnueles = 0


            while item and item[0] == dni:
                prestacionesMes= item[1]
                monto = item[2]
                # montoConvertido = float(monto.replace(',','.'))
                print(f"\t\tAtenciones del mes {prestacionesMes}: debe ${monto}")
                print("")
                monto = float(monto.replace(',','.'))
                total_anyo += monto
                prestacionesAnueles += int(prestacionesMes)

                item = next(presta_csv, None)
            print(f"\t Total en pesos año ${total_anyo}")
            print(f"total de prestaciones en el año :{prestacionesAnueles}")
            print("")
            total_cliente += total_anyo

        print(f"Total para el cliente {dni}: ${total_cliente}")
        total += total_cliente
        print("***************************************************")
    print(f"total general de todos los beneficiarios: ${total}")

    presta.close()


facturacion("obraSocial.csv")
