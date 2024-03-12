import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        # Carga la imagen del sprite (debe estar en el mismo directorio que este script)
        self.image = pygame.image.load(f'{path}/img/Personaje1.png').convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect()  # Obtiene el rectángulo del sprite
        self.rect.y = 225
        self.rect.x =  35

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
        