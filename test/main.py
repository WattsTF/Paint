import pygame
import sys
import math

pygame.init()

# Colores
background_color = (255, 255, 255)
line_color = (0, 0, 0)    

# Crear la ventana principal
ventana_principal = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Maravilloso Paint")
ventana_principal.fill(background_color)

# Variables para la entrada de texto
input_rect = pygame.Rect(10, 10, 780, 30)
input_text = ""
for j in range(3):
    for i in range(800):
        ventana_principal.set_at((0 + i , 50 - j), (120,120,120))

# Comandos
def dibujar_linea(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    err = dx - dy

    while x1 != x2 or y1 != y2:
        ventana_principal.set_at((x1, y1), line_color)
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
def fondo(color_fondo): #Revisar
    ventana_principal.fill(color_fondo)

def size_pixel(x, y, size): #Revisar
    for i in range(size):
        for j in range(size):
            ventana_principal.set_at((x * size + i, y * size + j), line_color)

def dibujar_linea_horizontal_positiva(x, y, longitud):
    if longitud > 0:
        for i in range(longitud):
            if x + i < 800 and y > 50:
                ventana_principal.set_at((x + i, y), line_color)

def dibujar_linea_horizontal_negativa(x, y, longitud):
    if longitud > 0:
        for i in range(longitud):
            if x + i < 800 and y > 50:
                ventana_principal.set_at((x - i, y), line_color)

def dibujar_linea_vertical_positiva(x, y, longitud):
    if longitud > 0:
        for i in range(longitud):
            if x < 800 and y + i > 50:
                ventana_principal.set_at((x , y - i), line_color)

def dibujar_linea_vertical_negativa(x, y, longitud):
    if longitud > 0:
        for i in range(longitud):
            if x < 800 and y + 1 > 50:
                ventana_principal.set_at((x , y + i), line_color)

def dibujar_circulo(x, y, radio):
    for i in range(-radio, radio + 1):
        for j in range(-radio, radio + 1):
            if x + i >= 0 and x + i < 800 and y + j >= 0 and y + j < 600:
                if i**2 + j**2 <= radio**2:
                    ventana_principal.set_at((x + i, y + j), line_color)

def dibujar_circunferencia(x, y, radio):
    for i in range(360):
        angulo_rad = i * (math.pi / 180)  # Convertir el ángulo a radianes
        punto_x = int(x + radio * math.cos(angulo_rad))
        punto_y = int(y + radio * math.sin(angulo_rad))
        ventana_principal.set_at((punto_x, punto_y), line_color)

def dibujar_cuadrado_vacio(x, y, longitud):
    for i in range(longitud):
        ventana_principal.set_at((x + i, y), line_color)
        ventana_principal.set_at((x + i, y + longitud - 1),  line_color)
        ventana_principal.set_at((x, y + i), line_color)
        ventana_principal.set_at((x + longitud - 1, y + i), line_color)

def dibujar_cuadrado_lleno(x, y, longitud):
    for i in range(longitud):
        for j in range(longitud):
            ventana_principal.set_at((x + i, y + j), line_color)
        
def dibujar_rectangulo_lleno(x, y, ancho, alto):
    for i in range(ancho):
        for j in range(alto):
            ventana_principal.set_at((x + i, y + j), line_color)

def dibujar_rectangulo_vacio(x, y, ancho, alto):
    for i in range(ancho):
        ventana_principal.set_at((x + i, y), line_color)
        ventana_principal.set_at((x + i, y + alto - 1), line_color)
    for j in range(alto):
        ventana_principal.set_at((x, y + j), line_color)
        ventana_principal.set_at((x + ancho - 1, y + j), line_color)

def dibujar_triangulo_equilatero(x, y, lado):
    altura = int(lado * (3 ** 0.5) / 2)
    for i in range(altura + 1):
        for j in range(i + 1):
            ventana_principal.set_at((x + lado // 2 - i + j, y + i), line_color)
            ventana_principal.set_at((x + lado // 2 + i - j, y + i), line_color)

def dibujar_triangulo_escaleno(x, y, base, altura):
    for i in range(altura + 1):
        for j in range(int(base * (1 - i / altura))):
            ventana_principal.set_at((x + j, y + i), line_color)

def dibujar_triangulo_isosceles(x, y, base, altura):
    for i in range(altura + 1):
        for j in range(base - i):
            ventana_principal.set_at((x + j, y + i), line_color)
            ventana_principal.set_at((x + j, y + i), line_color)
            ventana_principal.set_at((x + base // 2 - i // 2 + j, y + i), line_color)

def cambiar_color(color):
    if color == "blanco":
        line_color = (255, 255, 255)
    elif color == "negro":
        line_color = (0, 0, 0)
    elif color == "rojo":
        line_color = (255, 0, 0)
    elif color == "azul":
        line_color = (0, 0, 255)
    elif color == "verde":
        line_color = (0, 255, 0)
    elif color == "morado":
        line_color = (102, 0, 161)
    elif color == "rosa":
        line_color = (255, 0, 255)
    elif color == "amarillo":
        line_color = (255, 255, 0)
    elif color == "naranja":
        line_color = (255, 128, 0)
    elif color == "gris":
        line_color = (90, 90, 90)
    elif color == "cafe":
        line_color = (128, 54, 0)

    return line_color

# Ciclo principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                # Procesar el comando ingresado
                comando = input_text.strip().split()

                if comando[0] == "exit":
                    pygame.quit()
                    sys.exit()
#Revisar
                elif comando[0] == "fondo":
                    if len(comando) == 2:
                        try:
                            color_fondo = str(comando[1])
                            fondo(color_fondo)
                        except:
                            print("Error: Eses color no existe")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: fondo (color)")

                elif comando[0] == "linea":
                    if len(comando) == 5:
                        try:
                            x1 = int(comando[1])
                            y1 = int(comando[2])
                            x2 = int(comando[3])
                            y2 = int(comando[4])
                            dibujar_linea(x1, y1, x2, y2)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: linea (posicion X1, posicion Y1, posicion X2, posicion Y2)")
#Revisar
                elif comando[0] == "size":
                    if len(comando) == 4:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            size = int(comando[3])
                            size_pixel(x, y, size)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: size (posicion X, posicion Y, size)")

                elif comando[0] == "linea+h":
                    if len(comando) == 4:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            longitud = int(comando[3])
                            dibujar_linea_horizontal_positiva(x, y, longitud)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: linea+h (posicion X, posicion Y, longitud)")

                elif comando[0] == "linea-h":
                    if len(comando) == 4:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            longitud = int(comando[3])
                            dibujar_linea_horizontal_negativa(x, y, longitud)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: linea-h (posicion X, posicion Y, longitud)")

                elif comando[0] == "linea+v":
                    if len(comando) == 4:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            longitud = int(comando[3])
                            dibujar_linea_vertical_positiva(x, y, longitud)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: linea+v (posicion X, posicion Y, longitud)")

                elif comando[0] == "linea-v":
                    if len(comando) == 4:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            longitud = int(comando[3])
                            dibujar_linea_vertical_negativa(x, y, longitud)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: linea-v (posicion X, posicion Y, longitud)")       
                
                elif comando[0] == "circulo":
                    if len(comando) == 4:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            radio = int(comando[3])
                            dibujar_circulo(x, y, radio)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: circunferencia (posicion X, posicion Y, radio)")

                elif comando[0] == "circunferencia":
                    if len(comando) == 4:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            radio = int(comando[3])
                            dibujar_circunferencia(x, y, radio)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: circulo (posicion X, posicion Y, radio)")
       
                elif comando[0] == "cuadrado":
                    if comando[1] == "lleno":
                        if len(comando) == 5:
                            try:
                                x = int(comando[2])
                                y = int(comando[3])
                                longitud = int(comando[4])
                                dibujar_cuadrado_lleno(x, y, longitud)
                            except ValueError:
                                print("Error: Los valores deben ser enteros.")
                        else:
                            print("Error: Sintaxis incorrecta. Uso correcto: cuadrado lleno (posicion X, posicion Y, longitud)")
                    elif comando [1] == "vacio":
                        if len(comando) == 5:
                            try:
                                x = int(comando[2])
                                y = int(comando[3])
                                longitud = int(comando[4])
                                dibujar_cuadrado_vacio(x, y, longitud)
                            except ValueError:
                                print("Error: Los valores deben ser enteros.")
                        else:
                            print("Error: Sintaxis incorrecta. Uso correcto: cuadrado vacio (posicion X, posicion Y, longitud)")
                    else:
                        print("Error: Utiliza cuadrado (vacio o lleno)")

                elif comando[0] == "rectanguloL":
                    if len(comando) == 5:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            ancho = int(comando[3])
                            alto = int(comando[4])
                            dibujar_rectangulo_lleno(x, y, ancho, alto)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: rectanguloL (posicion X, posicion Y, ancho, alto)")

                elif comando[0] == "rectanguloV":
                    if len(comando) == 5:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            ancho = int(comando[3])
                            alto = int(comando[4])
                            dibujar_rectangulo_vacio(x, y, ancho, alto)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: rectanguloV (posicion X, posicion Y, ancho, alto)")

                elif comando[0] == "equilatero":
                    if len(comando) == 4:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            lado = int(comando[3])
                            dibujar_triangulo_equilatero(x, y, lado)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: equilatero (posicion X, positivo Y, lado)")

                elif comando[0] == "escaleno":
                    if len(comando) == 5:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            base = int(comando[3])
                            altura = int(comando[4])
                            dibujar_triangulo_escaleno(x, y, base, altura)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: escaleno (posicion X, positivo Y, base, altura)")

                elif comando[0] == "isosceles":
                    if len(comando) == 5:
                        try:
                            x = int(comando[1])
                            y = int(comando[2])
                            base = int(comando[3])
                            altura = int(comando[4])
                            dibujar_triangulo_isosceles(x, y, base, altura)
                        except ValueError:
                            print("Error: Los valores deben ser enteros.")
                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: isosceles (posicion X, positivo Y, base, altura)")
    #Reviasar
                elif comando[0] == "color":
                    if len(comando) == 2:
                        try:
                            color = comando[1]  # Evalúa el nombre del color para obtener su valor
                            line_color = cambiar_color(color)
                            print("El color actual es: ",color)
                            print(line_color)
                        except NameError:
                            print("Error: El color no existe.")

                    else:
                        print("Error: Sintaxis incorrecta. Uso correcto: color (nombre_color)")

                # Limpiar la entrada de texto
                input_text = ""

                # Actualizar la ventana principal después de cada comando
                pygame.display.update()
            else:
                # Agregar caracteres ingresados a la entrada de texto
                if evento.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += evento.unicode

    # Dibujar la entrada de texto
    pygame.draw.rect(ventana_principal, (200, 200, 200), input_rect)
    fuente = pygame.font.Font(None, 24)
    texto_superficie = fuente.render(input_text, True, (0, 0, 0))
    ventana_principal.blit(texto_superficie, (input_rect.x + 5, input_rect.y + 5))
    pygame.display.flip()