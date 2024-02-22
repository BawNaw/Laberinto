# Archivo caminos.py
from laberinto import Laberinto
from collections import deque

def explorar_caminos(inicio, fin):
    laberinto_instancia = Laberinto()
    matriz = laberinto_instancia.matriz
    
    def backtrack(actual, camino):
        if actual == fin:
            caminos.append(camino.copy())
            return
        x, y = actual
        matriz[x][y] = 2
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]) and matriz[nx][ny] == 0:
                backtrack((nx, ny), camino + [(nx, ny)])
        matriz[x][y] = 0
    
    caminos = []
    backtrack(inicio, [inicio])
    return caminos