from Game.gameClass.entityClass import player


class Game():
    def __init__(self):

        #générer le joueur
        self.player = player.Player()