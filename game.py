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
snack_x = random.randint(0,display_size)
snack_y = random.randint(0,display_size)
#promenne pochutiny
snack_time = 5

#pomocne promenne
running = True
points = 0


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
        elif event.type == pygame.KEYUP:
            dx = 0
            dy = 0
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
    screen.blit(character, (x,y))
    screen.blit(snack, (snack_x,snack_y))
    if (abs(snack_x-x) < character_size and abs(snack_y-y) < character_size):
        snack_x = random.randint(0,display_size)
        snack_y = random.randint(0,display_size)
        points += 1
        print(points)

    pygame.display.update()
    #FPS
    clock.tick(60)

pygame.quit()