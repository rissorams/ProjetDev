import math
from lib.constants import SCREEN_CONFIG
from lib.lib import Lib
import pygame

# from models.player import Player

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.id = player.id
        self.player = player
        self.angle = player.angle
        self.velocity = 5
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.centerx
        self.rect.y = player.rect.centery
    
    def remove(self):
        self.player.all_projectiles.remove(self)
          
    def move(self) : 
        angle_in_radians = math.radians(self.angle)
        
        # Formule trigonométrique
        dy = math.sin(angle_in_radians) * self.velocity
        dx = math.cos(angle_in_radians) * self.velocity
        self.rect.x += int(dx)
        self.rect.y -= int(dy)
        
        if self.is_not_in_screen() : 
            self.kill()
            
        for player in Lib.check_colliders(self, self.player.game.player2_group) : 
            print("COLLISIONS AVEC LE JOUEUR ADVERSE")
            self.remove()
            if player.damage(self.player.power_shoot) : 
                return True
            
        return False
        
        
    
    def is_not_in_screen(self) : 
        return self.rect.x < 0 or self.rect.x > SCREEN_CONFIG['WIDTH'] or self.rect.y < 0 or self.rect.y > SCREEN_CONFIG['HEIGHT'] 