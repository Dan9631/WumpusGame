import pygame
import os

from models.Jugador import Jugador
from models.Wumpus import Wumpus
from models.Tesoro import Tesoro
from models.Pozo import Pozo
from models.Hedor import Hedor
from models.Brisa import Brisa

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
jugador =Jugador(absolute_path)
wumpus = Wumpus(absolute_path)
tesoro = Tesoro(absolute_path)
pozo = Pozo(absolute_path, wumpus.rect, tesoro.rect)
sprite_player = pygame.sprite.Group()
sprite_enemys = pygame.sprite.Group()

sprite_player.add(jugador)

sprite_enemys.add(tesoro)

sprite_enemys.add(wumpus)
sprite_enemys.add(pozo)


# Cargar la imagen de inicio
start_image = pygame.image.load('img/START2.jpg')
start_image = pygame.transform.scale(start_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
image_tablero = pygame.image.load('img/fondotablero.jpg')
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

def draw_camino():
        # Dibujar los bloques visitados
        for i in range(4):
            for j in range(5):
                if jugador.visited[i][j]:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(j*120, i*70, 120, 90))

# Función para dibujar imágenes de hedor alrededor del Wumpus
def generate_hedor():
    sprite_enemys.add(Hedor(absolute_path,wumpus.rect.x, wumpus.rect.y - STEP_Y + 15)) # Arriba del Wumpus
    sprite_enemys.add(Hedor(absolute_path,wumpus.rect.x, wumpus.rect.y + STEP_Y + 15))  # Abajo del Wumpus
    sprite_enemys.add(Hedor(absolute_path,wumpus.rect.x - STEP_X + 5, wumpus.rect.y + 20))  # Izquierda del Wumpus
    sprite_enemys.add(Hedor(absolute_path,wumpus.rect.x + STEP_X + 5, wumpus.rect.y + 20))  # Derecha del Wumpus
    
# Funcion que identifica si el jugador puede ver el elemento o aun no ha pasado por esa casilla
def draw_enemys():
    for enemy in sprite_enemys:
        cord_x=enemy.rect.x // 120
        if isinstance(enemy,Pozo):
            cord_y=(enemy.rect.y // 70)
        else:
            cord_y=(enemy.rect.y // 75)
        if jugador.visited[cord_y][cord_x]:
            screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
       # print(f'{enemy.imagePath} x={cord_x} y={cord_y} enemy=x:{enemy.rect.x} y:{enemy.rect.y}')

# Función para dibujar imágenes de brisa alrededor del Pozo
def generate_brisa():
    sprite_enemys.add(Brisa(absolute_path,pozo.rect.x, pozo.rect.y - STEP_Y + 10))  # Arriba del Pozo
    sprite_enemys.add(Brisa(absolute_path,pozo.rect.x, pozo.rect.y + STEP_Y + 10))  # Abajo del Pozo
    sprite_enemys.add(Brisa(absolute_path,pozo.rect.x - STEP_X + 5, pozo.rect.y + 10))  # Izquierda del Pozo
    sprite_enemys.add(Brisa(absolute_path,pozo.rect.x + STEP_X + 5, pozo.rect.y + 10))  # Derecha del Pozo


# Función para el bucle principal del juego
def game_screen():
    generate_hedor()
    generate_brisa()

    draw_enemys()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        sprite_player.update()  # Actualizar las posiciones de los sprites

        screen.fill((255, 242, 255))  # Llenar la pantalla de negro
      #  screen.blit(image_tablero, (0, 0))
        draw_camino()
        draw_enemys()
        sprite_player.draw(screen)
        # sprite_enemys.draw(screen)
        
        
        
        clock.tick(8)
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