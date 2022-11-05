import pygame, sys
from home import Home
from game import Game

pygame.init()
WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tim14255")

clock = pygame.time.Clock()

home = Home(screen, WIDTH, HEIGHT)
game = Game(screen, WIDTH , HEIGHT)


home_active = True
game_active = False

music = pygame.mixer.Sound('game/assets/Audio/bg_music.wav')
music.set_volume(0.03)
music.play(loops = -1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            home_active = False
            game_active = True


    if home_active == True :
        home.run()

    if game_active == True :
        game.run()

    pygame.display.flip()
    clock.tick(60)