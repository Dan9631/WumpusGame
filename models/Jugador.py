import pygame
import os

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(__file__)  # Obtener el directorio actual del script
        image_path = os.path.join(current_dir, '..', 'img', 'Player.png')  # Construir la ruta de la imagen
        self.image = pygame.image.load(image_path).convert_alpha()  # Cargar imagen con transparencia
        self.image = pygame.transform.scale(self.image,(70,70))  # Escalar la imagen
        self.rect = self.image.get_rect()  # Obtiene el rectángulo del sprite
        self.rect.y = 225
        self.rect.x = 35

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 72 
        if keys[pygame.K_s]:
            self.rect.y += 72 
        if keys[pygame.K_a]:
            self.rect.x -= 120 
        if keys[pygame.K_d]:
            self.rect.x += 120 
