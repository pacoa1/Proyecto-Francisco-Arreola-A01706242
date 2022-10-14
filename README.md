# Primer Avance

Para este primer avance de proyecto, decidí realizar un juego conocido cmomo ahorcado, debido a que me parece un proyecto complejo, en el cual podré demostrar las competencias que se necesitan para este primer semestre. Además considero que también podría reflejar todo lo aprendido en clases, en los exámenes y actividades realizadas a lo largo del semestre. En esta primera entrega realizare una parte del pseudocódigo, para posteriormente empezar a programarlo como un código.
Con esta segunda entrega, entregare la primera parte del codigo. Ya empezando a darle estructura. En esta tercera entrega, voy a definir algunas funciones para poder utilizarlas con todas las variables que quiero poner.

# Pseudocodigo
Inicio
("Bienvenido al mejor juego de ahorcado, a continuacion se desplegara un menu con tres secciones distintas y se te asignara una palabra aleatoria. No olvides que tienes tres intentos para adivinar la pregunta")

Menu
Deportes
Frutas
Peliculas

Deportes = (Futbol, Basquetbol, Natación)
Frutas = (Manzana, Pera, Platano)
Peliculas = (Batman, Thor, Avengers)
Vidas = 3

Si (Deportes)
  Desplegar primera pista al usuario ("Es el deporte mas popular del mundo")  
Pedir a usuario respuesta("Ingresa tu respuesta")

Si respuesta = (Futbol)
  Desplegar al usuario ("Felicidades, lo hiciste a la primera")
  
Sino
  Desplegar a usuario segunda pista ("Es un deporte que se juega con los pies")
  Pedir a usuario respuesta("Ingresa tu respuesta")
  
Si respuesta = (Futbol)
  Desplegar al usuario ("Felicidades, lo lograste")
  
Sino
  Desplegar a usuario tercera pista ("El mejor jugador de este deporte es Cristiano Ronaldo")
  Pedir a usuario respuesta("Ingresa tu respuesta")
  
 Si respuesta = (Futbol)
  Desplegar al usuario ("Felicidades, la tercera es la vencida.")
  
 Sino
  Desplegar a usuario ("Animo, puedes volverlo a intentar")
 
 Si (Fruta)
  Desplegar primera pista al usuario ("Es una fruta que crece de los arboles")  
Pedir a usuario respuesta("Ingresa tu respuesta")

Si respuesta = (Manzana)
  Desplegar al usuario ("Felicidades, lo hiciste a la primera")
  
Sino
  Desplegar a usuario segunda pista ("Hay de muchos colores, los mas comunes son el rojo, amarillo y verde")
  Pedir a usuario respuesta("Ingresa tu respuesta")
  
Si respuesta = (Manzana)
  Desplegar al usuario ("Felicidades, lo lograste")
  
Sino
  Desplegar a usuario tercera pista ("Es el logo de una marca muy famosa de electrónicos")
  Pedir a usuario respuesta("Ingresa tu respuesta")
  
 Si respuesta = (Manzana)
  Desplegar al usuario ("Felicidades, la tercera es la vencida")
  
 Sino
  Desplegar a usuario ("Animo, puedes volverlo a intentar")
  
  Si (Peliculas)
  Desplegar primera pista al usuario ("Es una pelicula de la marca Dc comics")  
Pedir a usuario respuesta("Ingresa tu respuesta")

Si respuesta = (Batman)
  Desplegar al usuario ("Felicidades, lo hiciste a la primera")
  
Sino
  Desplegar a usuario segunda pista ("El color de su traje es negro")
  Pedir a usuario respuesta("Ingresa tu respuesta")
  
Si respuesta = (Batman)
  Desplegar al usuario ("Felicidades, lo lograste")
  
Sino
  Desplegar a usuario tercera pista ("Esta relacionado con murciélagos ")
  Pedir a usuario respuesta("Ingresa tu respuesta")
  
 Si respuesta = (Batman)
  Desplegar al usuario ("Felicidades, la tercera es la vencida")
  
 Sino
  Desplegar a usuario ("Animo, puedes volverlo a intentar")
