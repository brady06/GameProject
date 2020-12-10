import pygame

#Super class entity de la super class Sprite de pygame

class Entity(pygame.sprite.Sprite):
    #initialisation de la fonction d'initialisation de l'objet entity
    def __init__(self):
        #initialisation de la super class a l'initialisation de l'objet entity
        super().__init__()
        
        #initialisation des variable de base de l'objet 
        self.max_Heal = 100
        self.Heal = 100
        self.attack = 10
        self.lvl=1
        self.velocity = 10
        self.image = pygame.image.load("assets/entity/entity_WIP.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 800
    
    ##système de mouvement 

    #pour aller vers la droite 
    def moveRight(self, screen):
        #si la position X de l'entité n'est pas égale a la taille de l'écran, l'implémenté de velocity
        if self.rect.x != screen.getHeight:
            self.rect.x += self.velocity

    #pour aller vers la gauche 
    def moveLeft(self):
        #si la position X de l'entité n'est pas égale 0, la décrémenté de velocity
        if self.rect.x != 0:
            self.rect.x -= self.velocity

    #pour aller vers le haut
    def moveUp(self):
        #si la position Y de l'entité n'est pas égale a 0, l'implémenté de velocity
        if self.rect.y != 0:
            self.rect.y -= self.velocity

    #pour aller vers le bas
    def moveDown(self, screen):
        #si la position Y de l'entité n'est pas égale a la taille de l'écran, l'implémenté de velocity
        if self.rect.y != screen.getWidth:
            self.rect.y += self.velocity
