import pygame

class Queso:
    def __init__(self, x, y, laberinto):
        self.posicion = (x, y)
        self.tamaño = 40 
        self.color = (254, 204, 0)
        self.laberinto = laberinto

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.posicion[0], self.posicion[1], self.tamaño, self.tamaño))

