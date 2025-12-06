
from paquete.funciones import *

def validar_fila_columna(valor_maximo: int, 
                        valor_actual: int) -> int:
    
    valido = True
    
    while valido:
        if valor_maximo < valor_actual or valor_actual < 0:
            print("Ese numero esta fuera del parametro")
            valido = True
            valor_actual = int(input("Vuelva a ingresar numero: "))
        else:
            valido = False
            return valor_actual


def validar_accion(accion: str) -> str:
    acciones_validas = ["negro", "cruz", "borrar"]
    
    while accion not in acciones_validas:
        print("Acción no valida. Las acciones permitidas son: negro, cruz, borrar.")
        accion = input("Ingrese acción (negro, cruz, borrar): ")
    return accion


def comprobar_jugada_tablero(matriz_respuesta: list, 
                            accion: str, 
                            fila: int, 
                            columna: int) -> bool:
        
    if accion == "negro":
        movimiento_jugador = 1
    elif accion == "cruz":
        movimiento_jugador = 0 
    
    valor_correcto = matriz_respuesta[fila][columna]
    
    if movimiento_jugador == valor_correcto:
        return True
    else:
        return False

def verificar_gano_perdio(matriz_jugador: list, 
                        matriz_respuesta: list) -> bool:
    
    for i in range(len(matriz_respuesta)):
        for j in range(len(matriz_respuesta[i])):
            if matriz_respuesta[i][j] == 1 and matriz_jugador[i][j] != 1:
                return False
            if matriz_respuesta[i][j] == 0 and matriz_jugador[i][j] == 1:
                return False
    return True
