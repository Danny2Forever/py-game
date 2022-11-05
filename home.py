import pygame

class Home():
    def __init__(self, screen, WIDHT , HEIGHT):
        self.screen = screen
        self.WIDHT = WIDHT
        self.HEIGHT = HEIGHT
        self.bg_image = pygame.image.load("game/assets/Background/1.png").convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDHT , HEIGHT))

        #font
        self.font = pygame.font.Font("game/assets/Font/mago3.ttf", 100)

    def run(self):
        self.screen.blit(self.bg_image, (0,0))
        title_surf = self.font.render('Press Spacebar', False, 'white')
        title_rect = title_surf.get_rect(center=(self.WIDHT/2, self.HEIGHT / 2))
        self.screen.blit(title_surf, title_rect)