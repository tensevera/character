import pygame

pygame.init()

#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((500, 500))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # RED GREEN BLUE
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((0,0,0))
            elif event.key == pygame.K_s:
                screen.fill((255,0,0))
            elif event.key == pygame.K_d:
                screen.fill((0,255,0))
            elif event.key == pygame.K_w:
                screen.fill((0,0,255))
    pygame.display.update()

pygame.quit()