import pygame
from player import Player
from coin import Coin
from enemy import Enemy
from random import randint

class Game():
    def __init__(self, screen, WIDTH , HEIGHT):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.bg_image = pygame.image.load('game/assets/Background/1.png').convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH, HEIGHT))

        #player
        player_sprite = Player((self.WIDTH/2, self.HEIGHT - 100), self.WIDTH)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.score = 0

        #coin
        coin_sprite = Coin(self.WIDTH ,self.HEIGHT)
        self.coin = pygame.sprite.Group(coin_sprite)
        self.coin_adding_time = randint(30, 50)

        #enemy
        enemy_sprite = Enemy(self.WIDTH , self.HEIGHT)
        self.enemy = pygame.sprite.Group(enemy_sprite)
        self.enemy_adding_time = randint(40,50)

        self.gameover = False

        #font
        self.font = pygame.font.Font("game/assets/Font/mago3.ttf", 100)
        self.score_font = pygame.font.Font("game/assets/Font/mago3.ttf", 50)

        #audio
        self.coin_sound = pygame.mixer.Sound('game/assets/Audio/coin.wav')
        self.coin_sound.set_volume(4)

        self.die_sound = pygame.mixer.Sound('game/assets/Audio/die.wav')
        self.die_sound.set_volume(0.1)


    def add_coin(self):
        self.coin_adding_time -= 1
        if self.coin_adding_time <= 0:
            self.coin.add(Coin(self.WIDTH ,self.HEIGHT))
            self.coin_adding_time = randint(30, 50)

    def add_enemy(self):
        self.enemy_adding_time -= 1
        if self.enemy_adding_time <= 0:
            self.enemy.add(Enemy(self.WIDTH,self.HEIGHT))
            self.enemy_adding_time = randint(40, 50)


    def collision(self):
        for coin in self.coin:
            if pygame.sprite.spritecollide(coin, self.player, False):
                self.coin_sound.play()
                coin.kill()
                self.score += 1

        for enemy in self.enemy:
            if pygame.sprite.spritecollide(enemy, self.player, False):
                self.die_sound.play()
                self.gameover = True

    def display_score(self):
        score_surf = self.score_font.render(f'score = {self.score}', False, 'RED')
        score_rect = score_surf.get_rect(center = (self.WIDTH/2, 50))
        self.screen.blit(score_surf,score_rect)

    def gameover_scene(self):
        gameover_surf = self.font.render('Gameover', False, 'RED')
        gameover_rect = gameover_surf.get_rect(center = (self.WIDTH / 2 , self.HEIGHT / 2))
        self.screen.blit(gameover_surf, gameover_rect)

        score_surf = self.score_font.render(f'score = {self.score}', False, 'RED')
        score_rect = score_surf.get_rect(center = (self.WIDTH/2, self.HEIGHT/2 + 50))
        self.screen.blit(score_surf,score_rect)

    def run(self):
        self.screen.blit(self.bg_image, (0,0))

        if self.gameover == False:
            self.player.draw(self.screen)
            self.player.update()

            self.coin.draw(self.screen)
            self.coin.update()
            self.add_coin()

            self.enemy.draw(self.screen)
            self.enemy.update()
            self.add_enemy()

            self.collision()
            self.display_score()
        
        else :
            self.gameover_scene()