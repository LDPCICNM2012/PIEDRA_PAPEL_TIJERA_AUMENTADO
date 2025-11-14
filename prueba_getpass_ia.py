from getpass import getpass
import os
print("HOLA MUNDO")
eleccion = getpass("Elige piedra, papel o tijera: ").lower()
print("Has elegido:", eleccion)


#################################################FUNCION PARA BORRAR LA TERMINAL EN UN CODIGO DE PY>THON(CHATGPT ME HA ENSEÑADO ESTA FUNCION)###############

# def limpiar():
#     os.system("cls" if os.name == "nt" else "clear")     #AQUI SE CREA LA FUNCION DE BORRAR LA TERMINAL OS,SYSTEM ES PARA EJECUTAR UN COMANDO DE LA TERMINAL
#                                                          #"cls" se usa si el sistema es Windows (os.name=="nt"), y "clear" si es Linux o macOS; os.name devuelve el tipo de sistema operativo
# while True:
#     limpiar()
#     # aquí empieza la ronda
#     print("Nueva ronda: piedra, papel o tijera")
#     # ... resto del código del juego ...


import os
import time

# Definimos la función para limpiar la terminal
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# Ejemplo simple de "rondas"
for ronda in range(1, 4):
    limpiar()
    print(f"Ronda {ronda}")
    eleccion = input("Elige piedra, papel o tijera: ")
    print(f"Has elegido: {eleccion}")
    time.sleep(2)  # espera 2 segundos antes de la siguiente ronda


#############################################A PARTiR DE AQUI TODO SON PRUEBAS Q HE HECHO YO#########################################


