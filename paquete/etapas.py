
from paquete.funciones import *
from paquete.validaciones import validar_fila_columna, validar_accion, comprobar_jugada_tablero, verificar_gano_perdio
import time

def jugar(nombre: str) -> tuple:
    
    tiempo_inicio = time.time()
    matriz_jugador = crear_matriz_vacia(4, 12)
    pistas_filas = cargar_pistas_csv("archivos/pistas_filas.csv")
    pistas_columnas = cargar_pistas_csv("archivos/pistas_columnas.csv")
    matriz_respuesta = cargar_matriz_csv("archivos/llave.csv")
    vidas = 3
    jugando = True
    
    while jugando:
        
        print("\n=== PISTAS FILAS ===")
        mostrar_pistas_filas(pistas_filas)
        print("\n=== PISTAS COLUMNAS ===")
        mostrar_pistas_columnas(pistas_columnas)
        
        print("\n=== TABLERO ===")
        mostrar_matriz_console(matriz_jugador)
        
        
        print("Ingrese las coordenadas y la acción que desea realizar")
        fila = int(input("Fila: "))
        fila = validar_fila_columna(3, fila)
        
        columna = int(input("Columna: "))
        columna = validar_fila_columna(11, columna)
        
        accion = input("Acción (negro, cruz, borrar): ").lower()
        accion = validar_accion(accion)
        
        coord = (fila, columna)
        verificacion = comprobar_jugada_tablero(matriz_respuesta, accion, fila, columna)
        if verificacion:
            print("Correcto")
            marcar_celda(matriz_jugador, coord, accion)
            
            if verificar_gano_perdio(matriz_jugador, matriz_respuesta):
                print("""
                    ========================
                            GANASTE
                    ========================
                """)
                jugando = False
                continue
        else:
            print("Incorrecto")
            vidas -= 1
            print(f"Vidas restantes: {vidas}")
            
            if vidas == 0:
                print("Perdiste todas las vidas")
                jugando = False
                
    resultado = verificar_gano_perdio(matriz_jugador, matriz_respuesta)
    tiempo_final = time.time()
    duracion = tiempo_final - tiempo_inicio
    
    return resultado, duracion