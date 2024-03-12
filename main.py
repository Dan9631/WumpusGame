import pygame
import os
from models.Jugador import Jugador


# Definir las dimensiones de la pantalla
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Inicializar Pygame
pygame.init()
clock = pygame.time.Clock()

# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


absolute_path=os.getcwd().replace("\\", "/")


# Cargar ObjetosInteractuar
jugador = Jugador(absolute_path)
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(jugador)

# Cargar la imagen de inicio
start_image = pygame.image.load('img/START2.jpg')
start_image = pygame.transform.scale(start_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
image_tablero = pygame.image.load('img/tablero1.png')
image_tablero = pygame.transform.scale(image_tablero,(600,300))


# Función para mostrar la pantalla de inicio
def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
        screen.blit(start_image, (0, 0))
        pygame.display.update()



# Función para mostrar las instrucciones
def instructions_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
        screen.fill((0, 0, 0))  # Llenar la pantalla de negro
        font = pygame.font.Font(None, 36)
        text = font.render("Instrucciones: ...", True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()

# Función para el bucle principal del juego
def game_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        todos_los_sprites.update()

        # Aquí va la lógica de tu juego...
        screen.fill((0, 0, 0))  # Llenar la pantalla de negro
        screen.blit(image_tablero,(0,0))

        todos_los_sprites.draw(screen)
        clock.tick(9)
        pygame.display.flip()

    pygame.quit()

# Mostrar la pantalla de inicio
start_screen()

# Mostrar las instrucciones
instructions_screen()

# Iniciar el juego
game_screen()