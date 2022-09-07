from funciones import Juego , buscar_palabras , lexiletras , preguntar
#Reglas e Introduccion:
print("\nBienvenido a Lexi Retos\n")
print("¿Como se juega?")
print("En este juego se te entregaran 7 letras , dentro de ellas estara la llamada letra principal.")
print("Con estas letras deberas formar la mayor cantidad de palabras que incluyan dicha letra.")
print("\nReglas:\n")
print("- No se admiten nombres propios ,plurales y formas verbales conjugadas (solo infinitivos).")
print("- Esta version del juego no admite tildes en las palabras y la letra ñ es considerada como n.")
print("\nPuntuación:\n")
print("- Las palabras de 3 letras dan ,1 punto y las de 4 letras ,2 puntos.")
print("- A partir de 5 letras, obtendrás tantos puntos como letras tenga la palabra.")
print("- Los heptacraks , es decir, palabras que contienen todas las letras ,dan 10 puntos.\n")
#Comienzo del juego :
x = input("\n[1] Nueva Partida\n[2] Continuar\n")
while x not in ["1","2"]:
    print("Opcion no encontrada ,por favor intente nuevamente")
    x = input("\n[1] Nueva Partida\n[2] Continuar\n")
if x== "1":
    letras=lexiletras()
if x == "2":
    y = input("nombre :")
    
lexireto = Juego(letras,buscar_palabras(letras))
lexireto.empiezan_con()
lexireto.heptalexis() 
    
 # revisar cuando no se presiona 1 

while x != "1":
    print("Tecla no valida , intente nuevamente\n")
    x = input("Presiona 1 para comenzar\n")
#Flujo del juego :
while x == "1":
     lexireto.enunciado()
     intento = input("Coloque una palabra: ")
     buena = lexireto.revisar_palabra(intento)
     if buena:
        lexireto.asignacion_puntaje(intento)
        x = preguntar("Seguir jugando")
     else:
        x = preguntar("Intentar nuevamente")
print("\n¿Desea guardar el progreso?\n")
y = input("\n[1] Guardar partida\n[2] Salir\n")
while y not in ["1","2"]:
    print("Opcion no encontrada, por favor intente nuevamente")
    y = input("\n[1] Guardar partida\n[2] Salir\n")
if y == "1":
    nombre= input("nombre :")
    jugador = open("jugadores.txt","a")
    jletras = ",".join(lexireto.lexiletras)
    jpalabras = ",".join(lexireto.palabras_encontradas)
    texto = ";\n" + nombre + "\n" + jletras + "\n" + jpalabras
    jugador.write(texto)
    jugador.close() 