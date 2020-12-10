#importation des libs
"""
#################################
autor : Thomas LOUDOUX,
main scripte of game
#################################
"""
import sys
import pygame
import Game.gameClass.games as g
import Game.gameClass.screen as s
#super class entity de la super class Sprite de pygame

#initialisation du jeu

game = g.Game()
screen = s.GameScreen()
CONTINUE = True
#boucle de rendering
while CONTINUE:

    #boucle des event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CONTINUE = False
            pygame.quit()
            sys.exit()
    screen.blit(g.player.image, g.player.rect)
