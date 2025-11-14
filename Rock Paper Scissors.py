#HACER UN PIEDRA PAPEL TIJERA CON LA MACHINA
import random
import time
from getpass import getpass       #Esto es para que la eleccion no la vea el otro usuario en el modo multijugador
import os
from shutil import which
from os import system
from _thread import start_new_thread        #TODO ESTO ES PARA EL SECRETO..........
from time import sleep
from server import main
#Importamos random y time


###########################################################FUNCION DE LIMPIAR(OS)############################################################
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")     #HACEMOS LA FUNCION DE BORRAR LA TERMINAL CADA RONDA

########################################################### IMAGENES DE PIEDRA PAPEL TIJERA (ARCII) #########################################
piedra =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)                 
---.__(___)
""")
                                                   #Las formas de piedra papel o tijera en ARCII. Fuente: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
papel = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

tijera = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

################################################################# VARIABLES ##############################################################
puntuacion_jugador_1 = 0
puntuacion_jugador_2 = 0
Fin_Juego = False
usuario = 0
maquina_puntuacion = 0
jugar_contra_ia = 0
################################################################# CODIGO #################################################################
print("Bienvenido a PIEDRA PAPEL TIJERA. By Lander")
time.sleep(2)
decision_inicial = str(input("Que quieres: Jugar contra ia o multijugador: ")).lower()
time.sleep(2)

# Pedir nombres solo si es multijugador
if decision_inicial == "multijugador":
    nombre1 = str(input("Ingrese el nombre del primer jugador: "))
    nombre2 = str(input("Ingrese el nombre del segundo jugador: "))

while not Fin_Juego:
    if decision_inicial == "ia":
        ############################################################### PIEDRA PAPEL TIJERA CONTRA IA ############################################
        print("BIENVENDO A PIEDRA, PAPEL, TIJERA BY LANDER (CONTRA UNA IA)")

        eleccion_usuario = int(input("PIEDRA PAPEL TIJERA. Elije. 1. Piedra 2. Papel 3. Tijera: "))
        maquina = random.randint(1,3)
        if maquina == 1 and eleccion_usuario == 1:            #Machina Piedra, Tu Piedra
            print("Empate. Ambos habeis sacado piedra")
            print(piedra)
            print(f"Puntuacion de la machina: {maquina_puntuacion}")
            time.sleep(1)
            print(f"Puntuacion tuya: {usuario}")
            time.sleep(1)
            limpiar()

        elif maquina == 1 and eleccion_usuario == 2:          #Machina Piedra, Tu Papel
            print("ENHORABUENA. El ha sacado piedra")
            usuario = usuario + 1
            print(piedra)
            time.sleep(2)
            print(f"Puntuacion de la machina: {maquina_puntuacion}")
            time.sleep(1)
            print(f"Puntuacion tuya: {usuario}")
            time.sleep(1)
            limpiar()

        elif maquina == 1 and eleccion_usuario == 3:          #Machina Piedra, Tu Tijera
            print("Has perdido. El ha sacado piedra")
            machina_puntuacion = maquina_puntuacion + 1
            print(piedra)
            time.sleep(2)
            print(f"Puntuacion de la machina: {maquina_puntuacion}")
            time.sleep(1)
            print(f"Puntuacion tuya: {usuario}")
            time.sleep(1)
            limpiar()

        elif maquina == 2 and eleccion_usuario == 1:        #Machina Papel, Tu Piedra
            print("Has perdido. El ha sacado papel")
            print(papel)
            maquina_puntuacion = maquina_puntuacion + 1
            time.sleep(2)
            print(f"Puntuacion de la machina: {maquina_puntuacion}")
            time.sleep(1)
            print(f"Puntuacion tuya: {usuario}")
            time.sleep(1)
            limpiar()

        elif maquina == 2 and eleccion_usuario == 2:       #Machina Papel, Tu Papel
            print("Empate. El ha sacado papel")
            print(papel)
            time.sleep(2)
            print(f"Puntuacion de la machina: {maquina_puntuacion}")
            time.sleep(1)
            print(f"Puntuacion tuya: {usuario}")
            time.sleep(1)
            limpiar()

        elif maquina == 2 and eleccion_usuario == 3:        #Machina Papel, Tu Tijera
            print("ENHORABUENA. El ha sacado papel")
            print(papel)
            usuario = usuario + 1
            time.sleep(2)
            print(f"Puntuacion de la machina: {maquina_puntuacion}")
            time.sleep(1)
            print(f"Puntuacion tuya: {usuario}")
            time.sleep(1)
            limpiar()

        elif maquina == 3 and eleccion_usuario == 1:        #Machina Tijera, Tu Piedra
            print("ENHORABUENA. El ha sacado tijera")
            print(tijera)
            usuario = usuario + 1
            time.sleep(2)
            print(f"Puntuacion de la machina: {maquina_puntuacion}")
            time.sleep(1)
            print(f"Puntuacion tuya: {usuario}")
            time.sleep(1)
            limpiar()

        elif maquina == 3 and eleccion_usuario == 2:        #Machina Tijera, Tu Papel
            print("Has perdido. El ha sacado tijera")
            machina_puntuacion = maquina_puntuacion + 1
            print(tijera)
            time.sleep(2)
            print(f"Puntuacion de la machina: {maquina_puntuacion}")
            time.sleep(1)
            print(f"Puntuacion tuya: {usuario}")
            time.sleep(1)
            limpiar()

        elif maquina == 3 and eleccion_usuario == 3:       #Machina Tijera, Tu Tijera
            print("Empate. El ha sacado tijera")
            print(tijera)
            time.sleep(2)
            print(f"Puntuacion de la machina: {maquina_puntuacion}")
            time.sleep(1)
            print(f"Puntuacion tuya: {usuario}")
            time.sleep(1)
            limpiar()

        else:
            print("Has introducido un valor erroneo. Vuelve a empezar")
            time.sleep(2)
            limpiar()

        if maquina_puntuacion or usuario == 3:
            Fin_Juego = True

        ######################################################### PIEDRA PAPEL TIJERA (MULTIJUGADOR)##############################################################################

    elif decision_inicial == "multijugador":
        print("BIENVENDO A PIEDRA, PAPEL, TIJERA BY LANDER (VERSION MULTIJUGADOR)")
        eleccion_jugador_1 = getpass("Elije. 1. Piedra 2. Papel 3. Tijera: ").lower()    #ELECCION DE PIEDRA PAPEL TIJERA
        eleccion_jugador_2 = getpass("Elije. 1. Piedra 2. Papel 3. Tijera: ").lower()

        if eleccion_jugador_1 or eleccion_jugador_2 == "lander":
            print("Ese nombre me resulta familiar. 🧐")

        if eleccion_jugador_1 == "piedra" and eleccion_jugador_2 == "piedra":
            print(f"JUGADOR 1: {piedra}.")
            time.sleep(2)
            print(f"JUGADOR 2: {piedra}.")
            time.sleep(2)                                                                               #JUGADOR 1: 
            print("EMPATE. Ambos habeis sacado piedra")
            time.sleep(1)
            print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
            print(f"Puntuación del jugador 2:  {puntuacion_jugador_2}")
            time.sleep(3)
            limpiar()

        elif eleccion_jugador_1 == "piedra" and eleccion_jugador_2 == "papel":
            print(f"JUGADOR 1: {piedra}")
            time.sleep(2)
            print(f"JUGADOR 2: {papel}")
            time.sleep(2)
            print("HA GANADO EL JUGADOR 2")
            puntuacion_jugador_2 = puntuacion_jugador_2 + 1
            time.sleep(1)
            print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
            print(f"Puntuación del jugador 2:  {puntuacion_jugador_2}")
            time.sleep(3)
            limpiar()

        elif eleccion_jugador_1 == "piedra" and eleccion_jugador_2 == "tijera":
            print(f"JUGADOR 1: {piedra}")
            time.sleep(2)
            print(f"JUGADOR 2: {tijera}")
            time.sleep(2)
            print("HA GANADO EL JUGADOR 1")
            puntuacion_jugador_1 = puntuacion_jugador_1 + 1
            time.sleep(1)
            print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
            print(f"Puntuación del jugador 2:  {puntuacion_jugador_2}")
            time.sleep(3)
            limpiar()

        elif eleccion_jugador_1 == "papel" and eleccion_jugador_2 == "piedra":
            print(f"JUGADOR 1: {papel}")
            time.sleep(2)
            print(f"JUGADOR 2: {piedra}")
            time.sleep(2)
            print("HA GANADO EL JUGADOR 1")
            puntuacion_jugador_1 = puntuacion_jugador_1 + 1
            time.sleep(1)
            print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
            print(f"Puntuación del jugador 2:  {puntuacion_jugador_2}")
            time.sleep(3)
            limpiar()

        elif eleccion_jugador_1 == "papel" and eleccion_jugador_2 == "papel":
            print(f"JUGADOR 1: {papel}")
            time.sleep(2)
            print(f"JUGADOR 2: {papel}")
            time.sleep(2)
            print("Empate. Ambos habeis sacado papel")
            time.sleep(1)
            print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
            print(f"Puntuación del jugador 2  :{puntuacion_jugador_2}")
            time.sleep(3)
            limpiar()

        elif eleccion_jugador_1 == "papel" and eleccion_jugador_2 == "tijera":
            print(f"JUGADOR 1: {papel}")
            time.sleep(2)
            print(f"JUGADOR 2: {tijera}")
            time.sleep(2)
            print("HA GANADO EL JUGADOR 2")
            puntuacion_jugador_2 = puntuacion_jugador_2 + 1
            time.sleep(1)
            print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
            print(f"Puntuación del jugador 2:  {puntuacion_jugador_2}")
            time.sleep(3)
            limpiar()

        elif eleccion_jugador_1 == "tijera" and eleccion_jugador_2 == "piedra":
            print(f"JUGADOR 1: {tijera}")
            time.sleep(2)
            print(f"JUGADOR 2: {piedra}")
            time.sleep(2)
            print("HA GANADO EL JUGADOR 2")
            puntuacion_jugador_2 = puntuacion_jugador_2 + 1
            time.sleep(1)
            print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
            print(f"Puntuación del jugador 2:  {puntuacion_jugador_2}")
            time.sleep(3)
            limpiar()

        elif eleccion_jugador_1 == "tijera" and eleccion_jugador_2 == "papel":
            print(f"JUGADOR 1: {tijera}")
            time.sleep(2)
            print(f"JUGADOR 2: {papel}")
            time.sleep(2)
            print("HA GANADO EL JUGADOR 1")
            puntuacion_jugador_1 = puntuacion_jugador_1 + 1
            time.sleep(1)
            print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
            print(f"Puntuación del jugador 2:  {puntuacion_jugador_2}")
            time.sleep(3)
            limpiar()

        elif eleccion_jugador_1 == "tijera" and eleccion_jugador_2 == "tijera":
            print(f"JUGADOR 1: {tijera}")
            time.sleep(2)
            print(f"JUGADOR 2: {tijera}")
            time.sleep(2)
            print("Empate. Ambos habeis sacado tijera")
            time.sleep(1)
            print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
            print(f"Puntuación del jugador 2:  {puntuacion_jugador_2}")
            time.sleep(3)
            limpiar()

        else:
            print("HAS INTRODUCIDO UN VALOR EQUIVOCADO. VUELVE A EMPEZAR")
            time.sleep(1)
            limpiar()

        if puntuacion_jugador_1 == 3 or puntuacion_jugador_2 == 3:
            if puntuacion_jugador_1 == 3:
                print("FIN DEL JUEGO. HA GANADO EL JUGADOR 1")
                time.sleep(1)
                print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
                print(f"Puntuación del jugador 2:  {puntuacion_jugador_2}")
                time.sleep(3)
                limpiar()
                Fin_Juego = True
            else:
                print("FIN DEL JUEGO. HA GANADO EL JUGADOR 2")
                time.sleep(1)
                print(f"Puntuación del jugador 1:  {puntuacion_jugador_1}")
                print(f"Puntuación del jugador 2:  {puntuacion_jugador_2}")
                time.sleep(3)
                limpiar()
                Fin_Juego = True

    elif decision_inicial =="secreto":
        python_path = which("python")
        python3_path = which("python3")
        if (python3_path is None) or (python_path and (("WindowsApps" in python3_path) or ("mingw64" in python3_path))):
            cmd = "python"
        else:
            cmd = "python3"

        counted = 0
        start_new_thread(main, ())


        def threadeded():                                        #TODO ESTE CODIGO ES SACADO DE GITHUB: https://github.com/ImPavloh/DesktopLimboKeys
            global counted
            system(cmd + " key.py")
            counted -= 1


        for _ in range(8):
            counted += 1
            start_new_thread(threadeded, ())
            sleep(0.23)

        while counted:
            sleep(0.1)

        break


time.sleep(1)
print("GRACIAS POR JUGAR")
