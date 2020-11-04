def grep(archivo):#le pasamos el archivo como una variable y la expresion que buscamos en ese archivo
    try:#intentar
        with open(archivo, 'r', newline='') as file:
            totalGeneral = 0
            atencionesTotal = 0
            suSaldo = 0
            expresion = input("dni a buscar:  ")
            for linea in file:#por cada linea en el archivo
                casilleros = linea.split(";")
                cliente = casilleros[0]
                prestaciones = casilleros[1]
                consumo = casilleros[2]
                consumo = float(consumo.replace(",","."))
                totalGeneral += consumo
                consultas = 0
                if expresion in linea:#si la expresion esta en la linea
                    # print(linea)#inprimo la linea


                    dineroConsumido = 0

                    if expresion in cliente:

                        consultas += int(prestaciones)
                        suSaldo += float(consumo)


                    # print(casilleros)

                    atencionesTotal += int(prestaciones)

                linea = linea.rstrip('\n')#dentro del for le agrego al final el salto de linea, para ir a la siguiente linea

            print(f"cliente: {expresion}")
            print(f"\t\tAtenciones del mes {atencionesTotal}: debe ${suSaldo}")

        print(f"el consumo total general es de {totalGeneral}")
    except IOError:
        print("Hubo un error al abrir el archivo.")

grep('obraSocial.csv')
