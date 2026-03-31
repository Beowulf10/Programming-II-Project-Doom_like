import math, pygame

class Ray:
    def __init__(self, angle, player):
        self.rayAngle = angle
        self.player = player
    
    def cast(self):
        pass

    def render(self, screen):

        pygame.draw.line(screen, (255, 0, 0), (self.player.x, self.player.y), (self.player.x + math.cos(self.rayAngle) * 
        50, self.player.y + math.sin(self.rayAngle) * 50))
