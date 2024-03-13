import pygame
import os

from models.Jugador import Jugador
from models.Wumpus import Wumpus
from models.Tesoro import Tesoro
from models.Pozo import Pozo

# Definir los tamaños de los pasos
STEP_X = 120
STEP_Y = 72

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
jugador =Jugador()
wumpus = Wumpus(absolute_path)
tesoro = Tesoro(absolute_path)
pozo = Pozo(absolute_path, wumpus.rect, tesoro.rect)
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(jugador)
todos_los_sprites.add(wumpus)
todos_los_sprites.add(tesoro)
todos_los_sprites.add(pozo)


# Cargar la imagen de inicio
start_image = pygame.image.load('img/START2.jpg')
start_image = pygame.transform.scale(start_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
image_tablero = pygame.image.load('img/fondotablero.jpg')
image_tablero = pygame.transform.scale(image_tablero,(600,300))

# Cargar la imagen de hedor
hedor_image = pygame.image.load('img/Hedor.png').convert_alpha()
hedor_image = pygame.transform.scale(hedor_image, (40, 40))  # Ajustar al tamaño 

# Cargar la imagen de Brisa
brisa_image = pygame.image.load('img/Brisa.png').convert_alpha()
brisa_image = pygame.transform.scale(brisa_image, (40, 40))  # Ajustar al tamaño 


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


# Función para dibujar imágenes de hedor alrededor del Wumpus
def draw_hedor():
    screen.blit(hedor_image, (wumpus.rect.x, wumpus.rect.y - STEP_Y + 20))  # Arriba del Wumpus
    screen.blit(hedor_image, (wumpus.rect.x, wumpus.rect.y + STEP_Y + 20))  # Abajo del Wumpus
    screen.blit(hedor_image, (wumpus.rect.x - STEP_X + 5, wumpus.rect.y + 20))  # Izquierda del Wumpus
    screen.blit(hedor_image, (wumpus.rect.x + STEP_X + 5, wumpus.rect.y + 20))  # Derecha del Wumpus
    
# Función para dibujar imágenes de brisa alrededor del Pozo
def draw_brisa():
    screen.blit(brisa_image, (pozo.rect.x, pozo.rect.y - STEP_Y + 10))  # Arriba del Pozo
    screen.blit(brisa_image, (pozo.rect.x, pozo.rect.y + STEP_Y + 10))  # Abajo del Pozo
    screen.blit(brisa_image, (pozo.rect.x - STEP_X + 5, pozo.rect.y + 10))  # Izquierda del Pozo
    screen.blit(brisa_image, (pozo.rect.x + STEP_X + 5, pozo.rect.y + 10))  # Derecha del Pozo


# Función para el bucle principal del juego
def game_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        todos_los_sprites.update()  # Actualizar las posiciones de los sprites




        screen.fill((0, 0, 0))  # Llenar la pantalla de negro
        screen.blit(image_tablero, (0, 0))
        todos_los_sprites.draw(screen)
        draw_hedor()
        draw_brisa()
        clock.tick(9)
        pygame.display.flip()

    pygame.quit()


# Mostrar la pantalla de inicio
start_screen()

# Mostrar las instrucciones
instructions_screen()

# Reiniciar la posición del Wumpus antes de iniciar el juego
wumpus.reset_position()

# Iniciar el juego
game_screen()