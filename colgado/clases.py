class Juego:

    def __init__(self, usuario, palabra):
        
        self.usuario = usuario
        self.vidas = 7
        self.palabra = palabra
        self.palabra_oculta = [letra for letra in self.palabra]
        self.palabra_expuesta = ['_' for indice in range(len(self.palabra_oculta))]
    
    def jugada(self):
        
        while True:

            verificador = False
            print(' '.join(self.palabra_expuesta))
            print('')
            
            if self.palabra_oculta == self.palabra_expuesta:
                print(f'FELICITACIONES {self.usuario} TE HAS SALVADO')
                return 1
            elif self.vidas == 0:
                print(f'Defraudaste a Jorge Muñoz, la palabra era {self.palabra.upper()}')
                return 0
            
            while verificador == False:
                seleccion = input('Seleccione una letra (á - z): ')
                print('')
                if seleccion.isalpha() == True:
                    verificador = True
                    seleccion = seleccion.lower()
                else:
                    print(f'\nPorfavor intente con una letra')
            
            letra_buena = False
            for indice in range(len(self.palabra_oculta)):
                if self.palabra_oculta[indice] == seleccion:
                    letra_buena = True
                    self.palabra_expuesta[indice] = seleccion
            
            if letra_buena == True:
                print(f'Excelente {self.usuario}, sigues vivo\n')
            
            elif self.vidas - 1 >= 0:
                self.vidas -= 1
                if self.vidas in [6, 5]:
                    print(f'Tranquilo, todavía te quedan {self.vidas} vidas\n')
                elif self.vidas in [4, 3]:
                    print(f'Ojo!! te quedan tan solo {self.vidas} vidas\n')
                elif self.vidas == 2:
                    print(f'Últimas vidas, piensa antes de actuar...\n')
                else:
                    print(f'Siempre supimos que {self.usuario} era una buena persona\n')
