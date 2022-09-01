from linecache import getline
from random import randint
from clases import Juego 

palabra = getline('diccionario.txt', randint(1, 80383)).strip('\n')
usuario = input('Ingrese su nombre de usuario: ')

print(f'''
BIENVENIDO {usuario} AL COLGADO

- Intenta salvarte con 7 vidas:\n''')

while True:
    jugador = Juego(usuario, palabra)
    jugador.jugada()
    break