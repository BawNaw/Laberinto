import pygame

class Raton:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.posicion = [1, 1]
        self.tamaño = 40
        self.color = (128, 128, 128)
        self.camino = [(1, 1)]
        self.color_camino = (255, 105, 180)

    def establecer_posicion(self, nueva_pos):
        if not self.colisiona_con_pared(nueva_pos):
            self.posicion = nueva_pos
            self.camino.append((nueva_pos[0], nueva_pos[1]))

    def colisiona_con_pared(self, nueva_pos):
        for pared in self.laberinto.paredes:
            if pared.rect.collidepoint(nueva_pos[0] * self.tamaño, nueva_pos[1] * self.tamaño):
                return True
        return False

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.posicion[0] * self.tamaño, self.posicion[1] * self.tamaño, self.tamaño, self.tamaño))

    def limpiar_posicion_anterior(self):
        x, y = self.posicion
