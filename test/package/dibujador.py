import math
import pygame

class Dibujador:
    '''Clase encargada de dibujar en la pantalla'''

    def __init__(self, game):
        self.game = game


    def dibujar_linea(self, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1
        err = dx - dy

        while x1 != x2 or y1 != y2:
            self.game.ventana_principal.set_at((x1, y1), self.game.line_color)
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
        
    def dibujar_linea_horizontal_positiva(self, x, y, longitud):
        if longitud > 0:
            for i in range(longitud):
                if x + i < 800 and y > 50:
                    ventana_principal.set_at((x + i, y), line_color)