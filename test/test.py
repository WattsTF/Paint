import sys
import math
import pygame
from package.settings import RESOLUCION
from package.terminal import Terminal
from package.dibujador import Dibujador

class Paint:
    '''Clase principal de la aplicacion'''

    def __init__(self):
        pygame.init()
        
        self.ventana_principal = pygame.display.set_mode(RESOLUCION)
        self.backgroung_color = (255, 255, 255)
        self.line_color = (0, 0, 0)
        self.terminal = Terminal(self)
        self.dibujador = Dibujador(self)

    def run(self):
        while True:
            #---------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #---------

                # Dibujar la entrada de texto
            pygame.draw.rect(self.ventana_principal, (200, 200, 200), self.terminal.input_rect)
            fuente = pygame.font.Font(None, 24)
            texto_superficie = fuente.render(self.terminal.input_text, True, (0, 0, 0))
            self.ventana_principal.blit(texto_superficie, (self.terminal.input_rect.x + 5, self.terminal.input_rect.y + 5))

            self.update()

    def update(self):
        pygame.display.flip()            
            





if __name__ == '__main__':
    paint = Paint()
    paint.run()