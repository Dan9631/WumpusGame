import pygame
import os
import pygame.freetype
import random

#Carga de modelos de objetos
from models.Jugador import Jugador
from models.Wumpus import Wumpus
from models.Tesoro import Tesoro
from models.Pozo import Pozo
from models.Hedor import Hedor
from models.Brisa import Brisa
from models.Disparo import Disparo

# Definir los tamaños de los pasos
STEP_X = 120
STEP_Y = 72

# Definir las dimensiones de la pantalla
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Inicializar Pygame
pygame.init()
clock = pygame.time.Clock()
font1 = pygame.font.Font(None, 36)
pygame.mixer.music.load('sounds/Ambient.mp3')
pygame.mixer.music.play(-1)

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
image_inventario = pygame.image.load('img/inventario.jpg')
image_inventario = pygame.transform.scale(image_inventario,(600,500))

image_Municion = pygame.image.load('img/municionUp.png')
image_Municion = pygame.transform.scale(image_Municion,(35,35))
image_Vidas = pygame.image.load('img/vidas.png')
image_Vidas = pygame.transform.scale(image_Vidas,(35,35))



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

        text = font1.render("Instrucciones: ...", True, (255, 255, 255))
        
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()

#funcion que dibuja vidas
def draw_vidas():
     screen.fill((0, 0, 0))  # Llenar la pantalla de negro
     screen.blit(image_Vidas, (250, 300))
     text_vidas = font1.render(f'{jugador.vidas}', True, (255,255, 255))
     screen.blit(text_vidas, (300, 300))
     pygame.display.update()
     pygame.time.delay(2000)

# Funcion que permite ingresar el nombre del jugador
def get_namePlayer():
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.freetype.Font(None, 32)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        jugador.name = text
                        if jugador.name == '': jugador.name = f"Jugador{random.randint(1, 99999)}"
                        text = ''
                        text_msg =font1.render("¡¡¡¡¡¡LISTO PREPARATE!!!!", True, (255, 0, 0))
                        screen.blit(text_msg, (input_box.x, input_box.y+90))
                        pygame.display.update()

                        pygame.time.delay(2000)
                        draw_vidas()

                        return
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill((30, 30, 30))
        txt_surface, _ = font.render(text, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        text_msg =font1.render("Ingrese su nombre de Jugador,: ", True, (255, 255, 255))
        screen.blit(text_msg, (input_box.x, input_box.y-30))

        text_msg =font1.render("Presione Enter para continuar", True, (255, 255, 255))
        screen.blit(text_msg, (input_box.x, input_box.y+60))

        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)

def draw_camino():
        # Dibujar los bloques visitados
        for i in range(4):
            for j in range(5):
                if jugador.visited[i][j]:
                    pygame.draw.rect(screen, (222, 163, 55), pygame.Rect(j*120, i*70, 120, 90))

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
        try:    
            if jugador.visited[cord_y][cord_x]:
                screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
                enemy.has_collided = True
            else:
                enemy.has_collided = False
        except:
            pass
       # print(f'{enemy.imagePath} x={cord_x} y={cord_y} enemy=x:{enemy.rect.x} y:{enemy.rect.y}')

# Función para dibujar imágenes de brisa alrededor del Pozo
def generate_brisa():
    sprite_enemys.add(Brisa(absolute_path,pozo.rect.x, pozo.rect.y - STEP_Y + 10))  # Arriba del Pozo
    sprite_enemys.add(Brisa(absolute_path,pozo.rect.x, pozo.rect.y + STEP_Y + 20))  # Abajo del Pozo
    sprite_enemys.add(Brisa(absolute_path,pozo.rect.x - STEP_X + 5, pozo.rect.y + 10))  # Izquierda del Pozo
    sprite_enemys.add(Brisa(absolute_path,pozo.rect.x + STEP_X + 5, pozo.rect.y + 10))  # Derecha del Pozo

def draw_msg(text,color=(255, 255, 255)):
    screen.fill((0, 0, 0))  # Llenar la pantalla de negro
    text_msg =font1.render(text, True, color)
    screen.blit(text_msg, (30,300))
    pygame.display.update()
    pygame.time.delay(2000)

