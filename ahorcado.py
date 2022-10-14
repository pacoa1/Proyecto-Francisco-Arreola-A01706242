print("Bienvenido al mejor juego del mundo, las reglas consisten en que se tienen tres oportunidades para adivinar la respuesta correcta. Tras cada intento se desplegara una pista")
vidas=3
palabra = 'manzana'
respuesta = " "

while vidas > 0 :
    fallas = 0
    for letra in palabra:
        if letra in respuesta:
            print ( letra = "")
        else:
         print("*")
        fallas+=1
    if fallas==0:
        print("Respuesta Correcta")
        break
    let=input("Ingresa una letra: ")
    respuesta+=let
    if let not in palabra:
        vidas-=1
        print("Error")
    if vidas==0:
        print("Mal ahi")
else:
    print("Nos vemos pronto")
   
