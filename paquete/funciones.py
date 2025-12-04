
import csv

################ MATRIZ RESPUESTA #########################
def cargar_matriz_csv(nombre_archivo):
    matriz = []  
    
    with open(nombre_archivo, newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for fila in lector:  
            fila_convertida = []        
            for valor in fila:          
                numero = int(valor)   
                fila_convertida.append(numero)  
            matriz.append(fila_convertida)  
    return matriz

############################# TABLERO #######################

def mostrar_matriz_console(matriz):
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

def marcar_celda(matriz_jugador, coordenadas, accion):
    fila, columna = coordenadas  
    
    if accion == "negro":
        matriz_jugador[fila][columna] = 1
    elif accion == "cruz":
        matriz_jugador[fila][columna] = 2
    else:
        matriz_jugador[fila][columna] = 0


def crear_matriz_vacia(filas, columnas):
    matriz_vacia = []
    
    for _ in range(filas):
        fila = [0] * columnas
        matriz_vacia.append(fila)
    return matriz_vacia

######################## PISTAS ###############

def cargar_pistas_csv(nombre_archivo):
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


def mostrar_pistas_filas(pistas):
    for pista in pistas:
        linea = ""
        for num in pista:
            linea += str(num) + " "
        print(linea.strip())
    return pistas


def mostrar_pistas_columnas(pistas):
    for pista in pistas:
        linea = ""
        for num in pista:
            linea += str(num) + " "
        print(linea.strip())
    return pistas

######################### RANKING #######################

def guardar_ranking(nombre_archivo, nombre_jugador, tiempo, estado):
    with open(nombre_archivo, "a") as archivo:
        linea = ""
        fila = [nombre_jugador, tiempo, estado]
        
        for i in range(len(fila)):
            linea += str(fila[i])
            
            if i < (len(fila) - 1):
                linea += ","
        archivo.write(linea + "\n")


def leer_ranking(nombre_archivo):
    ranking = []
    
    with open(nombre_archivo, 'r', newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            nombre_jugador = fila[0]
            tiempo = float(fila[1])
            estado = fila[2]
            ranking.append((nombre_jugador, tiempo, estado))
    return ranking