import pygame
import random
""" from models.Wumpus import Wumpus
from models.Tesoro import Tesoro """

# Tamaño de los pasos del jugador
STEP_X = 120
STEP_Y = 72

class Pozo(pygame.sprite.Sprite):
    def __init__(self, path, wumpus_rect, tesoro_rect):
        super().__init__()
        self.image = pygame.image.load(f'{path}/img/Pozo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.reset_position(wumpus_rect, tesoro_rect)

    def reset_position(self, wumpus_rect, tesoro_rect):
        while True:
            self.rect.x = random.randint(0, 4) * STEP_X + 35
            self.rect.y = random.randint(0, 2) * STEP_Y + 30
            if not self.rect.colliderect(wumpus_rect) and not self.rect.colliderect(tesoro_rect):
                break
