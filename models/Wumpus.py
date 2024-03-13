import pygame
import random

# Tamaño de los pasos del jugador
STEP_X = 120
STEP_Y = 72
class Wumpus(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        # Carga la imagen del sprite (debe estar en el mismo directorio que este script)
        self.image = pygame.image.load(f'{path}/img/Wumpus.png').convert_alpha()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect() # Obtiene el rectángulo del sprite
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(1, 2) * STEP_X + 35 # Genera una coordenada x aleatoria
        self.rect.y = random.randint(1, 2) * STEP_Y + 8   # Genera una coordenada y aleatoria
