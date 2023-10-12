from pygame import *
from random import *
from time import sleep
font.init()
mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x=0, player_speed_y=0, image_wight=0, image_height=0):
        super().__init__()
        self.image_wight = image_wight
        self.image_height = image_height
        self.image = transform.scale(image.load(player_image), (image_wight, image_height))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.fps = 40
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x=0, player_speed_y=0, image_wight=0, image_height=0):
        super().__init__(player_image, player_x, player_y, player_speed_x, player_speed_y, image_wight, image_height)
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y < 310:
            self.rect.y += self.speed_y
    def move_automatic(self):
        self.rect.y += self.speed_y
        if self.rect.y <= 5 or self.rect.y >= 310:
            self.speed_y *= -1
    def move_ball(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y <= 5 or self.rect.y >= 325:
            self.speed_y *= -1
        
        if self.rect.x <=5:
            global count_player2
            global player1
            # self.speed_x *= -1
            count_player2 += 1
            self.rect.x = 320
            self.rect.y = 175
            player1.rect.x = 25
            player1.rect.y = 175
            player2.rect.x = 660
            player2.rect.y = 175
            # time.delay(2000)
            self.rect.x -= self.speed_x
            
            
        
        if self.rect.x >= 625:
            global count_player1
            # self.speed_x *= -1
            count_player1 += 1
            self.rect.x = 320
            self.rect.y = 175
            player2.rect.x = 660
            player2.rect.y = 175
            player1.rect.x = 25
            player1.rect.y = 175
            # time.delay(2000)
            self.rect.x += self.speed_x
            
        
        if sprite.collide_rect(ball, player1):
            self.speed_x *= -1
        if sprite.collide_rect(ball, player2):
            self.speed_x *= -1


class Button():
    def __init__(self, x, y, wight, height, color):
        self.rect = Rect(x, y, wight, height)
        self.color = color
        self.x = x
        self.y = y

    def draw_rect(self, border_color=0, new_color=0):
        if border_color == 0:
            border_color = self.color
        if new_color == 0:
            new_color = self.color
        draw.rect(window, self.color, self.rect)
        draw.rect(window, border_color, self.rect, 5)
    
    def create_text(self, size):
        self.font = font.SysFont('Arial', size)

    def draw_text(self, text_color, text, xofset, yofset):
        question = self.font.render(text, True, text_color)
        window.blit(question, (self.x+xofset, self.y+yofset))



            
        

x = 700
y = 400
window = display.set_mode((x, y))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('background.png'), (x, y))
window.blit(background, (0,0))

player1 = Player('redplatform.png', 25, 175, 1, 1, 25, 85)
player2 = Player('blueplatform.png', 660, 175, 1, 1, 25, 85)
ball = Player('ball.png', 320, 175, 1, 1, 65, 65)


start = Button(275, 165, 150, 65, (255, 255, 255))
start.draw_rect((0, 0, 0))
start.create_text(40)
start.draw_text((0, 0, 0), 'GO', 55, 20)

restart = Button(275, 250, 150, 65, (255, 255, 255))





count_player1 = 0
count_player2 = 0
font1 = font.SysFont('Arial', 35)
end = False
game = True
clock = time.Clock()
while game:
    if end:
        window.blit(background, (0,0))
        player1.reset()
        player1.move_automatic()
        player2.reset()
        player2.move()
        ball.reset()
        ball.move_ball()
        count1 = font1.render(str(count_player1), True, (255, 255, 255))
        count2 = font1.render(':'+str(count_player2), True, (255, 255, 255))
        window.blit(count1, (333,10))
        window.blit(count2, (346,10))
        if count_player1 >= 7:
            lose = font1.render('YOU LOSE!', True, (255, 255, 255))
            window.blit(lose, (285, 150))
            end = False
            restart.draw_rect((0, 0, 0))
            restart.create_text(40)
            restart.draw_text((0, 0, 0), 'RESTART', 10, 20)
        if count_player2 >= 7:
            win = font1.render('YOU WIN!', True, (255, 255, 255))
            window.blit(win, (290, 150))
            end = False
            restart.draw_rect((0, 0, 0))
            restart.create_text(40)
            restart.draw_text((0, 0, 0), 'RESTART', 10, 20)
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x_button, y_button = e.pos
            if start.rect.collidepoint(x_button, y_button):
                end = True
            if restart.rect.collidepoint(x_button, y_button):
                count_player1 = 0
                count_player2 = 0
                player1.rect.x = 25
                player1.rect.y = 175
                player1.move_automatic()
                player2.rect.x = 660
                player2.rect.y = 175
                ball.rect.x = 320
                ball.rect.y = 175
                end = True 
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(105)
        