import random

class Juego : #Ver opcion de gestionar todo el juego por medio de una clase 
    def __init__(self,letras,palabras):
        self.lexiletras = letras
        self.lexipalabras = palabras
        self.heptapalabras = []
        self.heptacracks = 0
        self.cantidades = [] # cantidad de palabras que empieza con cada letra 
        self.cant_encontradas = [0,0,0,0,0,0,0]
        self.palabras_encontradas= []
        self.letra_principal = letras[3]
        self.puntos = 0
        self.puntos_max = 0

    def empiezan_con (self):# busca la cantidad de palabra que inicia con cada letra 
     empieza = [] 
     for letra in self.lexiletras:
        contador = 0
        for palabra in self.lexipalabras:
            if palabra[0] == letra:
                contador +=1
        empieza.append(contador)
     self.cantidades = empieza
     self.puntmax()
     
    def heptalexis (self) : #busca la cantidad de palabras que ocupan todas las letras 
     heptacrack = []
     for i in range(len(self.lexipalabras)):
        contador = 0
        for letra in self.lexiletras:
            if letra in self.lexipalabras[i]:
                contador +=1
        if contador == 7 :
            heptacrack.append(self.lexipalabras[i])
     self.heptapalabras = heptacrack
    
    def revisar_palabra(self,palabra):
        if len(palabra)<3 :
            print("\nTu palabra es muy corta, por favor intenta con palabras de 3 letras o mas")
            return False
        for letra in palabra:
            if letra not in self.lexiletras:
                print("\nIngresaste una letra/numero que no se encuentra en el listado, por favor intentalo nuevamente")
                return False
        if self.letra_principal not in palabra:
            print("\nla palabra debe contener la letra central que es",self.letra_principal)
            return False
        if palabra not in self.lexipalabras:
            print("\nPalabra no encontrada")
            return False
        if palabra in self.palabras_encontradas:
            print ("\nYa encontrada")
            return False
        return True 
    
    def asignacion_puntaje(self,palabra): #tambien añade la palabra a la lista de encontradas y al respectivo contador de empieza con...
        if palabra in self.heptapalabras:
            print("Heptacrack!!")
            self.heptacracks += 1
            puntos = 10
        else:
            if len(palabra) == 3:
                puntos = 1
            elif len(palabra) == 4:
                puntos = 2
            else:
                puntos = len(palabra)
        print("Felicidades, has ganado",puntos,"puntos")
        self.puntos += puntos
        self.palabras_encontradas.append(palabra)
        for i in range(len(self.lexiletras)):
            if self.lexiletras[i]== palabra[0]:
                self.cant_encontradas[i] += 1
        
    def enunciado(self):
        texto_letras= " , ".join(self.lexiletras)
        print("\nLetras :",texto_letras)
        print("Letra principal :",self.lexiletras[3]+"\n")
        texto = []
        for i in range(len(self.cantidades)):
            x = "Empieza con " + self.lexiletras[i] + " :" +str(self.cant_encontradas[i])+ " / " +str(self.cantidades[i])
            texto.append(x)
        print("\n".join(texto))
        print("Heptacracks :" , self.heptacracks,"/",len(self.heptapalabras))
        print("\nPuntaje :",self.puntos,"/",self.puntos_max,"\n")

    def puntmax (self):
        suma = 0
        for palabra in self.lexipalabras:
            if palabra in self.heptapalabras:
                puntos = 10
            else:
                if len(palabra) == 3:
                    puntos = 1
                elif len(palabra) == 4:
                    puntos = 2
                else:
                    puntos = len(palabra)
            suma += puntos
        self.puntos_max = suma


def archivo(): #abre archivo castellano sin tildes.txt
    data = open("castellano sin tildes .txt","r")
    data1 = data.read()
    palabras = data1.split("\n")
    return palabras 

def lexiletras(): #consigue 7 letras que se usaran en el juego
    palabras = heptapalabras()
    x = random.randint(0,len(palabras)-1)
    palabra = palabras [x]
    letra = []
    for l in palabra:
        if l not in letra:
            letra.append(l)
    return letra

def buscar_palabras(letras): # buscara todas las palabras validas para el juego
    palabras = archivo()
    palabra = []
    for i in range (len(palabras)):
        agregar = True
        for letra in palabras[i]:
            if letra not in letras:
                agregar = False
        if agregar:
            palabra.append(palabras[i])
    lexipalabras = principales_palabras(letras , palabra)
    return lexipalabras

def principales_palabras(letras , palabras):
    letra = letras[3]
    final = []
    for palabra in palabras:
        if letra in palabra:
            final.append(palabra)
    return final

def heptapalabras ():
    palabras = archivo()
    heptapalabra = []
    for palabra in palabras:
        letras = [] 
        for letra in palabra:
            if letra not in letras:
                letras.append(letra)
        if len(letras) == 7:
            heptapalabra.append(palabra)
    return heptapalabra

def preguntar (x):
    y = input("\n[1] "+ x +"\n[2] Salir\n")
    while y not in ["1","2"]:
        print ("\nOpcion no encontrada , por favor intente nuevamente\n")
        y = input("\n[1] "+ x +"\n[2] Salir\n")
    return y