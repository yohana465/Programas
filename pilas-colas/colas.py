# ===============================================================================
# Programa de Impresion/Utilizando Colas
# Erick Estuardo Sicajau Turuy _________1990-10-18113
# Alba Gabriela Yool Alvarado _________1990-19-15166
# Paula Yohana Hernandez Morales ______1990-19-17246
# ===============================================================================

import random
from random import choice
import os
from collections import deque

cola2 = deque()
numero = []

while True:
    numero = 0
    print("\n*****************************************************")
    print("Desea?")     #Las opciones que el usuario puede disponer
    elegir = input("1) Agregar un elemento a la cola de impresion \n2) Imprimir \n3) Salir \n>>")
    if elegir == "1":
        print("Ingrese la Ruta")
        ruta_carpeta = input(">>")            # se tien quen Ingresar la ruta en donde estan los archivos que se desean imprimir
        archivos = os.listdir(ruta_carpeta)   # Ejemplo de ingreso de ruta
        cola = deque([archivos])              #C:\Users\Desktop\PrograPython\Proyecto2

        print("\nMostrando Vista previa de los Archivos de la Carpeta ")
        print("Ingrese el numero de archivo que desea agregar a la cola:")

        # Se programa el siguiente ciclo para que la impresion de los documentos sea de uno en uno
        while len(cola) > 0:
            siguiente_elemento = cola.popleft()
            for a in siguiente_elemento:
                numero = numero + 1
                num = [numero]
                print(f'{num} {a}')

            opcion = int(input(">>"))
            opcion_numero = opcion - 1
            impresion = siguiente_elemento[opcion_numero]
            cola2.append(impresion) #se agrega a la impresion
            numero = 0
            print("\nLa cola de impresion es:")
            #En esta funcion muestra los elementos que estan en cola
            for e in cola2:
                numero = numero + 1
                num = [numero] #asigna un correlativo a los archivo encerrado en llaves
                print(f'{num} {e}')

    #En esta Funcion permite elegir que documento se desea imprimir
    elif elegir == "2":
        if len(cola2) > 0:
            cola_impresion = cola2.popleft()
            print(f'\nSe imprimio: {cola_impresion}')
            if len(cola2) > 0:
                print("\nLa cola de impresion es:")
                numero = 0
                for y in cola2:
                    numero = numero + 1
                    num = [numero]  #asigna un correlativo a los archivo encerrado en llaves
                    print(f'{num} {y}')
            else:
                while len(cola2) == 0:
                    print("\nLa cola de impresion esta Vacia")
                    break
        else:
            while len(cola2) == 0:
                print("\nLa cola de impresion esta Vacia")
                break

    elif elegir == "3":
        print("\nFue un gusto realizar su cola de impresion!!!")
        break
    else:
        print("\nNo existe la opcion")


