import random

print ("Bienvenido al mejor juego de ahorcado, a continuacion se desplegara una horca y se te asignara una palabra aleatoria \n tendras que contestarla sin equivocarte mucho para salvar al personaje.\n No olvides que tienes tres intentos para adivinar la pregunta. \n Las palabras que tendras que adivinar son las siguientes \n Batman, Thor, Avengers, Manzana, Pera, Platano, Futbol, Basquetbol, Natacion\n Suerte!!!")

Personaje = [ #Personaje del ahorcado
    '''
    +-----+
    |     |
          |
          |
          |
          | 
         ===========
    ''',
     '''
    +-----+
    |     |
    O     |
          |
          |
          | -1 VIDAS
          ===========
    ''',
    '''
    +-----+
    |     |
    O     |
    |     |
          |
          | -2 VIDAS
         ===========
    ''',
     '''
    +-----+
    |     |
    O     |
    |\    |
          |
          | - 3 VIDAS
          ===========
    ''',
     '''
    +-----+
    |     |
    O     |
   /|\    |
          |
          | - 4 VIDAS
          ===========
    ''',
     '''
    +-----+
    |     |
    O     |
   /|\    |
     \    |
          | - 5 VIDAS
          ===========
    ''',
     '''
    +-----+
    |     |
    O     |
   /|\    |
   / \    |
          | FALLASTE
          ===========
    ''',

]

Opciones = ["Futbol", "Basquetbol", "Natación", "Manzana", "Pera", "Platano", "Batman", "Thor", "Avengers"] #Lista de palabras para el juego

Palabra_aleatoria = random.choice (Opciones) # Variable para las palabras al azar

def estructura_juego (): #Estructura del juego completo, con esta funcion desarrollada se puede jugar Ahorcado
    Palabra_Completa = Palabra_aleatoria
    Palabras_Secretas = []
    lista_palabras = []
    for i in Palabra_Completa:
        Palabras_Secretas.append (i)
        lista_palabras.append (" _ ")
    Personaje_Posicion = 0
    print (Personaje[Personaje_Posicion])
    print (",".join(lista_palabras))

    while True:
        Letra_Usuario = input("Ingresa una letra para jugar ")
        acumulador = -1
        palabra = False
        for i in Palabra_Completa:
            acumulador += 1
            if Letra_Usuario == i :
                lista_palabras [acumulador] = i
                palabra = True
        if  Palabras_Secretas == lista_palabras:
            print ("Felicidades, lo lograste antes de que se te acabaran las vidas!!!!")
            break
        if Personaje_Posicion >= 5 and palabra != True:
            print (Personaje [6])
            print ("Perdiste, pero puedes seguir intentando, la respuesta correcta es " ,'' .join( Palabras_Secretas) )
            break
        elif palabra != True:
            Personaje_Posicion += 1

        print (Personaje[Personaje_Posicion])
        print (",".join(lista_palabras))

estructura_juego ()
