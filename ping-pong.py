from pygame import *
from random import *
font.init()
mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_wight=0, image_height=0):
        super().__init__()
        self.image_wight = image_wight
        self.image_height = image_height
        self.image = transform.scale(image.load(player_image), (image_wight, image_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.fps = 40
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_wight=0, image_height=0):
        super().__init__(player_image, player_x, player_y, player_speed, image_wight, image_height)
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 310:
            self.rect.y += self.speed
    def move_automatic(self):
        self.rect.y -= self.speed
        if self.rect.y >= 5:
            self.rect.y -= self.speed
        if self.rect.y <= 310:
            self.rect.y += self.speed
    def move_ball(self):
        self.rect.y += self.speed
        self.rect.x += self.speed
        if self.rect.x <= 70 or self.rect.y >= 630:
            self.speed *= -1
            
        

x = 700
y = 400
window = display.set_mode((x, y))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('background.png'), (x, y))
window.blit(background, (0,0))

player1 = Player('redplatform.png', 25, 175, 1, 25, 85)
player2 = Player('blueplatform.png', 660, 175, 2, 25, 85)
ball = Player('ball.png', 350, 200, 1, 65, 65)








end = False
game = True
clock = time.Clock()
while game:
    window.blit(background, (0,0))
    player1.reset()
    # player1.move_automatic()
    player2.reset()
    player2.move()
    ball.reset()
    # ball.move_ball()
    for e in event.get():
        if e.type == QUIT:
                game = False
        display.update()
        clock.tick(105)
        