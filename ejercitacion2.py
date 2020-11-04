def cut(archivo, campos, delimitador):# e pasamos el archivo, los campos y el delimitados como variables
    try:#intentar
        with open(archivo, 'r', newline='') as file:
            linea = file.readline()#leemos la primera linea
            campos_seleccionados = []#en esta lista guardamos los campos que vamos a seleccionar
            while linea:#mientras linea sea True
                listaTempotal = linea.split(delimitador)#hacemos una lista temporal, que en cada linea va a estar separadndo con
                #el delimitador que le pasemos

                for campo in campos:#para cada campo en los campos que le pasemos
                    # try:
                    #     campos_seleccionados.append(listaTempotal[campo])
                    # except IndexError:
                    #     print(f"el campo {campo} no existe")

                    if campo < len(listaTempotal):#si cada campo es menor a la longitud de la lista temporal
                        campos_seleccionados.append(listaTempotal[campo])#la lista de campos campos_seleccionados va a
                        #adicionar el campo cada campo de la lista temporal
                    else:
                        print(f"el campo {campo} no existe")
                linea = file.readline()#hacemos que se lea la linea que no fue procesada para que la lista temporal sea mayor y vuelva al for
        for item in campos_seleccionados:#por cada iten de los campos sleccionados
            print(item)
    except IOError:
        print("problemas de I/O")

cut('familia.txt', [0,2], ';')
