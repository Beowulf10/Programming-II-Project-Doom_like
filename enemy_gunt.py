import pygame
import settings
import math
from ray import Ray
class Gunt():
    def __init__(self):
        self.attack_dist = Ray(3,6,7)
        self.speed = 0.33
        self.size = 10
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        self.alive = True
        self.pain = False
    
    