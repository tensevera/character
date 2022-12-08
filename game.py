import time
import pygame
import random
import math

pygame.init()


display_size = 500
screen = pygame.display.set_mode((display_size, display_size))
#vytvor panacka
character_size = 20
character = pygame.Surface((character_size,character_size))
character.fill((255,255,255))
character_length = 1
character_body = []
#souradnice
x = 0
y = 0
#smer pohybu
dx = 0
dy = 0
#rychlost pohybu
step = 2

#vytvor pochutinu
snack = pygame.Surface((10,10))
snack.fill((255,0,0))
#souradnice pochutiny
snack_x = random.randint(0,10)
snack_y = random.randint(0,display_size)
#promenne pochutiny
snack_time = 5
snack_spawn = time.time()
#pochutina offset
snack_offset = 20

#pomocne promenne
running = True
points = 0

#font
font_size = 15
score_font = pygame.font.SysFont("comicsansms", font_size)
timer_font = pygame.font.SysFont("impact", font_size)

clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # pohyb
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                dx = -1
                dy = 0
            elif event.key == pygame.K_s:
               dy = 1
               dx = 0
            elif event.key == pygame.K_d:
                dx = 1
                dy = 0
            elif event.key == pygame.K_w:
                dy = -1
                dx = 0
    #posun
    x += step*dx
    y += step*dy
    #krajni meze
    if (x < 0):
        x = display_size
    if (y < 0):
        y = display_size
    if (x > display_size):
        x = 0
    if (y > display_size):
        y = 0
    #vykresli
    screen.fill((0,0,0))

    screen.blit(snack, (snack_x,snack_y))
    if (abs(snack_x-x) < character_size and abs(snack_y-y) < character_size):
        snack_x = random.randint(snack_offset,display_size-snack_offset)
        snack_y = random.randint(snack_offset,display_size-snack_offset)
        snack_spawn = time.time()
        character_length += 1
        points += 1

    if(time.time() - snack_spawn > snack_time):
        points = 0
        snack_x = random.randint(snack_offset,display_size-snack_offset)
        snack_y = random.randint(snack_offset,display_size-snack_offset)
        snack_spawn = time.time()
    score_value = score_font.render("Your score: " + str(points), True, (255,255,255))
    timer_value = timer_font.render("Timer: " + str(round(snack_time -time.time()+snack_spawn)), True, (255,255,255))
    screen.blit(score_value, (0,0))
    screen.blit(timer_value, (0,font_size))

    screen.blit(character, (x,y))


    pygame.display.update()
    #FPS
    clock.tick(60)

pygame.quit()