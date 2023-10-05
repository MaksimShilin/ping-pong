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
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_wight=0, image_height=0):
        super().__init__(player_image, player_x, player_y, player_speed, image_wight, image_height)
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < x-5:
            self.rect.x += self.speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < x-5:
            self.rect.x -= self.speed
        if self.rect.x > 5:
            self.rect.x += self.speed
        

x = 450
y = 675
window = display.set_mode((x, y))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('background.jpg'), (x, y))
window.blit(background, (0,0))

player1 = Player('redplatform.png', 175, 35, 1, 95, 25)
player2 = Player('blueplatform.png', 175, 625, 2, 95, 25)
ball = Player('ball.png', 250, 300, 2, 65, 65)








end = False
game = True
while game:
    window.blit(background, (0,0))
    player1.reset()
    # player1.update()
    player2.reset()
    player2.move()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
                game = False
        display.update()
        