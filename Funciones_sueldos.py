import csv
import random

trabajadores=["Juan Pérez","María Garcia","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos={}

def menu(titulo,lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        print(i,'.- Salir del programa')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')

def valida_Asignar_sueldos(trabajadores):
    if sueldos >= 300000  <= 2500000:
        return True
    else:
        return False
def lee_Asignar_sueldos():
    while True:
        trabajadores=random('Sueldos aleotorios: ')
        if trabajadores.isdigit():
           trabajadores_int = int(sueldos)
           if valida_Asignar_sueldos(int(trabajadores_int)):
                return trabajadores
           else:
                print('Sueldos aleotorios entre $300.000 y $2.500.000')
        else:
            print('Debe Ingresar un numero')
def crea_txt(nombre,datos):
    with open(nombre+'.txt', 'w') as archivo:
	    archivo.write(datos)