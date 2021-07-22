#22-07-2021
#Rosa Vanessa Palacios Beltran
#n --> ar = long

from random import *

#Entradas
n = randint(1,11)
ar = []
long = n
#Procesos
valueN = int(input('Ingresa un número: '))
if valueN >= 11:
    print('Número no valido, solo se premiten números enteros del 1 al 10.')
    quit()
#Falta ciclo for 
if valueN <= 11: #cumple
    valueN = n
    ar = [valueN]

#Salidas
print(ar)