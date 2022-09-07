from re import L
import random
import WordleESprep as prep
print("Bienvenido a Wordle ES!!\n"
"REGLAS\n"
"-Cuando la letra está en blanco significa que no está en la palabra\n"
"-Cuando la letra está en amarillo significa que está en la palabra pero no en esa posición\n"
"-Cuando la letra está en verde significa que está en la palabra y en la posición correcta\n"
"\n"
"Elige un estilo de juego:\n"
"1 > 5 letras\n"
"2 > 6 letras\n"
"3 > 7 letras\n")
dificultad = int(input("Estilo: "))
print("\nYa puedes jugar!!\n")

if dificultad == 1:
  juego=prep.palabras5
elif dificultad == 2:
  juego=prep.palabras6
elif dificultad == 3:
  juego=prep.palabras7

n=random.randint(0,len(juego))
pista=juego[n]

turnos=0
play = input()
print("")
intentos=""

while play!=pista and turnos<6:
  mod=""
  letras=list(pista)
  if play not in juego:
    print("La palabra no está en la lista")
  else:
    turnos+=1
    for i in range(0,len(play)):
      if play[i] not in pista:
        mod=mod+play[i]
      elif play[i]==pista[i]:
        l=prep.color.green+play[i]+prep.color.end
        mod=mod+l
        if play[i] in letras:
           letras.remove(play[i])
      else:
        if play[i] in letras:
          l=prep.color.yellow+play[i]+prep.color.end
          mod=mod+l
          if play[i] in letras:
            letras.remove(play[i])
        else:
          mod=mod+play[i]
    mod=mod+"\n"
    intentos=intentos+mod
  print(intentos)
  if turnos<=5 and play!=pista:
    play = input()
    print("")
  else:
    pass

if play==pista:
  play=prep.color.green+play+prep.color.end
  intentos=intentos+play
  print(intentos)
  print("GANASTE!!")
else:
  print("Se te acabaron los intentos :(")
  print("La palabra era", pista.upper())