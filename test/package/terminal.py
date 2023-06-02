import pygame

class Terminal:
    '''Clase que se encarga de controlar los comandos'''

    def __init__(self,game):
        self.game = game
        self.input_rect = pygame.Rect(10, 10, 780, 30)
        self.input_text = ""
    
    def draw_decoration(self):
        '''Dibuja la decoracion de la terminal'''
        ventana_principal = self.game.ventana_principal

        for j in range(3):
            for i in range(800):
                ventana_principal.set_at((0 + i , 50 - j), (120,120,120))
