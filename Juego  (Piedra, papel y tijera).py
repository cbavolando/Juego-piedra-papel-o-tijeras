import random 
opciones = ["piedra", "papel", "tijeras"] 
marcador = dict() 

def juego():#funcion que inicia juego
    turno = random.randint(0,2)
    computadora = opciones[turno]
    print ("Juguemos: piedra, papel o tijeras")
    jugador = input("Seleccione una opcion: ")
    print("Su eleccion fue: ", jugador)
    if (jugador == computadora):
        puntuaciones = 0
        print("empate!")
    if (jugador == "tijeras"):
        if (computadora == "papel"):
            puntuaciones = 1
            print("Ha ganado!")
        if (computadora == "piedra"):
            puntuaciones = 2
            print("Ha perdido! ")        

    elif (jugador == "papel"):
        if (computadora == "piedra"):
            puntuaciones = 1
            print("Ha ganado!")
        if (computadora == "tijeras"):
            puntuaciones = 2
            print("Ha perdido!")

    elif (jugador == "piedra"):
        if (computadora == "tijeras"):
            puntuaciones = 1
            print("Ha ganado!")
        if (computadora == "papel"):
            puntuaciones = 2
            print("Ha perdido!")
    print ("La computadora selecciono:", computadora) 
    return puntuaciones

def pizarra(nombre):#funcion de puntuaciones
    if nombre not in marcador.keys():
        jugador = 0 
    else:
        jugador = marcador[nombre]
    computadora = 0
    n = False
    while n==False:
        puntuaciones = juego()
        if puntuaciones == 1:
            jugador += 1
        elif puntuaciones == 2:
            computadora += 1
        print ("Puntuaciones: computadora -->", computadora, "jugador -->", jugador)
        respuesta=input("¿Quiere seguir jugando?: s/n: ")
        if(respuesta == "n"):
            print("Juego finalizado")
            marcador[nombre] = jugador
            n = True
            
def imprimir_puntuaciones(marcador):#funcion para imprimir puntuacion de manera orderanda
    [print("Nombre: "+ key + " ha ganado " + str(value) + " veces") for key, value in marcador.items()]    
        
while True:#menu
    print("Menu:")
    print("1. Jugar")
    print("2. Puntuaciones")
    print("3. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Introduzca su nombre para puntuacion: ")
        pizarra(nombre)
        
    elif opcion == "2":
        imprimir_puntuaciones(marcador)
    elif opcion == "3":
        print("Gracias por jugar!")
        break    

'''
-Sebastian Alvarez
'''
      
        
        
        
