
import csv

################ MATRIZ RESPUESTA #########################

def cargar_matriz_csv(nombre_archivo: str) -> tuple:
    matriz = []
    with open(nombre_archivo, newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for fila in lector:
            fila_convertida = tuple(int(valor) for valor in fila)  # tupla
            matriz.append(fila_convertida)
    return tuple(matriz) 

############################# TABLERO #######################

def mostrar_matriz_console(matriz: tuple) -> None:
    for fila in matriz:
        linea = []
        
        for celda in fila:
            if celda == 0:
                linea.append(".")
            elif celda == 1:
                linea.append("#")
            elif celda == 2:
                linea.append("X")
        print(" ".join(linea))


def marcar_celda(matriz_jugador: list, 
                coordenadas: tuple, 
                accion: str) -> None:
    
    fila, columna = coordenadas  
    
    if accion == "negro":
        matriz_jugador[fila][columna] = 1
    elif accion == "cruz":
        matriz_jugador[fila][columna] = 2
    else:
        matriz_jugador[fila][columna] = 0


def crear_matriz_vacia(filas: int, columnas: int) -> list:
    matriz_vacia = []
    
    for _ in range(filas):
        fila = [0] * columnas
        matriz_vacia.append(fila)
    return matriz_vacia

######################## PISTAS ###############

def cargar_pistas_csv(nombre_archivo: str) -> list:
    pistas = []   
    
    with open(nombre_archivo, newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:        
            pista_fila = []        
            for valor in fila:     
                numero = (valor)    
                pista_fila.append(numero)   
            pistas.append(pista_fila)  
    return pistas


def mostrar_pistas_filas(pistas: list) -> list:
    
    for pista in pistas:
        linea = ""
        for num in pista:
            linea += str(num) + " "
        print(linea.strip())
    return pistas


def mostrar_pistas_columnas(pistas: list) -> list:
    for pista in pistas:
        linea = ""
        for num in pista:
            linea += str(num) + " "
        print(linea.strip())
    return pistas

######################### RANKING #######################

def guardar_ranking(nombre_archivo: str, 
                    nombre_jugador: str, 
                    tiempo: float, 
                    estado: str) -> None:
    with open(nombre_archivo, "a") as archivo:
        
        registro = {
            "nombre": nombre_jugador,
            "tiempo": tiempo,
            "estado": estado
        }
        cargar_registro = (f"{registro['nombre']},{registro['tiempo']},{registro['estado']}\n")
        archivo.write(cargar_registro)


def leer_ranking(nombre_archivo: str) -> list:
    ranking = []
    
    with open(nombre_archivo, 'r', newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            nombre_jugador = fila[0]
            tiempo = float(fila[1])
            estado = fila[2]
            ranking.append((nombre_jugador, tiempo, estado))
            
    ranking_ordenado = sorted(ranking, key=lambda x: x[1])
    return ranking_ordenado