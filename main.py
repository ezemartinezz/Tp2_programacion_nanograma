
from paquete.funciones import *
from paquete.etapas import *

bandera = True

while bandera:
    
    print("-----------------------------")
    print("       MENU PRINCIPAL        ")
    print("-----------------------------")
    print("1. Entrar al juego")
    print("2. Ver ranking")
    print("3. Salir")
    print("-----------------------------")
    
    opcion = input("Seleccione una opcion (1-3): ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del jugador: ")
        print(f"¡Bienvenido al juego, {nombre}!")
        
        resultado, duracion = jugar(nombre)
        
        if resultado:
            estado = "GANO"
        else:
            estado = "PERDIO"
        guardar_ranking("archivos/ranking.csv", nombre, duracion, estado)
        
    elif opcion == "2":
        print("Ranking de jugadores:")
        ranking = leer_ranking("archivos/ranking.csv")
        for i, (nombre_jugador, tiempo, estado) in enumerate(ranking, start=1):
            print(f"{i}. {nombre_jugador} - Tiempo: {tiempo:.2f} segundos - Estado: {estado}")
            
    elif opcion == "3":
        print("Saliendo del programa.")
        bandera = False
    else:
        print("Opcion no válida. Intente de nuevo.")
