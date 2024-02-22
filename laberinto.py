import pygame
from pared import Pared
from queso import Queso

class Laberinto:
    def __init__(self):
        self.tamaño = 40 
        
        self.matriz = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        
        self.paredes = self.crear_paredes_desde_matriz()
        
        self.queso = Queso(5 * self.tamaño, 5 * self.tamaño, self)

    def crear_paredes_desde_matriz(self):
        paredes = []
        filas = len(self.matriz)
        columnas = len(self.matriz[0]) if filas > 0 else 0
        
        for fila in range(filas):
            for columna in range(columnas):
                if self.matriz[fila][columna] == 1:
                    paredes.append(Pared(columna * self.tamaño, fila * self.tamaño, self.tamaño))
        return paredes

    def dibujar(self, pantalla):
        for pared in self.paredes:
            self.queso.dibujar(pantalla)
            pared.dibujar(pantalla)