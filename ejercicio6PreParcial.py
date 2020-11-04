# def perdirNumero():
#
#     while True:
#         numero = input("ingrese numero del 1 al 10: ")
#         try:
#             numero = int(numero)
#             if 0 < numero <= 10:
#                 return numero
#             else:
#                 print("el nuero debe estar entre 1 y 10")
#         except ValueError:
#             print(f" {numero}debe ser un entero")
#
# def tablaN():
#     numero = perdirNumero()
#     try:
#         with open(f'tabla-{numero}.txt', 'w', newline="") as file:
#
#             for multiplicador in range(1,11):
#                 file.writer(f"{multiplicador} x {numero} = {numero * multiplicador}\n")
#     except IOError:
#             print("hubo un error")

    
