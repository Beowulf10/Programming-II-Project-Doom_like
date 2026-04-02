import pygame
from settings import *
from map import Map
from player import Player
from raycaster import Raycaster

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#screen_rect = screen.get_rect()


map = Map()
player = Player()

clock = pygame.time.Clock()
raycaster = Raycaster(player, map)

while True:
    clock.tick(60) #60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.update()
    raycaster.castAllRays()

    screen.fill((0, 0, 0))

    #bg_image = pygame.image.load("background_image.png")
    #bg_rect = bg_image.get_rect(center=screen_rect.center)

    #screen.blit(bg_image, (0, 0))

    #map.render(screen)
    #player.render(screen)      #Both comments have the original grid map

    raycaster.render(screen)


    pygame.display.update()