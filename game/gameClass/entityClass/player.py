import pygame
import Game.gameClass.entityClass.entity as e


#class de l'objet Player
class Player(e.Entity):
    #initialisation de l'objet
    def __init__(self):
        #initialisation de la super class entity
        super().__init__()

        #modification des variables
        super().max_Heal = 150
        super().Heal = 150
        self.image = pygame.image.load("fr.gameproject/assets/entity/player/player_sprite_none.png")
        #initialisation des variable de l'objet Player
        self.xp=0.0
        self.xp_to_next_lvl = 100.0
    