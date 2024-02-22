import pygame

class Pared:
    def __init__(self, x, y, tamaño):
        self.rect = pygame.Rect(x, y, tamaño, tamaño)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (255, 255, 0), self.rect)
