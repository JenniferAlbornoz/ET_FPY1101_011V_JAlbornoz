import os
import csv
import Funciones_sueldos as f
from random import random
import statistics
os.system('cls')

trabajadores = []   
while True:
    opc=f.menu('Menu principal',['Asignar sueldos','Clasificar sueldos','Ver estadisticas','Reporte de sueldos'])
    if opc==1:
        sueldos=f.lee_Asignar_sueldos()
    else:
        print('Finalizando programa')
        print('Desarrollado por Jennifer Albornoz')
        print('RUT 19.229.951-9')
    break