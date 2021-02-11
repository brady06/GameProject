import pygame
import sys
sys.path.append('')
sys.path.append('../')
pygame.init()




pygame.display.set_caption("NSI project game")
screen = pygame.display.set_mode((1080,720))
background = pygame.image.load('assets\textures\background\background_WIP.png')


running = True
while running:

    screen.blit(background, (0,0))


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running=False
            pygame.quit()