# Funcion para identificar si el jugador ha colisionado con el enemigo o el tesoro
def check_collision():
    for enemy in sprite_enemys:
        if pygame.sprite.collide_rect(jugador, enemy):
            if isinstance(enemy, Wumpus) and not enemy.has_collided:
                draw_msg("¡¡¡¡¡¡Has sido devorado por el \n Wumpus!!!!",(255, 0, 0))
                jugador.vidas=jugador.vidas - 1
                draw_vidas()

            if isinstance(enemy, Tesoro) and not enemy.has_collided:
                draw_msg("¡¡¡¡¡¡Has encontrado el \n tesoro!!!!",(225, 180, 10))

            if isinstance(enemy, Pozo) and not enemy.has_collided:
                draw_msg("¡¡¡¡¡¡Has caido en un pozo!!!!",(0, 0, 255))
                jugador.vidas=jugador.vidas - 1
                draw_vidas()

            if isinstance(enemy, Hedor) and not enemy.has_collided:
                draw_msg(".....Estas cerca del Wumpus..... un hedor inusual",(74, 222, 55))

            if isinstance(enemy, Brisa) and not enemy.has_collided:
                draw_msg(".....¿una brisa de viento?...",(55, 186, 222))

#Identificar si se presiono la tecla de disparo
def check_fire(event):
            if event.type == pygame.KEYDOWN and jugador.municion>0:  # Se presionó una tecla
                if event.key == pygame.K_UP:  # La tecla presionada fue la flecha hacia arriba
                    sprite_player.add(Disparo(f'img/MunicionUp.png',jugador.rect.x, jugador.rect.y,0,-5))
                    jugador.municion = jugador.municion - 1
                elif event.key == pygame.K_DOWN:  # La tecla presionada fue la flecha hacia abajo
                    sprite_player.add(Disparo(f'img/MunicionDown.png',jugador.rect.x, jugador.rect.y,0,5))
                    jugador.municion = jugador.municion - 1
                elif event.key == pygame.K_LEFT:  # La tecla presionada fue la flecha hacia la izquierda
                    sprite_player.add(Disparo(f'img/MunicionLeft.png',jugador.rect.x, jugador.rect.y,-5,0))
                    jugador.municion = jugador.municion - 1
                elif event.key == pygame.K_RIGHT:  # La tecla presionada fue la flecha hacia la derecha
                    sprite_player.add(Disparo(f'img/MunicionRight.png',jugador.rect.x, jugador.rect.y,5,0))
                    jugador.municion = jugador.municion - 1
                


#valida si el disparo collisiono con el enemigo
def check_collisionFire():
    for enemy in sprite_enemys:
        if isinstance(enemy,Hedor):
            sprite_enemys.remove(enemy)

def draw_inventario():
    text_nombre = font1.render(f'{jugador.name}', True, (0, 0, 0))
    screen.blit(text_nombre, (50, 405))

    screen.blit(image_Municion, (40, 505))
    text_municion = font1.render(f'{jugador.municion}', True, (0, 0, 0))
    screen.blit(text_municion, (150, 515))

    screen.blit(image_Vidas, (40, 540))
    text_vidas = font1.render(f'{jugador.vidas}', True, (0, 0, 0))
    screen.blit(text_vidas, (150, 550))


# Función para el bucle principal del juego
def game_screen():
    generate_hedor()
    generate_brisa()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                check_fire(event)

        sprite_player.update()  # Actualizar las posiciones de los sprites

        for disparo in sprite_player:
            if isinstance(disparo, Disparo):
                if disparo.rect.colliderect(wumpus.rect):
                    sprite_player.remove(disparo)
                    sprite_enemys.remove(wumpus)
                    check_collisionFire()
                    draw_msg("¡¡¡¡¡¡Has matado al Wumpus!!!!",(255, 0, 0))


    # valida la colision con los enemigos
        check_collision()
        screen.fill((0, 0, 0))  # Llenar la pantalla de negro
        
        screen.blit(image_inventario, (0, 300))
      #  screen.blit(image_tablero, (0, 0))
        draw_camino()
        sprite_player.draw(screen)
        draw_enemys()
        draw_inventario()
        # sprite_enemys.draw(screen)
        
        
        
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


# Mostrar la pantalla de inicio
start_screen()

# Mostrar las instrucciones
instructions_screen()

#Solicita nombre jugador
get_namePlayer()

# Reiniciar la posición del Wumpus antes de iniciar el juego
wumpus.reset_position()

# Iniciar el juego
game_screen()