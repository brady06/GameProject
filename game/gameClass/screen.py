import pygame

#creation de l'objet gameScreen
class GameClass():
    #Initialisation de l'objet gameScreen

    def __init__(self):
        #La taille de l'écran 
        self.width = 720
        self.height = 1080
        self.size = (self.height,self.width) #La taille est de type tuple 

        #initialisation de l'écran 
        self.mode = pygame.display.set_mode(self.size)

        #configuration de l'écran 
        self.caption = pygame.display.set_caption("NSI Project")
        self.link = "fr.gameproject/assets/background_WIP.png"
        self.image = pygame.image.load(self.link)


    def update(self):
        self.blit(self.image,(0,0))

    #méthode pour la taille
    def get_size(self):
        return self.size
    def set_size(self, new_size):
        assert new_size.isinstance(tuple)
        self.size = new_size
        self.update()

    #méthode pour la hauteur de la fenêtre
    def get_height(self):
        return self.height
    def set_height(self, nHeight):
        self.height=nHeight
        self.set_size((nHeight, self.width))
    
    #méthode pour la largeur de la genêtre 
    def get_width(self):
        return self.width
    def set_width(self, nWidth):
        self.width = nWidth
        self.set_size((self.height, nWidth))
    def blit(self, subject, rect):
        self.mode.blit(subject, rect)
        