import pygame
import random

# Definir los tamaños de los pasos
STEP_X = 120
STEP_Y = 72

class Tesoro(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.has_collided = False
        self.image = pygame.image.load(f'{path}/img/Tesoro.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, 4) * STEP_X + 35 # Genera una coordenada x aleatoria
        self.rect.y = random.randint(0, 2) * STEP_Y + 20 # Genera una coordenada y aleatoria

