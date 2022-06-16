from typing import Any
from lib.constants import SCREEN_CONFIG
from player import Player
import pygame


class Game(object):
    def __init__(self, *args):
        # Initialising of the basics pygame parametters
        pygame.init()
        # title
        pygame.display.set_caption("Battle Shoot")
        # size
        self.screen = pygame.display.set_mode((SCREEN_CONFIG['WIDTH'], SCREEN_CONFIG['HEIGHT']))
        self.player = Player(1, self)
        self.player2 = Player(2, self)
        self.player1_group = pygame.sprite.Group(self.player)
        self.player2_group = pygame.sprite.Group(self.player2)

    
    def start(self) :
        self.running()
        
    
    def running(self) :
        # SI TU VEUX JOUER LE JOUEUR 2 ECHANGE JUSTE LE NOM DES VARIABLES
        game = True
        bg = pygame.image.load("assets/bg.jpg")
        game_over = pygame.image.load("assets/Game_Over_logo.png")
        running = True
        # Closing window
        while running:
            if game : 
                # Render
                self.screen.blit(bg, (0, 0))
                self.screen.blit(self.player.image, self.player.rect)
                self.screen.blit(self.player2.image, self.player2.rect)
                self.player.all_projectiles.draw(self.screen)
                
                
                for projectile in self.player.all_projectiles :
                    if projectile.move() : 
                        game = False
                    
                # self.check_projectiles_colliders()
                

                self.player.update_pos(self.screen)
                self.player.health_bar(self.screen)
                self.player2.update_pos(self.screen)
                self.player2.health_bar(self.screen)
                
                # Todo : change the event with the controllers (rasberry)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        self.player.pressed[event.key] = True
            
                        
                        if event.key == pygame.K_SPACE : 
                            self.player.launch_projectile()
                        
                    elif event.type == pygame.KEYUP:
                        self.player.pressed[event.key] = False
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit() 
                        
            else : 
                self.screen.blit(game_over, (400, 100))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit() 
            # clock.tick(30)  # Afficher à 30 fps le jeu
            pygame.display.flip()    
    
        
    
        