#importation des libs
"""
#################################
autor : Thomas LOUDOUX,
main scripte of game
#################################
"""
import sys
import pygame
import gameClass.game
import gameClass.screen
#super class entity de la super class Sprite de pygame

#initialisation du jeu

game = gameClass.game.Game()
screen = gameClass.screen.GameScreen()
CONTINUE = True
#boucle de rendering
while CONTINUE:

    #boucle des event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CONTINUE = False
            pygame.quit()
            sys.exit()
    screen.blit(game.player.image, game.player.rect)
