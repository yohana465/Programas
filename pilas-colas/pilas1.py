# ===============================================================================
# piedra,papel,tijera
# Erick Estuardo Sicajau Turuy _________1990-10-18113
# Alba Gabriela Yool Alvarado _________1990-19-15166
# Paula Yohana Hernandez Morales ______1990-19-17246
# ===============================================================================


import random
from random import choice
import os
# importar el tipo de dato para utilizar pilas
from collections import deque

# definir la pila
historial = deque()
historial2 = deque()
historial3 = deque()

#Se realiza una funcion para inicio de partidas
def mi_partida():
    Opciones = ['Piedra', 'Papel', 'Tijera']
    Maquina = (choice((Opciones)))
    print("\nElige tu respuesta:")
    # menu que se mostraran en pantalla
    print("1)Piedra \n2)Papel \n3)Tijera")
    #Eleccion de elemento que realizara el usuario
    Eleccion = input(">>")
    if Eleccion == "1":
        usuario = 'Piedra'
    elif Eleccion == "2":
        usuario = 'Papel'
    elif Eleccion == "3":
        usuario = 'Tijera'

    print("\nHumano: ", usuario)
    print("Computadora: ", Maquina)
    historial.append(usuario)  # usar append para agregar elementos al historial
    historial2.append(Maquina)
     #ejecucion del juego. quein gana humano, computadora.
    if usuario == Maquina:
        puntuaciones = 0
        print("Resultado: Empate!!")
        historial3.append("Empate!!")

    if (usuario == 'Piedra'):
        if (Maquina == 'Papel'):
            print("Resultado: Gana Computadora!")
            historial3.append("Gana Computadora!")
        elif (Maquina == 'Tijera'):
            print("Resultado: Gana Humano!")
            historial3.append("Gana Humano!")

    if (usuario == 'Papel'):
        if (Maquina == 'Tijera'):
            print("Resultado: Gana Computadora!")
            historial3.append("Gana Computadora!")
        elif (Maquina == 'Piedra'):
            print("Resultado: Gana Humano!")
            historial3.append("Gana Humano!")

    if (usuario == 'Tijera'):
        if (Maquina == 'Piedra'):
            print("Resultado: Gana Computadora!")
            historial3.append("Gana Computadora!")
        elif (Maquina == 'Papel'):
            print("Resultado: Gana Humano!")
            historial3.append("Gana Humano!")


def main():
    n = False
    while n == False:
        puntuaciones = mi_partida()
        while True:
            # cantidad de registros o veces que se desean ingresar
            respuesta = input("\nDeseas? \n1) Jugar otra vez \n2) Ver resultado anterior \n3) Salir \n>> ").lower()
            if (respuesta == "1"):
                puntuaciones = mi_partida()
            if (respuesta == "2"):
                if len(historial) > 0:
                    while len(historial) > 0:
                        # extraer el último elemento utilizando pop
                        ultima_acction = historial.pop()
                        print(f'\nHumano: {ultima_acction}')
                        break
                    while len(historial2) > 0:
                        # extraer el último elemento utilizando pop
                        ultima_acction2 = historial2.pop()
                        ultimo_resultado = historial3.pop()
                        print(f'Computadora: {ultima_acction2}')
                        print(f'Resultado: {ultimo_resultado}')
                        break
                else:
                    while len(historial) == 0:
                        print("\n¡El Historial esta Vacio!")
                        break
            if (respuesta == "3"):
                print("\nNada mejor que divertirse, vuelva pronto!!!")
                n = True
                break


main()