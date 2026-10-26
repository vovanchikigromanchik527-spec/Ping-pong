from pygame import *
from random import *
from time import time as timer

window = display.set_mode((700, 500))
display.set_caption('Ping-pong')
background = transform.scale(image.load("sky.jpg"), (700, 500))
win_width = 700
win_height = 500
game = True
FPS = 40
score1 = 0
lose_score1 = 0
clock = time.Clock()
finish = False
font.init()
font = font.SysFont('Arial', 36)
lose_scire_right = 0
lose_scire_left = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wid, hei):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wid, hei))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

ball = GameSprite('ball.png', 350, 250, 3, 25, 25)
racket1 = Player('racket1.png', 5, 250, 3, 100, 100)
racket2 = Player('racket2.png', 620, 250, 3, 100, 100)
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        racket1.update_l()
        racket2.update_r()

        if sprite.collide_rect(ball, racket1):
            speed_x = 3
        if sprite.collide_rect(ball, racket2):
            speed_x = -3
        if ball.rect.y > 475:
            speed_y = -3
        if ball.rect.x > 675:
            speed_x = -3
            lose_scire_right += 1
        if ball.rect.y < 0:
            speed_y = 3
        if ball.rect.x < 0:
            lose_scire_left += 1
            speed_x = 3

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.update()
        racket1.reset()
        racket2.update()
        racket2.reset()
        ball.reset()

    score_left = font.render(('Счёт левого: ' + str(lose_scire_left)), True, (255, 255, 255))
    score_right = font.render(('Счёт правого: ' + str(lose_scire_right)), True, (255, 255, 255))
    left_lose = font.render("LEFT Win!", True, (255, 215, 0))
    right_lose = font.render('RIGHT Lose!', True, (180, 0, 0))
    window.blit(score_left, (10, 20))
    window.blit(score_right, (10, 45))

    if lose_scire_left >= 3:
        window.blit(left_lose, (300, 225))
        game = False
    if lose_scire_right >= 3:
        window.blit(right_lose, (300, 225))
        game = False

    display.update()
    clock.tick(60)
    window.blit(background, (0,0))
