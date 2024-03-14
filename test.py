import pygame
import random

# Inicializa Pygame
pygame.init()

# Define las dimensiones de los segmentos y la figura
ANCHO_SEGMENTO = 150
ALTO_SEGMENTO = 120
ANCHO_FIGURA = 70
ALTO_FIGURA = 70

# Crea una ventana de 150x120
ventana = pygame.display.set_mode((600, 600))

# Carga la imagen (asegúrate de tener una imagen válida en este path)
imagen = pygame.image.load('img/Player.png').convert_alpha()
imagen = pygame.transform.scale(imagen,(70,70))
# Calcula las coordenadas del centro de cada segmento
centro_x = (ANCHO_SEGMENTO - ANCHO_FIGURA) // 2
centro_y = (ALTO_SEGMENTO - ALTO_FIGURA) // 2

# Genera una coordenada x e y aleatoria para el segmento
segmento_x = random.randint(1, 2) * ANCHO_SEGMENTO
segmento_y = random.randint(1, 2) * ALTO_SEGMENTO

# Calcula las coordenadas finales sumando las coordenadas del centro de la figura a las del segmento
final_x = segmento_x + centro_x
final_y = segmento_y + centro_y

# Dibuja la imagen en las coordenadas finales
ventana.blit(imagen, (final_x, final_y))

# Actualiza la pantalla
pygame.display.flip()

# Mantén la ventana abierta hasta que se cierre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
